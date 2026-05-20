import statsmodels.api as sm
import pandas as pd

def sales_trend_seasonality(df, period=12):
    """Decomposes sales data into trend, seasonal, and residual components."""
    # df should have a datetime index and 'sales' column
    res = sm.tsa.seasonal_decompose(df['sales'], model='additive', period=period)
    return res.trend, res.seasonal, res.resid