import pandas as pd

def fmcg_inventory_insights(df):
    """Provides high-level EDA insights for a Fast-Moving Consumer Goods dataset."""
    insights = {
        'top_skus': df.groupby('product_name')['sales'].sum().nlargest(5).to_dict(),
        'out_of_stock_rate': (df['stock_level'] == 0).mean() * 100,
        'regional_performance': df.groupby('region')['revenue'].sum().sort_values(ascending=False).to_dict()
    }
    return insights