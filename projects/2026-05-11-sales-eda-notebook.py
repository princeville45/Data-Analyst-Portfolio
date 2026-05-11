import pandas as pd
import numpy as np

def perform_sales_eda():
    """
    Performs Exploratory Data Analysis on a synthetic monthly sales dataset.
    """
    # Create synthetic dataset
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    categories = ['Electronics', 'Groceries', 'Apparel', 'Home', 'Health']
    
    data = []
    for month in months:
        for cat in categories:
            data.append({
                'Month': month,
                'Category': cat,
                'Sales': np.random.randint(5000, 20000),
                'Orders': np.random.randint(50, 200)
            })
    
    df = pd.DataFrame(data)
    
    # Summary Statistics
    print("--- Summary Statistics ---")
    print(df.describe())
    
    # Month-over-Month Growth
    monthly_sales = df.groupby('Month')['Sales'].sum().reindex(months)
    mom_growth = monthly_sales.pct_change() * 100
    
    print("\n--- Month-over-Month Growth (%) ---")
    print(mom_growth)
    
    # Top Category Analysis
    cat_summary = df.groupby('Category').agg({'Sales': 'sum', 'Orders': 'sum'}).sort_values(by='Sales', ascending=False)
    print("\n--- Top Category Performance ---")
    print(cat_summary)
    
    # Trend Detection (Regression slope)
    x = np.arange(len(monthly_sales))
    y = monthly_sales.values
    slope, intercept = np.polyfit(x, y, 1)
    print(f"\nOverall Sales Trend (Slope): {slope:.2f} USD/month")

if __name__ == "__main__":
    perform_sales_eda()
