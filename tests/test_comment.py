import unittest
from obfuscators.comment_obfuscator import CommentObfuscator

class TestCommentObfuscator(unittest.TestCase):
    """
    Unit tests for CommentObfuscator.
    """

    def setUp(self):
        self.obfuscator = CommentObfuscator()
        self.solidity_code = """
        pragma solidity ^0.8.0;

        // This is a test comment
        contract Example {
            function testFunction() public {
                // Another comment
            }
        }
        """

    def test_comment_removal(self):
        """
        Test if existing comments are removed.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertNotIn("// This is a test comment", obfuscated_code)  # Original comment should not exist

    def test_fake_comment_insertion(self):
        """
        Test if fake comments are inserted.
        """
        obfuscated_code = self.obfuscator.obfuscate(self.solidity_code)
        self.assertIn("// TODO:", obfuscated_code)  # Check for fake comment

if __name__ == "__main__":
    unittest.main()