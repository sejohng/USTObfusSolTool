import unittest
from obfuscators.function_obfuscator import FunctionObfuscator

class TestFunctionObfuscator(unittest.TestCase):
    """
    Unit tests for FunctionObfuscator.
    """

    def setUp(self):
        self.obfuscator = FunctionObfuscator()
        self.solidity_code = """
        pragma solidity ^0.8.0;

        contract Example {
            function simpleFunction() public pure returns (uint256) {
                return 42;
            }

            function complexFunction(uint256 a) public pure returns (uint256) {
                return a * 2;
            }
        }
        """

    def test_function_inlining(self):
        """
        Test if simple functions are inlined.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertNotIn("function simpleFunction", obfuscated_code)  # Check if inlined

    def test_function_splitting(self):
        """
        Test if complex functions are split into sub-functions.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("subFunc_", obfuscated_code)  # Check for sub-function

if __name__ == "__main__":
    unittest.main()