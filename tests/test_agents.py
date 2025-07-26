import unittest
from src.agents.eligibility_agent import EligibilityAgent
from src.agents.contribution_agent import ContributionAgent
from src.agents.distribution_agent import DistributionAgent
from src.agents.compliance_agent import ComplianceAgent

class TestEligibilityAgent(unittest.TestCase):
    def setUp(self):
        self.agent = EligibilityAgent()

    def test_eligibility(self):
        # Test eligibility determination logic
        self.assertTrue(self.agent.is_eligible(30, 1000))  # Example parameters

class TestContributionAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ContributionAgent()

    def test_contribution_limit(self):
        # Test contribution limit compliance
        self.assertTrue(self.agent.is_within_limit(3000))  # Example parameter

class TestDistributionAgent(unittest.TestCase):
    def setUp(self):
        self.agent = DistributionAgent()

    def test_qualified_expense(self):
        # Test if the expense is qualified
        self.assertTrue(self.agent.is_qualified_expense(200))  # Example parameter

class TestComplianceAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ComplianceAgent()

    def test_compliance_check(self):
        # Test compliance checking logic
        self.assertTrue(self.agent.check_compliance())  # Example method

if __name__ == '__main__':
    unittest.main()