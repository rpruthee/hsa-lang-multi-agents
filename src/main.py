# main.py

# This file serves as the entry point for the HSA multi-agent system application.

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from typing import Dict, Any
from src.graph.hsa_workflow import HSAWorkflow
from src.graph.hsa_state import HSAState

def main():
    """Main entry point for the HSA Multi-Agent System."""
    
    # Initialize the workflow
    workflow = HSAWorkflow()
    app = workflow.compile()
    
    # Sample user data for testing
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
    
    # Initialize state
    initial_state: HSAState = {
        "messages": [],
        "agent_messages": [],  # Add this field for detailed messages
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
    
    # Execute the workflow
    print("Starting HSA Multi-Agent Workflow...")
    result = app.invoke(initial_state)
    
    # Print results
    print("\nWorkflow Results:")
    print(f"Status: {result['workflow_status']}")
    print(f"Eligibility: {result['is_eligible']}")
    print(f"Reason: {result['eligibility_reason']}")
    print(f"Processed by: {result.get('processed_by', [])}")
    
    # Debug: Check what's actually in messages
    print(f"\nDebug - Messages type: {type(result.get('messages', []))}")
    print(f"Debug - Number of messages: {len(result.get('messages', []))}")
    
    # Print messages safely
    if result.get("messages"):
        print("\nAgent Messages:")
        for i, msg in enumerate(result["messages"]):
            print(f"Message {i}: {msg}")
            
            # Handle different message formats
            if isinstance(msg, dict):
                if 'content' in msg:
                    # LangGraph format
                    print(f"  Content: {msg['content']}")
                elif 'message' in msg and 'agent' in msg:
                    # Old format
                    print(f"  [{msg['agent']}] {msg['message']}")
                else:
                    # Unknown format
                    print(f"  Unknown format: {msg}")
            else:
                print(f"  Non-dict message: {msg}")
    
    # Print detailed agent messages if available
    if result.get("agent_messages"):
        print("\nDetailed Agent Messages:")
        for msg in result["agent_messages"]:
            if isinstance(msg, dict) and all(key in msg for key in ['agent', 'message', 'type', 'timestamp']):
                print(f"[{msg['agent']}] [{msg['type']}] {msg['message']} ({msg['timestamp']})")
            else:
                print(f"Unexpected agent message format: {msg}")
    
    # Print any errors or warnings
    if result.get("errors"):
        print("\nErrors:")
        for error in result["errors"]:
            print(f"❌ {error}")
    
    if result.get("warnings"):
        print("\nWarnings:")
        for warning in result["warnings"]:
            print(f"⚠️ {warning}")

if __name__ == "__main__":
    main()