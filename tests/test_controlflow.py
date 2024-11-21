import unittest
from obfuscators.controlflow_obfuscator import ControlflowObfuscator

class TestControlflowObfuscator(unittest.TestCase):
    """
    Unit tests for ControlflowObfuscator.
    """

    def setUp(self):
        self.obfuscator = ControlflowObfuscator()
        self.solidity_code = """
        pragma solidity ^0.8.0;

        contract Example {
            function testFunction(uint256 input) public returns (uint256) {
                if (input > 10) {
                    return input * 2;
                }
                return input;
            }
        }
        """

    def test_fake_conditions(self):
        """
        Test if fake conditions are added.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("if (1 == 0)", obfuscated_code)  # Check for fake condition

    def test_complexify_conditionals(self):
        """
        Test if conditionals are complexified.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("&& (1 == 1)", obfuscated_code)  # Check for complex logic

    def test_fake_loops(self):
        """
        Test if fake loops are inserted.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("for (uint256 i = 0; i < 1; i++)", obfuscated_code)  # Check for fake loop

if __name__ == "__main__":
    unittest.main()