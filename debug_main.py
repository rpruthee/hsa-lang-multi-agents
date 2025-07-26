import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.graph.hsa_workflow import HSAWorkflow
from src.graph.hsa_state import HSAState

def debug_main():
    """Debug version to identify message format issues."""
    
    workflow = HSAWorkflow()
    app = workflow.compile()
    
    sample_user_data = {
        "user_id": "user123",
        "request_type": "contribution",
        "has_hdhp": True,
        "has_other_health_coverage": False,
        "enrolled_in_medicare": False,
        "claimed_as_dependent": False,
        "age": 35,
        "contribution_amount": 3000.0,
        "year": 2024
    }
    
    initial_state: HSAState = {
        "messages": [],
        "agent_messages": [],
        "user_data": sample_user_data,
        "is_eligible": None,
        "eligibility_reason": None,
        "contribution_amount": None,
        "contribution_limit": None,
        "contribution_valid": None,
        "contribution_errors": None,
        "distribution_amount": None,
        "distribution_reason": None,
        "distribution_valid": None,
        "distribution_tax_implications": None,
        "compliance_check_result": None,
        "compliance_violations": None,
        "compliance_warnings": None,
        "current_step": None,
        "next_step": None,
        "workflow_status": "pending",
        "errors": None,
        "warnings": None,
        "timestamp": None,
        "processed_by": []
    }
    
    print("Starting workflow...")
    result = app.invoke(initial_state)
    
    print(f"\nResult type: {type(result)}")
    print(f"Result keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}")
    
    if 'messages' in result:
        print(f"\nMessages type: {type(result['messages'])}")
        print(f"Number of messages: {len(result['messages'])}")
        
        for i, msg in enumerate(result['messages']):
            print(f"\nMessage {i}:")
            print(f"  Type: {type(msg)}")
            print(f"  Content: {msg}")
            if isinstance(msg, dict):
                print(f"  Keys: {list(msg.keys())}")

if __name__ == "__main__":
    debug_main()