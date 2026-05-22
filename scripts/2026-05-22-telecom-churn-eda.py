import pandas as pd

def telecom_churn_insights(df):
    """EDA function for identifying key churn drivers in telecom subscriber data."""
    report = {
        'churn_rate': df['churn'].mean() * 100,
        'data_usage_v_churn': df.groupby('churn')['data_usage_gb'].mean().to_dict(),
        'tenure_bins': pd.cut(df['tenure_months'], bins=[0, 6, 12, 24, 60]).value_counts().to_dict()
    }
    return report