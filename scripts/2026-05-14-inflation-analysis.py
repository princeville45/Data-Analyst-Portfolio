import pandas as pd

def analyze_cpi_trend(df):
    """Analyzes year-over-year CPI changes for Nigeria."""
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df['YoY_Inflation'] = df['CPI'].pct_change(periods=12) * 100
    avg_inflation = df['YoY_Inflation'].mean()
    return avg_inflation, df[['Date', 'YoY_Inflation']].tail(5)