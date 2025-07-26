from typing import Dict, Any
from langgraph.graph import StateGraph, END

# Use absolute imports instead of relative imports
from src.agents.eligibility_agent import EligibilityAgent
from src.agents.contribution_agent import ContributionAgent
from src.agents.distribution_agent import DistributionAgent
from src.agents.compliance_agent import ComplianceAgent
from src.graph.hsa_state import HSAState

class HSAWorkflow:
    """Main workflow orchestrator for HSA management using LangGraph."""
    
    def __init__(self):
        self.eligibility_agent = EligibilityAgent()
        self.contribution_agent = ContributionAgent()
        self.distribution_agent = DistributionAgent()
        self.compliance_agent = ComplianceAgent()
        
        # Create the state graph
        self.workflow = StateGraph(HSAState)
        self._setup_workflow()
    
    def _setup_workflow(self):
        """Set up the LangGraph workflow with nodes and edges."""
        
        # Add nodes (agents) to the workflow
        self.workflow.add_node("eligibility", self.eligibility_agent.process)
        self.workflow.add_node("contribution", self.contribution_agent.process)
        self.workflow.add_node("compliance", self.compliance_agent.process)
        
        # Set entry point
        self.workflow.set_entry_point("eligibility")
        
        # Add conditional edges
        self.workflow.add_conditional_edges(
            "eligibility",
            self._route_after_eligibility,
            {
                "contribution": "contribution",
                "end": END
            }
        )
        
        self.workflow.add_edge("contribution", "compliance")
        self.workflow.add_edge("compliance", END)
    
    def _route_after_eligibility(self, state: HSAState) -> str:
        """Route to appropriate agent after eligibility check."""
        if not state.get("is_eligible", False):
            return "end"
        
        user_data = state.get("user_data", {})
        request_type = user_data.get("request_type", "")
        
        if request_type == "contribution":
            return "contribution"
        else:
            return "end"
    
    def compile(self):
        """Compile the workflow for execution."""
        return self.workflow.compile()