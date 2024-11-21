import unittest
from obfuscators.arithmetic_obfuscator import ArithmeticObfuscator

class TestArithmeticObfuscator(unittest.TestCase):
    def setUp(self):
        """
        Initialize the Arithmetic Obfuscator for testing
        """
        self.obfuscator = ArithmeticObfuscator()
        
    def test_arithmetic_complexity(self):
        """
        Test if arithmetic expressions are complexified with redundant operations
        """
        original_code = """
        pragma solidity ^0.8.0;

        contract Example {
            function calculate(uint256 a, uint256 b) public pure returns (uint256) {
                return a + b;
            }
        }
        """
        obfuscated_code = self.obfuscator.obfuscate(original_code)
        
        # Check that redundant operations are added
        self.assertIn("((a + b) + 0 - 0)", obfuscated_code)
        
    def test_no_change_to_other_code(self):
        """
        Ensure non-arithmetic code remains unchanged
        """
        original_code = """
        pragma solidity ^0.8.0;

        contract Example {
            function getNumber() public pure returns (uint256) {
                return 42;
            }
        }
        """
        obfuscated_code = self.obfuscator.obfuscate(original_code)
        
        # Ensure that non-arithmetic parts of the code remain untouched
        self.assertIn("return 42;", obfuscated_code)
        
    def test_complex_arithmetic(self):
        """
        Ensure the obfuscator handles complex arithmetic correctly
        """
        original_code = """
        pragma solidity ^0.8.0;

        contract Example {
            function calculateComplex(uint256 a, uint256 b, uint256 c) public pure returns (uint256) {
                return a * b + c - 5;
            }
        }
        """
        obfuscated_code = self.obfuscator.obfuscate(original_code)
        
        # Check that multiple arithmetic expressions are obfuscated
        self.assertIn("((a * b) + 0 - 0)", obfuscated_code)
        self.assertIn("((c - 5) + 0 - 0)", obfuscated_code)
        
if __name__ == "__main__":
    unittest.main()