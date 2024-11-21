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
        self.assertIn("uint256", obfuscated_code)

    def test_function_renaming(self):
        """
        Test that function names are obfuscated correctly.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertNotIn("myFunction", obfuscated_code)
        self.assertIn("function", obfuscated_code)

    def test_output_structure(self):
        """
        Test that the overall structure of the contract remains intact.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("pragma solidity ^0.8.0;", obfuscated_code)
        self.assertIn("contract Example", obfuscated_code)

    def test_insert_fake_code(self):
        """
        Test that fake code is inserted correctly.
        """
        obfuscated_code = self.obfuscator.insert_fake_code(self.solidity_code, num_fake_items=2)
        self.assertGreaterEqual(obfuscated_code.count("function fakeFunction"), 1)
        self.assertGreaterEqual(obfuscated_code.count("// Fake comment"), 1)

    def test_shuffle_preserves_contract(self):
        """
        Test that shuffling preserves the contract structure.
        """
        obfuscated_code = self.obfuscator.shuffle_code_blocks(self.solidity_code)
        self.assertIn("pragma solidity ^0.8.0;", obfuscated_code)
        self.assertIn("contract Example", obfuscated_code)


if __name__ == "__main__":
    unittest.main()