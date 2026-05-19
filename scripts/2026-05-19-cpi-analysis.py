import pandas as pd

def analyze_cpi_trend(df):
    """Analyzes Month-on-Month (MoM) inflation from Nigerian CPI data."""
    df['MoM_Inflation'] = df['CPI'].pct_change() * 100
    avg_inflation = df['MoM_Inflation'].mean()
    return round(avg_inflation, 2)