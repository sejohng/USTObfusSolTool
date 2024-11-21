import unittest
from obfuscators.string_obfuscator import StringObfuscator

class TestStringObfuscator(unittest.TestCase):
    """
    Unit tests for StringObfuscator.
    """

    def setUp(self):
        self.obfuscator = StringObfuscator()
        self.solidity_code = """
        pragma solidity ^0.8.0;

        contract Example {
            function getString() public pure returns (string memory) {
                return "HelloWorld";
            }
        }
        """

    def test_string_encoding(self):
        """
        Test if strings are encoded correctly.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertNotIn('"HelloWorld"', obfuscated_code)  # Original string should not exist
        self.assertIn("abi.encodePacked", obfuscated_code)  # Check for encoded string

if __name__ == "__main__":
    unittest.main()