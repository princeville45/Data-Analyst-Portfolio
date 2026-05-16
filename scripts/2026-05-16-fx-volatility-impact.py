import pandas as pd

def correlate_fx_to_imports(fx_df, import_df):
    """Analyzes the impact of NGN/USD volatility on import costs."""
    merged = pd.merge(fx_df, import_df, on='date')
    correlation = merged['fx_rate'].corr(merged['import_value'])
    return round(correlation, 2)