# HSA Contribution Agent Documentation

## Overview
The Contribution Agent is responsible for processing and validating HSA contribution requests according to IRS rules and regulations. It ensures that all contribution amounts comply with annual limits, eligibility requirements, and timing constraints.

## Agent Responsibilities

### Primary Functions
- **Contribution Validation**: Validates requested contribution amounts against IRS limits
- **Limit Calculation**: Determines applicable contribution limits based on coverage type and age
- **Catch-up Contribution Processing**: Handles additional contributions for individuals aged 55+
- **Deadline Verification**: Ensures contributions are made within IRS deadlines
- **Existing Contribution Tracking**: Prevents over-contribution by tracking existing contributions

### State Management
The agent processes and updates the following state fields:
- `contribution_amount`: The requested contribution amount
- `contribution_limit`: The applicable contribution limit for the user
- `contribution_valid`: Boolean indicating if the contribution is valid
- `contribution_errors`: List of validation errors if any

## IRS Rules Implemented

### Annual Contribution Limits (2024)
- **Individual Coverage**: $4,150
- **Family Coverage**: $8,300
- **Catch-up Contribution**: Additional $1,000 for individuals aged 55+

### Validation Rules

#### 1. Amount Validation
```python
# Must be greater than zero
if amount <= 0:
    errors.append("Contribution amount must be greater than zero")