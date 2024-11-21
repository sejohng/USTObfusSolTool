import re
import random

class DataflowObfuscator:
    """
    Data Flow Obfuscator
    """

    def __init__(self):
        """
        Initialize the obfuscator
        """
        self.temp_variable_counter = 0

    def generate_temp_variable(self):
        """
        Generate a temporary variable name
        :return: Temporary variable name
        """
        self.temp_variable_counter += 1
        return f"tempVar_{self.temp_variable_counter}"

    def split_constants(self, code):
        """
        Split constants into expressions, e.g., replace 100 with 50 + 50
        :param code: Input code
        :return: Code with constants split into expressions
        """
        def replace_constant(match):
            value = int(match.group())
            if value > 10:  # Avoid overly complex splitting for small values
                part1 = random.randint(1, value - 1)
                part2 = value - part1
                return f"({part1} + {part2})"
            return str(value)

        pattern = r'\b\d+\b'
        return re.sub(pattern, replace_constant, code)

    def insert_temp_variables(self, code):
        """
        Replace direct assignments with temporary variables
        :param code: Input code
        :return: Code with temporary variables inserted
        """
        pattern = r'(\b[a-zA-Z_][a-zA-Z0-9_]*\b)\s*=\s*(.+?);'

        def replace_assignment(match):
            variable = match.group(1)
            value = match.group(2)
            temp_var = self.generate_temp_variable()
            return f"uint256 {temp_var} = {value};\n    {variable} = {temp_var};"

        return re.sub(pattern, replace_assignment, code)

    def obfuscate(self, code):
        """
        Apply data flow obfuscation
        :param code: Input code
        :return: Obfuscated code
        """
        # 1. Split constants into expressions
        code = self.split_constants(code)
        # 2. Insert temporary variables
        code = self.insert_temp_variables(code)

        return code