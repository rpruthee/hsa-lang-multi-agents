def validate_hsa_contribution(contribution, limit):
    # Validate that the contribution does not exceed the IRS limit
    if contribution < 0:
        raise ValueError("Contribution cannot be negative.")
    if contribution > limit:
        raise ValueError(f"Contribution exceeds the limit of {limit}.")
    return True

def validate_hsa_distribution(distribution, qualified_expenses):
    # Validate that the distribution is for qualified medical expenses
    if distribution < 0:
        raise ValueError("Distribution cannot be negative.")
    if distribution > sum(qualified_expenses):
        raise ValueError("Distribution exceeds the total of qualified medical expenses.")
    return True

def validate_eligibility(age, is_covered_by_high_deductible_plan):
    # Validate eligibility for HSA based on age and insurance coverage
    if age < 18:
        raise ValueError("Must be at least 18 years old to contribute to an HSA.")
    if not is_covered_by_high_deductible_plan:
        raise ValueError("Must be covered by a high-deductible health plan to contribute to an HSA.")
    return True

def validate_data_integrity(data):
    # Validate that the provided data is not None and is of the expected type
    if data is None:
        raise ValueError("Data cannot be None.")
    if not isinstance(data, (int, float)):
        raise ValueError("Data must be a number.")
    return True