# test_shardiris.py
"""
Tests for ShardIris module.
"""

import unittest
from shardiris import ShardIris

class TestShardIris(unittest.TestCase):
    """Test cases for ShardIris class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShardIris()
        self.assertIsInstance(instance, ShardIris)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShardIris()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
