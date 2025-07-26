# tests/test_workflow.py

import unittest
from src.graph.hsa_workflow import HSAWorkflow
from src.agents.eligibility_agent import EligibilityAgent
from src.agents.contribution_agent import ContributionAgent
from src.agents.distribution_agent import DistributionAgent
from src.agents.compliance_agent import ComplianceAgent

class TestHSAWorkflow(unittest.TestCase):
    def setUp(self):
        # Initialize agents for testing
        self.eligibility_agent = EligibilityAgent()
        self.contribution_agent = ContributionAgent()
        self.distribution_agent = DistributionAgent()
        self.compliance_agent = ComplianceAgent()
        self.workflow = HSAWorkflow(
            self.eligibility_agent,
            self.contribution_agent,
            self.distribution_agent,
            self.compliance_agent
        )

    def test_eligibility_check(self):
        # Test eligibility determination
        result = self.workflow.check_eligibility({"age": 30, "coverage": "self"})
        self.assertTrue(result)

    def test_contribution_management(self):
        # Test contribution handling
        contribution_result = self.workflow.manage_contribution(5000)
        self.assertTrue(contribution_result)

    def test_distribution_handling(self):
        # Test distribution for qualified expenses
        distribution_result = self.workflow.handle_distribution(2000, "qualified medical expense")
        self.assertTrue(distribution_result)

    def test_compliance_check(self):
        # Test compliance verification
        compliance_result = self.workflow.verify_compliance()
        self.assertTrue(compliance_result)

    def tearDown(self):
        # Clean up after tests
        del self.workflow
        del self.eligibility_agent
        del self.contribution_agent
        del self.distribution_agent
        del self.compliance_agent

if __name__ == '__main__':
    unittest.main()