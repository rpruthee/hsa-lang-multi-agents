import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

try:
    from src.graph.hsa_state import HSAState
    print("✅ HSAState imported successfully")
except Exception as e:
    print(f"❌ HSAState import failed: {e}")

try:
    from src.agents.base_agent import BaseHSAAgent
    print("✅ BaseHSAAgent imported successfully")
except Exception as e:
    print(f"❌ BaseHSAAgent import failed: {e}")

try:
    from src.agents.compliance_agent import ComplianceAgent
    print("✅ ComplianceAgent imported successfully")
except Exception as e:
    print(f"❌ ComplianceAgent import failed: {e}")