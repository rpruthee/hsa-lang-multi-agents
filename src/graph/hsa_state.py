# src/graph/hsa_state.py

from typing import TypedDict, Optional, Dict, Any, List
from datetime import datetime

class HSAState(TypedDict):
    """State definition for HSA workflow using LangGraph."""
    
    # LangGraph compatible messages
    messages: List[Dict[str, str]]
    
    # Custom agent messages (optional)
    agent_messages: Optional[List[Dict[str, Any]]]
    
    # User input data
    user_data: Dict[str, Any]
    
    # Eligibility results
    is_eligible: Optional[bool]
    eligibility_reason: Optional[str]
    
    # Contribution processing results
    contribution_amount: Optional[float]
    contribution_limit: Optional[float]
    contribution_valid: Optional[bool]
    contribution_errors: Optional[List[str]]
    
    # Distribution processing results
    distribution_amount: Optional[float]
    distribution_reason: Optional[str]
    distribution_valid: Optional[bool]
    distribution_tax_implications: Optional[Dict[str, Any]]
    
    # Compliance results
    compliance_check_result: Optional[str]
    compliance_violations: Optional[List[str]]
    compliance_warnings: Optional[List[str]]
    
    # Workflow metadata
    current_step: Optional[str]
    next_step: Optional[str]
    workflow_status: str
    errors: Optional[List[str]]
    warnings: Optional[List[str]]
    timestamp: Optional[datetime]
    processed_by: List[str]