from src.agents.base_agent import BaseHSAAgent
from src.graph.hsa_state import HSAState

class DistributionAgent(BaseHSAAgent):
    """Agent responsible for processing HSA distributions."""
    
    def __init__(self):
        super().__init__("DistributionAgent")
    
    def process(self, state: HSAState) -> HSAState:
        """Process HSA distribution request."""
        # Simple implementation for now
        state = self._update_state_metadata(state)
        state["current_step"] = "distribution_processing"
        
        message = "Distribution processing completed"
        state = self._add_message(state, message)
        
        return state