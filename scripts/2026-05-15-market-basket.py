from itertools import combinations
from collections import Counter

def get_frequent_itemsets(transactions, min_support=2):
    """Simple frequent itemset generator for retail market basket analysis."""
    item_counts = Counter()
    for t in transactions:
        for pair in combinations(sorted(t), 2):
            item_counts[pair] += 1
    return {k: v for k, v in item_counts.items() if v >= min_support}