# test_utils.py

import unittest
from src.utils.irs_rules import is_eligible_for_hsa, get_contribution_limits
from src.utils.validation import validate_contribution

class TestUtils(unittest.TestCase):
    """Unit tests for utility functions."""

    def test_is_eligible_for_hsa(self):
        """Test eligibility determination based on IRS rules."""
        self.assertTrue(is_eligible_for_hsa(30, 'individual'))
        self.assertFalse(is_eligible_for_hsa(25, 'individual'))
        self.assertTrue(is_eligible_for_hsa(40, 'family'))
        self.assertFalse(is_eligible_for_hsa(35, 'family'))

    def test_get_contribution_limits(self):
        """Test retrieval of contribution limits based on filing status."""
        self.assertEqual(get_contribution_limits('individual'), 3600)
        self.assertEqual(get_contribution_limits('family'), 7200)

    def test_validate_contribution(self):
        """Test validation of contributions against IRS limits."""
        self.assertTrue(validate_contribution(3500, 'individual'))
        self.assertFalse(validate_contribution(4000, 'individual'))
        self.assertTrue(validate_contribution(7000, 'family'))
        self.assertFalse(validate_contribution(8000, 'family'))

if __name__ == '__main__':
    unittest.main()