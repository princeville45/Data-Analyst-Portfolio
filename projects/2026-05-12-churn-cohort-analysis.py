"""
Churn Cohort Analysis Engine
Author: Irem Victor Chinonso | Statistical Business Architect
Date: 2026-05-12
Repo: Data-Analyst-Portfolio

Analyzes customer churn by acquisition cohort.
Identifies which cohorts have the highest lifetime value retention.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_customer_data(n=500):
    """Simulate customer acquisition and churn data."""
    random.seed(42)
    np.random.seed(42)

    cohorts = pd.date_range("2025-01-01", periods=12, freq="MS")
    records = []

    for i in range(n):
        cohort = random.choice(cohorts)
        tenure = np.random.randint(1, 13)
        churned = np.random.choice([0, 1], p=[0.65, 0.35])
        monthly_value = round(np.random.uniform(2000, 25000), 2)
        records.append({
            "customer_id": f"CUST-{i+1:04d}",
            "cohort_month": cohort.strftime("%Y-%m"),
            "tenure_months": tenure,
            "churned": churned,
            "monthly_value_ngn": monthly_value,
            "total_value_ngn": round(monthly_value * tenure, 2)
        })

    return pd.DataFrame(records)


def build_cohort_retention_matrix(df):
    """Build a month-by-month retention matrix per cohort."""
    cohort_sizes = df.groupby("cohort_month")["customer_id"].nunique()
    retention = df.groupby(["cohort_month", "tenure_months"])["customer_id"].nunique().unstack()
    retention_rate = retention.divide(cohort_sizes, axis=0).round(4) * 100
    return retention_rate


def compute_cohort_ltv(df):
    """Compute average LTV per cohort."""
    ltv = df.groupby("cohort_month").agg(
        avg_ltv=("total_value_ngn", "mean"),
        total_revenue=("total_value_ngn", "sum"),
        customers=("customer_id", "nunique"),
        churn_rate=("churned", "mean")
    ).round(2)
    ltv["churn_rate_pct"] = (ltv["churn_rate"] * 100).round(1)
    ltv.drop(columns=["churn_rate"], inplace=True)
    return ltv.sort_values("avg_ltv", ascending=False)


def flag_at_risk_cohorts(ltv_df, churn_threshold=40.0):
    """Flag cohorts with churn rate above threshold."""
    at_risk = ltv_df[ltv_df["churn_rate_pct"] > churn_threshold]
    return at_risk


def run_analysis():
    print("=" * 60)
    print("CHURN COHORT ANALYSIS ENGINE")
    print("Statistical Business Architect | Irem Victor Chinonso")
    print("=" * 60)

    df = generate_customer_data(500)

    print(f"\nDataset: {len(df)} customer records across {df['cohort_month'].nunique()} cohorts\n")

    retention_matrix = build_cohort_retention_matrix(df)
    print("--- RETENTION MATRIX (%) ---")
    print(retention_matrix.to_string())

    ltv_df = compute_cohort_ltv(df)
    print("\n--- COHORT LTV ANALYSIS ---")
    print(ltv_df.to_string())

    at_risk = flag_at_risk_cohorts(ltv_df)
    if not at_risk.empty:
        print(f"\n--- AT-RISK COHORTS (Churn > 40%) ---")
        print(at_risk[["customers", "avg_ltv", "churn_rate_pct"]].to_string())
    else:
        print("\nNo cohorts above churn threshold. Retention is healthy.")

    best_cohort = ltv_df["avg_ltv"].idxmax()
    worst_cohort = ltv_df["churn_rate_pct"].idxmax()
    print(f"\nBest LTV Cohort: {best_cohort} | Avg LTV: ₦{ltv_df.loc[best_cohort, 'avg_ltv']:,.0f}")
    print(f"Highest Churn Cohort: {worst_cohort} | Churn Rate: {ltv_df.loc[worst_cohort, 'churn_rate_pct']}%")
    print("\nAnalysis complete.")


if __name__ == "__main__":
    run_analysis()
