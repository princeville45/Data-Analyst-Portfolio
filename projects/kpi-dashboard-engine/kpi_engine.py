"""
KPI Dashboard Engine
Author: Irem Victor Chinonso (princeville45)
Description: A module for calculating, monitoring, and reporting business KPIs.
"""

import pandas as pd

class KPIDashboard:
    """Calculates and monitors business KPIs."""
    
    def __init__(self, metrics):
        """
        Initialize with raw business metrics dictionary.
        Expected keys: revenue, customers, conversion_rate, churn, aov, last_month_revenue
        """
        self.metrics = metrics
        self.kpis = {}
        self.targets = {
            'mom_growth': 5.0,
            'churn_rate': 2.0,
            'clv': 500.0
        }

    def calculate_kpis(self):
        """Calculates derived KPIs from raw metrics."""
        m = self.metrics
        
        # MoM Growth
        if 'last_month_revenue' in m and m['last_month_revenue'] > 0:
            self.kpis['mom_growth'] = ((m['revenue'] - m['last_month_revenue']) / m['last_month_revenue']) * 100
        else:
            self.kpis['mom_growth'] = 0.0
            
        # Revenue per Customer (ARPU)
        if m['customers'] > 0:
            self.kpis['rev_per_customer'] = m['revenue'] / m['customers']
        else:
            self.kpis['rev_per_customer'] = 0.0
            
        # Estimated Customer Lifetime Value (CLV)
        # Simplified: CLV = AOV / Churn Rate
        if m['churn'] > 0:
            self.kpis['estimated_clv'] = m['aov'] / (m['churn'] / 100)
        else:
            self.kpis['estimated_clv'] = 0.0
            
        self.kpis['churn_rate'] = m['churn']
        
    def get_status(self, kpi_name, value):
        """Returns a status flag (Red/Yellow/Green) based on targets."""
        if kpi_name == 'mom_growth':
            if value >= self.targets['mom_growth']: return "🟢 GREEN"
            if value > 0: return "🟡 YELLOW"
            return "🔴 RED"
            
        if kpi_name == 'churn_rate':
            if value <= self.targets['churn_rate']: return "🟢 GREEN"
            if value < self.targets['churn_rate'] * 2: return "🟡 YELLOW"
            return "🔴 RED"
            
        if kpi_name == 'estimated_clv':
            if value >= self.targets['clv']: return "🟢 GREEN"
            return "🔴 RED"
            
        return "⚪ N/A"

    def generate_report(self):
        """Prints a formatted KPI report."""
        self.calculate_kpis()
        
        print("\n" + "="*40)
        print("       BUSINESS KPI DASHBOARD")
        print("="*40)
        
        for kpi, val in self.kpis.items():
            status = self.get_status(kpi, val)
            print(f"{kpi.replace('_', ' ').upper():<20} : {val:>8.2f} {status}")
            
        print("-" * 40)
        print("Benchmark Comparison (Target MoM: 5.0%)")
        print("="*40)

if __name__ == "__main__":
    # Sample RevOps Metrics
    raw_data = {
        'revenue': 55000,
        'last_month_revenue': 50000,
        'customers': 1200,
        'conversion_rate': 3.5,
        'churn': 1.8,
        'aov': 45.0
    }
    
    dashboard = KPIDashboard(raw_data)
    dashboard.generate_report()
