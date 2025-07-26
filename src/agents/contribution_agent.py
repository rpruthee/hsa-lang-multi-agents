from typing import Dict, Any, List

from src.agents.base_agent import BaseHSAAgent
from src.graph.hsa_state import HSAState
from src.utils.irs_rules import IRSRules

class ContributionAgent(BaseHSAAgent):
    """Agent responsible for processing HSA contributions."""
    
    def __init__(self):
        super().__init__("ContributionAgent")
        self.irs_rules = IRSRules()
    
    def process(self, state: HSAState) -> HSAState:
        """Process HSA contribution request."""
        # Simple implementation for now
        state = self._update_state_metadata(state)
        state["current_step"] = "contribution_processing"
        
        user_data = state.get("user_data", {})
        requested_amount = user_data.get("contribution_amount", 0.0)
        
        # Basic validation
        state["contribution_amount"] = requested_amount
        state["contribution_valid"] = requested_amount > 0
        state["contribution_errors"] = [] if requested_amount > 0 else ["Invalid amount"]
        
        message = f"Contribution processing completed for ${requested_amount}"
        state = self._add_message(state, message)
        
        return state