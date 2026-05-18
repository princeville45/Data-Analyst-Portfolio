def calculate_hhi_index(market_shares):
    """Calculates the Herfindahl-Hirschman Index (HHI) for market concentration analysis."""
    # market_shares: list of percentages (e.g., [40, 30, 20, 10])
    return sum([share**2 for share in market_shares])