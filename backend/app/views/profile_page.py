from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def holdings(request):
    holdings = [
        { 'id': 1, 'asset': 'SPDR S&P 500 ETF', 'quantity': 100.234, 'value': 45000.56, 'change_value': 500.12, 'percentage_change': 1.123 },
        { 'id': 2, 'asset': 'Vanguard Total Stock Market ETF', 'quantity': 150.567, 'value': 34500.78, 'change_value': 300.45, 'percentage_change': 0.874 },
        { 'id': 3, 'asset': 'iShares MSCI Emerging Markets ETF', 'quantity': 200.891, 'value': 11000.34, 'change_value': 100.23, 'percentage_change': 0.912 },
        { 'id': 4, 'asset': 'Invesco QQQ Trust', 'quantity': 50.123, 'value': 18500.89, 'change_value': 700.67, 'percentage_change': 3.934 },
        { 'id': 5, 'asset': 'Schwab U.S. Dividend Equity ETF', 'quantity': 120.456, 'value': 9000.12, 'change_value': 150.34, 'percentage_change': 1.693 },
        { 'id': 6, 'asset': 'ARK Innovation ETF', 'quantity': 80.789, 'value': 9600.45, 'change_value': 400.56, 'percentage_change': 4.354 },
        { 'id': 7, 'asset': 'iShares Russell 2000 ETF', 'quantity': 70.234, 'value': 14700.67, 'change_value': 350.78, 'percentage_change': 2.432 },
        { 'id': 8, 'asset': 'Vanguard FTSE Developed Markets ETF', 'quantity': 180.567, 'value': 9000.89, 'change_value': 80.12, 'percentage_change': 0.894 },
        { 'id': 9, 'asset': 'Bitcoin (BTC)', 'quantity': 0.543, 'value': 30000.34, 'change_value': 2000.45, 'percentage_change': 7.143 },
        { 'id': 10, 'asset': 'Ethereum (ETH)', 'quantity': 2.345, 'value': 4000.56, 'change_value': 300.67, 'percentage_change': 8.114 },
    ]

    return Response(holdings)

@api_view(['GET'])
def buyandsell_transaction(request):
    ...