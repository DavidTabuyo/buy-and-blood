import yfinance as yf
from typing import List
from app.models import Plan, PlanAsset

def get_asset_percentage_change(symbol_yf: str) -> float:
    """
    Download the last two daily closes for the given symbol and return
    the % change from the close 24h ago to the most recent close.
    
    If data is unavailable or an error occurs, returns 0.0.
    """
    try:
        # Download the last 2 days of daily data
        df = yf.download(
            tickers=symbol_yf,
            period="2d",
            interval="1d",
            progress=False,
            threads=False
        )
        # If df has a MultiIndex, flatten it:
        if isinstance(df.columns, pd.MultiIndex):
            df = df[symbol_yf]
        # Compute change
        prev_close = df['Close'].iloc[-2] # Yesterday close price
        last_close = df['Close'].iloc[-1] # Today close price
        return (last_close - prev_close) / prev_close * 100
    except Exception:
        return 0.0

def get_plan_percentage_change(plan: Plan) -> float:
    """
    For the given Plan, fetch all related PlanAsset entries,
    get each asset’s 24 h % change, then return the weighted
    average according to PlanAsset.percentage.
    
    If the plan has no assets or total weight is zero, returns 0.0.
    """
    # Fetch all PlanAsset rows in one go
    plan_assets = (
        PlanAsset.objects
        .filter(plan=plan)
        .select_related('asset')
    )
    # Build lists of weights and individual pct changes
    weights: List[float] = []
    changes: List[float] = []
    for pa in plan_assets:
        weight = float(pa.percentage)
        pct = get_asset_percentage_change(pa.asset.symbol_yf)
        weights.append(weight)
        changes.append(pct)
    
    total_weight = sum(weights)
    if total_weight <= 0 or not changes:
        return 0.0

    # Weighted average
    weighted_avg = sum(w * c for w, c in zip(weights, changes)) / total_weight
    return round(weighted_avg, 2)
    