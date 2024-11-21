import unittest
from obfuscators.deadcode_obfuscator import DeadCodeObfuscator

class TestDeadCodeObfuscator(unittest.TestCase):
    """
    Unit tests for DeadCodeObfuscator.
    """

    def setUp(self):
        self.obfuscator = DeadCodeObfuscator()
        self.solidity_code = """
        pragma solidity ^0.8.0;

        contract Example {
            function testFunction(uint256 input) public returns (uint256) {
                return input * 2;
            }
        }
        """

    def test_dead_code_insertion(self):
        """
        Test if dead code is inserted into functions.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("uint256 uselessVar = 0;", obfuscated_code)  # Check for dead code

if __name__ == "__main__":
    unittest.main()