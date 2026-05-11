# test_neurforge.py
"""
Tests for NeurForge module.
"""

import unittest
from neurforge import NeurForge

class TestNeurForge(unittest.TestCase):
    """Test cases for NeurForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeurForge()
        self.assertIsInstance(instance, NeurForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeurForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
