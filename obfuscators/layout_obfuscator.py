import re
import random
import string

from utils.helper import generate_random_name


class LayoutObfuscator:
    """
    Layout Obfuscator
    """

    def __init__(self):
        """
        Initialize the obfuscator
        """
        self.variable_map = {}
        self.function_map = {}

    def obfuscate_variables(self, code):
        """
        Obfuscate variable names
        :param code: Input code
        :return: Code with obfuscated variable names
        """
        pattern = r'\b(bool|u?int(8|16|32|64|128|256)?|u?fixed|address|string|byte(s[0-9]*)?|enum)\s+(([a-zA-Z_][a-zA-Z0-9_]*)\s+)*(?P<var_name>[a-zA-Z_][a-zA-Z0-9_]*)'
        matches = re.finditer(pattern, code)

        for match in matches:
            var_name = match.group('var_name')
            if var_name not in self.variable_map:
                self.variable_map[var_name] = generate_random_name()
                code = re.sub(rf'(?P<stay>"[^"]*")|(?<!msg\.)\b{var_name}\b', lambda x: x.group('stay') if x.group('stay') else self.variable_map[var_name], code)

        return code

    def obfuscate_functions(self, code):
        """
        Obfuscate names of functions, modifiers, contracts, structs, and events
        :param code: Input code
        :return: Code with obfuscated function names
        """
        pattern = r'(function|modifier|contract|event|struct)\s+(?P<func_name>[a-zA-Z0-9_]*)\s*(\(|\{)'
        matches = re.finditer(pattern, code)

        for match in matches:
            func_name = match.group('func_name')
            if func_name not in self.function_map:
                self.function_map[func_name] = generate_random_name()
                code = re.sub(rf'(?P<stay>"[^"]*")|\b{func_name}\b', lambda x: x.group('stay') if x.group('stay') else self.function_map[func_name], code)

        return code

    def obfuscate(self, code):
        """
        Apply layout obfuscation
        :param code: Input code
        :return: Obfuscated code
        """
        # Obfuscate variable names
        code = self.obfuscate_variables(code)
        # Obfuscate function names
        code = self.obfuscate_functions(code)

        return code