# Project: KPI Dashboard Engine

## Overview
The KPI Dashboard Engine is a Python-based utility designed for Revenue Operations (RevOps) and Business Intelligence (BI) teams. It automates the calculation of critical business metrics and provides visual status indicators (Red/Yellow/Green) based on predefined targets.

## Tracked Metrics
- **MoM Growth**: Month-over-Month revenue expansion.
- **ARPU**: Average Revenue Per User/Customer.
- **CLV (Estimated)**: Customer Lifetime Value calculated using Average Order Value and Churn Rate.
- **Churn Rate**: Customer attrition monitoring.

## Business Use Case
In a fast-paced business environment, manually calculating KPIs is error-prone and slow. This engine allows a RevOps Lead to:
1.  **Monitor Health**: Immediately see which parts of the business are underperforming (Red status).
2.  **Benchmark**: Compare current performance against historical data or industry standards.
3.  **Automate Reporting**: Generate consistent reports that can be piped into emails or Slack updates.

## Technical Design
The engine is built around the `KPIDashboard` class, making it easy to integrate into larger automation pipelines. It uses dictionary-based input for flexibility and includes built-in logic for handling edge cases like zero-division.
