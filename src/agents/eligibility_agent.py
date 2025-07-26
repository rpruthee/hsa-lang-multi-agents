from typing import Dict, Any

from src.agents.base_agent import BaseHSAAgent
from src.graph.hsa_state import HSAState
from src.utils.irs_rules import IRSRules

class EligibilityAgent(BaseHSAAgent):
    """Agent responsible for determining HSA eligibility based on IRS rules."""
    
    def __init__(self):
        super().__init__("EligibilityAgent")
        self.irs_rules = IRSRules()
    
    def process(self, state: HSAState) -> HSAState:
        """Process eligibility check for HSA participation."""
        # Update metadata
        state = self._update_state_metadata(state)
        state["current_step"] = "eligibility_check"
        
        # Get user data
        user_data = state.get("user_data", {})
        
        # Check eligibility
        has_hdhp = user_data.get("has_hdhp", False)
        has_other_coverage = user_data.get("has_other_health_coverage", False)
        enrolled_in_medicare = user_data.get("enrolled_in_medicare", False)
        claimed_as_dependent = user_data.get("claimed_as_dependent", False)
        
        # Determine eligibility
        is_eligible = (has_hdhp and 
                      not has_other_coverage and 
                      not enrolled_in_medicare and 
                      not claimed_as_dependent)
        
        if is_eligible:
            reason = "Meets all IRS eligibility requirements for HSA participation"
        else:
            reason = "Does not meet HSA eligibility requirements"
        
        # Update state
        state["is_eligible"] = is_eligible
        state["eligibility_reason"] = reason
        state["workflow_status"] = "in_progress"
        
        # Add message
        message = f"Eligibility check completed: {'Eligible' if is_eligible else 'Not Eligible'}"
        state = self._add_message(state, message)
        
        return state