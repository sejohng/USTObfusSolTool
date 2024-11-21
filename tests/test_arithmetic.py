import unittest
from obfuscators.arithmetic_obfuscator import ArithmeticObfuscator

class TestArithmeticObfuscator(unittest.TestCase):
    """
    Unit tests for ArithmeticObfuscator.
    """

    def setUp(self):
        self.obfuscator = ArithmeticObfuscator()
        self.solidity_code = """
        pragma solidity ^0.8.0;

        contract Example {
            function calculate(uint256 a, uint256 b) public pure returns (uint256) {
                return a + b;
            }
        }
        """

    def test_arithmetic_complexity(self):
        """
        Test if arithmetic expressions are complexified.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("+ 0 - 0", obfuscated_code)  # Check for redundant arithmetic logic

if __name__ == "__main__":
    unittest.main()