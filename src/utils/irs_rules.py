# Contents of /hsa-multi-agent-system/hsa-multi-agent-system/src/utils/irs_rules.py

from typing import Dict, Any

class IRSRules:
    """
    Utility class containing IRS rules and limits for HSA management.
    Centralizes all IRS-related calculations and validations.
    """
    
    def __init__(self):
        """Initialize IRS rules with current year limits."""
        self.contribution_limits = {
            2024: {
                "individual": {
                    "annual_limit": 4150.00,
                    "catch_up_limit": 1000.00
                },
                "family": {
                    "annual_limit": 8300.00,
                    "catch_up_limit": 1000.00
                }
            }
        }
        
    def get_contribution_limits(self, year: int, coverage_type: str) -> Dict[str, float]:
        """
        Get HSA contribution limits for specified year and coverage type.
        
        Args:
            year: Tax year
            coverage_type: 'individual' or 'family'
            
        Returns:
            Dictionary with contribution limits
        """
        if year not in self.contribution_limits:
            # Default to most recent year
            year = max(self.contribution_limits.keys())
        
        return self.contribution_limits[year].get(coverage_type, self.contribution_limits[year]["individual"])
    
    def is_qualified_medical_expense(self, expense_type: str) -> bool:
        """
        Check if expense type qualifies as medical expense under IRS rules.
        
        Args:
            expense_type: Type of medical expense
            
        Returns:
            True if qualified medical expense
        """
        qualified_expenses = {
            "medical_care", "prescription_drugs", "dental_care", "vision_care",
            "hospital_expenses", "doctor_visits", "medical_equipment"
        }
        
        return expense_type.lower() in qualified_expenses