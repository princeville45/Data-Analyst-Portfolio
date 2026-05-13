def rfm_segment(r, f, m):
    if r <= 30 and f >= 10 and m >= 1000: return 'Champion'
    if r > 90: return 'At Risk'
    return 'Standard'