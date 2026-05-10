"""
Statistical Inference Suite
Author: Irem Victor Chinonso (princeville45)
Description: Demonstration of hypothesis testing for business decision making.
"""

import numpy as np
from scipy import stats

def run_hypothesis_tests():
    """Runs a series of statistical tests on synthetic data."""
    np.random.seed(42)
    
    # 1. One-Sample T-Test: Is average daily revenue significantly different from target?
    # Target: $1000/day. Actual: Sample of 30 days.
    target_rev = 1000
    daily_revenue = np.random.normal(loc=1050, scale=100, size=30)
    t_stat, p_val = stats.ttest_1samp(daily_revenue, target_rev)
    
    print("--- TEST 1: ONE-SAMPLE T-TEST (Revenue vs Target) ---")
    print(f"Sample Mean: ${daily_revenue.mean():.2f} | P-Value: {p_val:.4f}")
    if p_val < 0.05:
        print("Conclusion: The difference is statistically significant. We are beating the target.")
    else:
        print("Conclusion: No significant difference found from the target.")
        
    # 2. Two-Sample T-Test: Are two product categories performing differently?
    cat_a_sales = np.random.normal(loc=200, scale=30, size=50)
    cat_b_sales = np.random.normal(loc=210, scale=35, size=50)
    t_stat_2, p_val_2 = stats.ttest_ind(cat_a_sales, cat_b_sales)
    
    print("\n--- TEST 2: TWO-SAMPLE T-TEST (Product A vs Product B) ---")
    print(f"Cat A Mean: {cat_a_sales.mean():.2f} | Cat B Mean: {cat_b_sales.mean():.2f} | P-Value: {p_val_2:.4f}")
    if p_val_2 < 0.05:
        print("Conclusion: There is a statistically significant difference in performance between categories.")
    else:
        print("Conclusion: No statistically significant difference in performance detected.")

    # 3. Chi-Square Test: Is there a relationship between region and product preference?
    # Rows: Region (North, South) | Cols: Product (Basic, Premium)
    observed = np.array([[30, 70], [50, 50]]) 
    chi2, p_val_3, dof, ex = stats.chi2_contingency(observed)
    
    print("\n--- TEST 3: CHI-SQUARE TEST (Region vs Product Preference) ---")
    print(f"Chi2 Stat: {chi2:.4f} | P-Value: {p_val_3:.4f}")
    if p_val_3 < 0.05:
        print("Conclusion: Region and Product preference are dependent. Location affects choice.")
    else:
        print("Conclusion: No significant relationship found between Region and Product preference.")

if __name__ == "__main__":
    print("="*60)
    print("      STATISTICAL INFERENCE FOR BUSINESS DECISIONS")
    print("="*60)
    run_hypothesis_tests()
    print("="*60)
