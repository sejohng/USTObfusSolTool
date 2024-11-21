import hashlib
import re

class HashObfuscator:
    """
    Obfuscator for generating hashed names for variables and functions.
    """

    def __init__(self):
        pass

    @staticmethod
    def generate_hashed_name(original_name):
        """
        Generate an obfuscated name by hashing the original name.
        :param original_name: The original variable or function name.
        :return: A hashed name with a '0x' prefix.
        """
        hashed = hashlib.sha256(original_name.encode()).hexdigest()[:10]
        return f"0x{hashed}"

    def obfuscate_variables(self, code):
        """
        Obfuscate variable names using hashing.
        :param code: Input Solidity code.
        :return: Code with hashed variable names.
        """
        pattern = r"(uint256|address|bool|mapping|int256|bytes\d*|string)\s+(\w+)"
        matches = re.findall(pattern, code)

        for var_type, var_name in matches:
            hashed_name = self.generate_hashed_name(var_name)
            code = re.sub(rf"\b{var_name}\b", hashed_name, code)

        return code

    def obfuscate_functions(self, code):
        """
        Obfuscate function names using hashing.
        :param code: Input Solidity code.
        :return: Code with hashed function names.
        """
        pattern = r"function\s+(\w+)\s*\("
        matches = re.findall(pattern, code)

        for func_name in matches:
            hashed_name = self.generate_hashed_name(func_name)
            code = re.sub(rf"\b{func_name}\b", hashed_name, code)

        return code

    def obfuscate(self, code):
        """
        Apply the hashing obfuscation to both variables and functions.
        :param code: Input Solidity code.
        :return: Fully obfuscated code.
        """
        code = self.obfuscate_variables(code)
        code = self.obfuscate_functions(code)
        return code