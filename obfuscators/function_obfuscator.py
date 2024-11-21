import re
import random

class FunctionObfuscator:
    """
    Function Inlining and Splitting Obfuscator
    """

    def inline_functions(self, code):
        """
        Inline simple functions at their call points
        :param code: Input code
        :return: Code with functions inlined
        """
        # Match functions with no parameters and simple return statements
        pattern = r'function\s+(\w+)\s*\(\)\s+public\s+returns\s*\((\w+)\)\s*\{\s*return\s*(.+?);\s*\}'
        matches = re.findall(pattern, code)

        for match in matches:
            func_name, return_type, return_value = match
            # Replace function calls with the inlined return value
            call_pattern = r'\b' + func_name + r'\(\)'
            code = re.sub(call_pattern, f"({return_value})", code)

            # Remove the original function definition
            func_pattern = r'function\s+' + func_name + r'\s*\(.*?\)\s*\{.*?\}'
            code = re.sub(func_pattern, "", code, flags=re.DOTALL)

        return code

    def split_function(self, code):
        """
        Split complex functions into sub-functions
        :param code: Input code
        :return: Code with functions split into sub-functions
        """
        # Match non-simple functions
        pattern = r'(function\s+\w+\s*\(.*?\)\s*{)(.+?)(return\s+.+?;)(\s*})'
        matches = re.findall(pattern, code, flags=re.DOTALL)

        for match in matches:
            func_header, body, return_statement, func_footer = match
            sub_func_name = f"subFunc_{random.randint(1000, 9999)}"
            sub_func_code = f"{func_header}\n    return {sub_func_name}();\n{func_footer}\n\nfunction {sub_func_name}() private {body.strip()} {return_statement} }}"

            # Replace the original function with the modified version
            code = code.replace("".join(match), sub_func_code)

        return code

    def obfuscate(self, code):
        """
        Apply function obfuscation
        :param code: Input code
        :return: Obfuscated code
        """
        code = self.inline_functions(code)
        code = self.split_function(code)
        return code