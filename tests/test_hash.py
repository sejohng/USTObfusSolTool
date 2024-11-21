import unittest
from obfuscators.hash_obfuscator import HashObfuscator

class TestHashObfuscator(unittest.TestCase):
    """
    Unit tests for HashObfuscator.
    """

    def setUp(self):
        self.obfuscator = HashObfuscator()
        self.solidity_code = """
        pragma solidity ^0.8.0;

        contract ExampleContract {
            uint256 public myVariable;
            address private owner;

            function setVariable(uint256 value) public {
                myVariable = value;
            }

            function getOwner() public view returns (address) {
                return owner;
            }
        }
        """

    def test_variable_hashing(self):
        """
        Test that variables are renamed using hashes.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertNotIn("myVariable", obfuscated_code)
        self.assertNotIn("owner", obfuscated_code)
        self.assertIn("0x", obfuscated_code)

    def test_function_hashing(self):
        """
        Test that functions are renamed using hashes.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertNotIn("setVariable", obfuscated_code)
        self.assertNotIn("getOwner", obfuscated_code)
        self.assertIn("function 0x", obfuscated_code)

    def test_overall_structure(self):
        """
        Test that the structure of the contract remains intact.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("pragma solidity ^0.8.0;", obfuscated_code)
        self.assertIn("contract ExampleContract", obfuscated_code)

if __name__ == "__main__":
    unittest.main()