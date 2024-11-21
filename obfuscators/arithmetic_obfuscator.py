import re
import random

class ArithmeticObfuscator:
    """
    Arithmetic Obfuscator
    """

    def obfuscate_arithmetic(self, code):
        """
        Obfuscate arithmetic expressions
        :param code: Input code
        :return: Code with obfuscated arithmetic expressions
        """
        pattern = r'(\b\d+\s*[\+\-\*/]\s*\d+\b)'  # Match simple arithmetic operations

        def replace_arithmetic(match):
            expression = match.group(1)
            components = expression.split()
            if len(components) == 3:
                a, operator, b = components
                return f"(({a} {operator} {b}) + 0 - 0)"
            return expression

        return re.sub(pattern, replace_arithmetic, code)

    def obfuscate(self, code):
        """
        Apply arithmetic obfuscation
        :param code: Input code
        :return: Code with applied obfuscation
        """
        return self.obfuscate_arithmetic(code)