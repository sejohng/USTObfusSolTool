import re
import random

from utils.helper import generate_random_name


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
            value = int(match. group())
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
        pattern = r'\b(?!.*constant.*)(?P<prefix>(?P<var_type>bool|u?int(8|16|32|64|128|256)?|u?fixed|address|string|byte(s[0-9]*)?|enum)\s+(([a-zA-Z_][a-zA-Z0-9_]*)\s+)*)(?P<var_name>[a-zA-Z_][a-zA-Z0-9_]*)\b\s*=\s*(?P<var_val>.+?);'
        matches = re.finditer(pattern, code)

        def replace_assignment(match):
            var_value = match.group('var_val')
            var_name = match.group('var_name')
            var_type = match.group('var_type')
            prefix = match.group('prefix')
            temp_var = generate_random_name()
            return f"{var_type} {temp_var} = {var_value};\n\t{prefix}{var_name} = {temp_var};"

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