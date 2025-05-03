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