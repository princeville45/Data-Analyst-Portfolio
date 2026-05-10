# Project: Statistical Inference Suite

## Overview
Statistics is the backbone of reliable business intelligence. This project demonstrates how to move beyond "gut feelings" by using frequentist statistical methods to validate business hypotheses.

## Scenarios Covered

### 1. Performance vs. Benchmarks (One-Sample T-Test)
**Scenario**: Does our daily revenue actually exceed our $1,000 target, or is the observed mean just due to random noise?
**Value**: Validates if growth strategies are actually working.

### 2. A/B Testing (Two-Sample T-Test)
**Scenario**: We launched two different pricing models for Category A and Category B. Is one actually performing better?
**Value**: Essential for optimizing product strategy and marketing spend.

### 3. Market Segmentation (Chi-Square Test)
**Scenario**: Does a customer's region influence their product preference (Basic vs. Premium)?
**Value**: Helps in localized marketing and inventory distribution.

## Technical Implementation
The suite utilizes `scipy.stats` for rigorous computation. Each test returns a p-value, which is then interpreted against a standard significance level (alpha = 0.05) to provide a clear, plain-English conclusion for non-technical stakeholders.
