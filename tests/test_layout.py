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
        # Original variable name should not exist
        self.assertNotIn("myVariable", obfuscated_code)
        # Ensure type declaration remains intact
        self.assertIn("uint256", obfuscated_code)

    def test_function_renaming(self):
        """
        Test that function names are obfuscated correctly.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        # Original function name should not exist
        self.assertNotIn("myFunction", obfuscated_code)
        # Ensure function keyword remains intact
        self.assertIn("function", obfuscated_code)

    def test_output_structure(self):
        """
        Test that the overall structure of the contract remains intact.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        # Pragma statement should remain
        self.assertIn("pragma solidity ^0.8.0;", obfuscated_code)
        # Contract declaration should remain
        self.assertIn("contract Example", obfuscated_code)

    def test_insert_fake_code(self):
        """
        Test that fake code is inserted correctly.
        """
        obfuscated_code = self.obfuscator.insert_fake_code(self.solidity_code, num_fake_items=3)
        # Ensure fake functions and comments are inserted
        self.assertGreaterEqual(obfuscated_code.count("function fakeFunction"), 1)
        self.assertGreaterEqual(obfuscated_code.count("// Fake comment"), 1)

    def test_shuffle_preserves_contract(self):
        """
        Test that shuffling preserves the contract structure.
        """
        obfuscated_code = self.obfuscator.shuffle_code_blocks(self.solidity_code)
        # Pragma statement and contract declaration should remain
        self.assertIn("pragma solidity ^0.8.0;", obfuscated_code)
        self.assertIn("contract Example", obfuscated_code)

    def test_minify_code(self):
        """
        Test that minification removes unnecessary spaces and line breaks.
        """
        minified_code = self.obfuscator.minify_code(self.solidity_code)
        # Ensure no extra spaces or line breaks
        self.assertNotIn("\n", minified_code)
        self.assertNotIn("  ", minified_code)
        # Ensure critical keywords remain
        self.assertIn("pragma solidity ^0.8.0;", minified_code)
        self.assertIn("contract Example", minified_code)

    def test_full_obfuscation(self):
        """
        Test the full obfuscation process.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        # Ensure variable and function names are obfuscated
        self.assertNotIn("myVariable", obfuscated_code)
        self.assertNotIn("myFunction", obfuscated_code)
        # Ensure minification is applied
        self.assertNotIn("\n", obfuscated_code)
        self.assertNotIn("  ", obfuscated_code)
        # Ensure critical structure remains
        self.assertIn("pragma solidity ^0.8.0;", obfuscated_code)
        self.assertIn("contract Example", obfuscated_code)


if __name__ == "__main__":
    unittest.main()