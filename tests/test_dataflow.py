#Usage: cd /Project/USTObfusSol
# python3 -m unittest tests/test_dataflow.py

import unittest
from obfuscators.dataflow_obfuscator import DataflowObfuscator

class TestDataflowObfuscator(unittest.TestCase):
    """
    Unit tests for DataflowObfuscator.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.obfuscator = DataflowObfuscator()
        self.solidity_code = """
        pragma solidity ^0.8.0;

        contract Example {
            uint256 public myVariable;

            function updateVariable(uint256 newValue) public {
                myVariable = newValue;
                uint256 constantValue = 100;
            }
        }
        """

    def test_constant_split(self):
        """
        Test that constants are split correctly.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertNotIn("100;", obfuscated_code)
        self.assertIn("+", obfuscated_code)  # Ensure constant is split into parts

    def test_temporary_variables(self):
        """
        Test that temporary variables are inserted correctly.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("tempVar", obfuscated_code)  # Ensure temporary variables are present
        self.assertIn("myVariable =", obfuscated_code)  # Ensure original assignment still exists

    def test_output_structure(self):
        """
        Test that the overall structure of the contract remains intact.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("contract Example", obfuscated_code)  # Contract name should remain
        self.assertIn("pragma solidity ^0.8.0;", obfuscated_code)  # Pragma statement should remain

if __name__ == "__main__":
    unittest.main()