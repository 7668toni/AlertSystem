# test_alertsystem.py
"""
Tests for AlertSystem module.
"""

import unittest
from alertsystem import AlertSystem

class TestAlertSystem(unittest.TestCase):
    """Test cases for AlertSystem class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AlertSystem()
        self.assertIsInstance(instance, AlertSystem)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AlertSystem()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
