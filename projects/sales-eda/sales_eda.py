"""
Sales Exploratory Data Analysis (EDA) Engine
Author: Irem Victor Chinonso (princeville45)
Description: A standalone script to generate synthetic sales data and perform full EDA.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def generate_synthetic_data(rows=1000):
    """Generates a realistic synthetic sales dataset."""
    np.random.seed(42)
    
    start_date = datetime(2025, 1, 1)
    dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(rows)]
    
    products = ['Product A', 'Product B', 'Product C', 'Product D']
    regions = ['North', 'South', 'East', 'West']
    
    data = {
        'order_id': range(1001, 1001 + rows),
        'date': dates,
        'product': np.random.choice(products, rows),
        'region': np.random.choice(regions, rows),
        'quantity': np.random.randint(1, 10, rows),
        'unit_price': np.random.uniform(10.0, 500.0, rows)
    }
    
    df = pd.DataFrame(data)
    df['revenue'] = df['quantity'] * df['unit_price']
    
    # Introduce some outliers
    df.loc[np.random.choice(df.index, 10), 'revenue'] *= 10
    
    # Introduce some missing values
    df.loc[np.random.choice(df.index, 5), 'quantity'] = np.nan
    
    return df

def perform_eda(df):
    """Performs Exploratory Data Analysis on the dataframe."""
    print("--- DATA OVERVIEW ---")
    print(f"Shape: {df.shape}")
    print("\nData Types:")
    print(df.dtypes)
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Cleaning missing values for analysis
    df = df.dropna().copy()
    
    print("\n--- DESCRIPTIVE STATISTICS ---")
    print(df.describe())
    
    # Revenue Analysis
    total_revenue = df['revenue'].sum()
    rev_by_product = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
    rev_by_region = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
    
    df['month'] = df['date'].dt.to_period('M')
    rev_by_month = df.groupby('month')['revenue'].sum()
    
    # Sales Velocity (Quantity per product)
    velocity = df.groupby('product')['quantity'].sum().sort_values(ascending=False)
    
    # Trend Analysis (Month-over-Month)
    mom_growth = rev_by_month.pct_change() * 100
    
    # Outlier Detection (IQR Method)
    Q1 = df['revenue'].quantile(0.25)
    Q3 = df['revenue'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df['revenue'] < lower_bound) | (df['revenue'] > upper_bound)]
    
    # REPORTING
    print("\n" + "="*50)
    print("            SALES ANALYTICAL REPORT")
    print("="*50)
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print("\nRevenue by Product:")
    print(rev_by_product)
    print("\nRevenue by Region:")
    print(rev_by_region)
    print("\nTop Selling Product (Velocity):", velocity.idxmax())
    print("\nAverage MoM Growth Rate:", mom_growth.mean().round(2), "%")
    print("\nStatistical Outliers Detected:", len(outliers))
    print("="*50)

if __name__ == "__main__":
    sales_df = generate_synthetic_data()
    perform_eda(sales_df)
