## 4. Comprehensive Rules Summary

# HSA IRS Rules Implementation Summary

## Overview
This document summarizes all IRS rules and regulations implemented across the HSA Multi-Agent System. These rules are based on IRS Publication 969 and current tax law.

This comprehensive documentation covers all aspects of the HSA agents and the IRS rules they implement. Each agent has detailed documentation explaining their responsibilities, the rules they enforce, input/output formats, and integration points with other agents.

## Core HSA Rules

### Eligibility Requirements (IRC Section 223)

#### Must Have High Deductible Health Plan (HDHP)
- **2024 Minimum Deductibles**:
  - Individual: $1,600
  - Family: $3,200
- **2024 Maximum Out-of-Pocket**:
  - Individual: $8,050
  - Family: $16,100

#### Disqualifying Factors
1. **Other Health Coverage**: Cannot have non-HDHP coverage
2. **Medicare Enrollment**: Cannot contribute while enrolled in Medicare
3. **Dependent Status**: Cannot contribute if claimed as dependent
4. **Spouse Coverage**: Spouse's non-HDHP coverage can disqualify

### Contribution Rules (IRC Section 223(b))

#### Annual Contribution Limits
```python
# 2024 Contribution Limits
CONTRIBUTION_LIMITS = {
    "individual": {
        "annual_limit": 4150.00,
        "catch_up_limit": 1000.00  # Age 55+
    },
    "family": {
        "annual_limit": 8300.00,
        "catch_up_limit": 1000.00  # Age 55+
    }
}

def calculate_distribution_tax(amount, age, tax_rate):
    """Calculate tax and penalty for non-qualified distribution"""
    income_tax = amount * tax_rate
    penalty = amount * 0.20 if age < 65 else 0.0
    return {
        "income_tax": income_tax,
        "penalty": penalty,
        "total_tax": income_tax + penalty
    }

def calculate_contribution_limit(coverage_type, age, year):
    """Calculate total contribution limit including catch-up"""
    base_limit = CONTRIBUTION_LIMITS[year][coverage_type]["annual_limit"]
    catch_up = CONTRIBUTION_LIMITS[year][coverage_type]["catch_up_limit"] if age >= 55 else 0
    return base_limit + catch_up
```