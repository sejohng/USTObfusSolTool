import unittest
from obfuscators.dataflow_obfuscator import DataflowObfuscator

class TestDeadCodeObfuscator(unittest.TestCase):
    def setUp(self):
        """
        Initialize the DataflowObfuscator for testing
        """
        self.obfuscator = DataflowObfuscator()

    def test_split_constants(self):
        """
        Test splitting constants into expressions
        """
        original_code = """
        uint256 value = 100;
        uint256 anotherValue = 50;
        """
        obfuscated_code = self.obfuscator.split_constants(original_code)
        
        # Assert that constants are split into expressions
        self.assertRegex(obfuscated_code, r'\b\d+\s*\+\s*\d+\b')  # Check for addition expression
        self.assertNotIn("100;", obfuscated_code)  # Ensure original constants are not present
        self.assertNotIn("50;", obfuscated_code)

    def test_insert_temp_variables(self):
        """
        Test inserting temporary variables in assignments
        """
        original_code = """
        uint256 result = 10 * 2;
        uint256 anotherResult = 5 + 5;
        """
        obfuscated_code = self.obfuscator.insert_temp_variables(original_code)
        
        # Assert that temporary variables are inserted correctly
        self.assertIn("uint256 tempVar_1 =", obfuscated_code)  # Check for tempVar
        self.assertIn("result = tempVar_1;", obfuscated_code)
        self.assertIn("uint256 tempVar_2 =", obfuscated_code)
        self.assertIn("anotherResult = tempVar_2;", obfuscated_code)

    def test_full_obfuscation(self):
        """
        Test full obfuscation pipeline
        """
        original_code = """
        uint256 value = 100;
        uint256 result = value + 50;
        """
        obfuscated_code = self.obfuscator.obfuscate(original_code)
        
        # Assert that constants are split and temp variables are inserted
        self.assertRegex(obfuscated_code, r'\b\d+\s*\+\s*\d+\b')  # Check for split constants
        self.assertIn("uint256 tempVar_1 =", obfuscated_code)  # Check for tempVar insertion
        self.assertIn("value = tempVar_1;", obfuscated_code)

if __name__ == "__main__":
    unittest.main()