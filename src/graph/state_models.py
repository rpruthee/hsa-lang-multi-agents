from dataclasses import dataclass

@dataclass
class HSAState:
    """Represents the state of the HSA process."""
    eligibility: bool
    contributions: float
    distributions: float
    compliance_status: bool

    def update_eligibility(self, eligibility: bool):
        """Update the eligibility status."""
        self.eligibility = eligibility

    def update_contributions(self, amount: float):
        """Update the total contributions to the HSA."""
        self.contributions += amount

    def update_distributions(self, amount: float):
        """Update the total distributions from the HSA."""
        self.distributions += amount

    def update_compliance_status(self, status: bool):
        """Update the compliance status of the HSA."""
        self.compliance_status = status

    def reset(self):
        """Reset the state for a new HSA process."""
        self.eligibility = False
        self.contributions = 0.0
        self.distributions = 0.0
        self.compliance_status = True  # Assume compliant by default

# Additional state models can be defined here as needed for the workflow.