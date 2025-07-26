# This file initializes the agents package.

from abc import ABC, abstractmethod
from datetime import datetime
from ..graph.hsa_state import HSAState

class BaseHSAAgent(ABC):
    """Base class for all HSA agents."""
    
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
    
    @abstractmethod
    def process(self, state: HSAState) -> HSAState:
        """Process the HSA state and return updated state."""
        pass
    
    def _update_state_metadata(self, state: HSAState) -> HSAState:
        """Update common state metadata."""
        processed_by = state.get("processed_by", [])
        processed_by.append(self.agent_name)
        
        state["processed_by"] = processed_by
        state["timestamp"] = datetime.now()
        
        return state
    
    def _add_message(self, state: HSAState, message: str, message_type: str = "info") -> HSAState:
        """Add a message to the state for agent communication."""
        message_data = {
            "agent": self.agent_name,
            "message": message,
            "type": message_type,
            "timestamp": datetime.now().isoformat()
        }
        
        messages = state.get("messages", [])
        messages.append(message_data)
        state["messages"] = messages
        
        return state