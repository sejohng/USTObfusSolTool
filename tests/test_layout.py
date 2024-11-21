import unittest
from obfuscators.layout_obfuscator import LayoutObfuscator

class TestLayoutObfuscator(unittest.TestCase):
    """
    Unit tests for LayoutObfuscator.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.obfuscator = LayoutObfuscator()
        self.solidity_code = """
        pragma solidity ^0.8.0;

        contract Example {
            uint256 public myVariable;

            event MyEvent(address indexed from, uint256 value);

            function myFunction(uint256 input) public returns (uint256) {
                return input * 2;
            }
        }
        """

    def test_variable_renaming(self):
        """
        Test that variable names are obfuscated correctly.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertNotIn("myVariable", obfuscated_code)
        self.assertIn("uint256", obfuscated_code)  # Ensure variable type remains unchanged

    def test_function_renaming(self):
        """
        Test that function names are obfuscated correctly.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertNotIn("myFunction", obfuscated_code)
        self.assertIn("function", obfuscated_code)  # Ensure function keyword remains unchanged

    def test_output_structure(self):
        """
        Test that the overall structure of the contract remains intact.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("contract Example", obfuscated_code)  # Contract name should remain the same
        self.assertIn("pragma solidity ^0.8.0;", obfuscated_code)  # Pragma statement should remain

if __name__ == "__main__":
    unittest.main()