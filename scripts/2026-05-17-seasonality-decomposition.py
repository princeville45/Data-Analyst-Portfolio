import statsmodels.api as sm

def decompose_seasonality(series, freq=12):
    """Performs seasonal decomposition on a time series dataset."""
    decomposition = sm.tsa.seasonal_decompose(series, model='additive', period=freq)
    return decomposition.trend, decomposition.seasonal, decomposition.resid