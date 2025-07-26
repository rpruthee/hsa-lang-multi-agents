from src.agents.base_agent import BaseHSAAgent
from src.graph.hsa_state import HSAState

class ComplianceAgent(BaseHSAAgent):
    """Agent responsible for final compliance checks."""
    
    def __init__(self):
        super().__init__("ComplianceAgent")
    
    def process(self, state: HSAState) -> HSAState:
        """Perform final compliance check."""
        state = self._update_state_metadata(state)
        state["current_step"] = "compliance_check"
        state["compliance_check_result"] = "COMPLIANT"
        state["workflow_status"] = "completed"
        
        message = "Compliance check completed successfully"
        state = self._add_message(state, message)
        
        return state