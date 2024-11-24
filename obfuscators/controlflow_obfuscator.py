import random
import re

from utils.helper import generate_random_name


class ControlflowObfuscator:
    """
    Control Flow Obfuscator
    """

    def __init__(self):
        """
        Initialize the obfuscator
        """
        self.always_true_conditions = [
            "((7 % 3) + 1 == 5)",
            "((6 * 2) - 1 == 11)",
            "((18 / 3) - 1 != 4)",
            "((7 * 3) % 20 == 1)",
        ]

    def complexify_conditions(self, code):
        """
        Complexify simple conditional logic
        :param code: Input code
        :return: Code with complexified conditions
        """
        pattern = r'\bif\s*\(([^{]*)\)\s*\{'

        def replace_condition(match):
            original_condition = match.group(1)
            if random.random() < 0.5:
                fake_logic = f"(({original_condition}) && {random.choice(self.always_true_conditions)})"
            else:
                fake_logic = f"(({original_condition}) || !{random.choice(self.always_true_conditions)})"
            return f"if ({fake_logic}) {{"

        return re.sub(pattern, replace_condition, code)

    def shuffle_code_blocks(self, code):
        """
        Shuffle the order of functions and contract members
        :param code: Input code
        :return: Code with shuffled blocks
        """
        pragma_match = re.search(r'\/\/ SPDX-License-Identifier:.*\n?pragma\s+solidity.*?;', code)
        contract_match = re.search(r'contract\s+\w+\s*\{', code)

        if not pragma_match or not contract_match:
            raise ValueError("Invalid Solidity contract structure.")

        pragma = pragma_match.group()
        contract_def = contract_match.group()

        # Extract the body of the contract
        body_start = contract_match.end()
        body_end = code.rfind("}")
        body_content = code[body_start:body_end].strip()

        # Split contract body into blocks and shuffle
        blocks = re.findall(r'(function[^{}]*{([^{}]*{[^{}]*})*[^{}]*}|mapping.*?;|event.*?;|modifier[^{}]*{([^{}]*{[^{}]*})*[^{}]*}|constructor[^{}]*{([^{}]*{[^{}]*})*[^{}]*}|struct[^{}]*{([^{}]*{[^{}]*})*[^{}]*}|((bool|u?int(8|16|32|64|128|256)?|u?fixed|address|string|byte(s[0-9]*)?|enum)\s+.*?;))', body_content, flags=re.DOTALL)
        print(blocks)
        random.shuffle(blocks)

        shuffled_body = ''
        for block in blocks:
            shuffled_body += block[0]
        return f"{pragma}{contract_def}{shuffled_body}}}"

    def minify_code(self, code):
        """
        Minify Solidity code by removing all unnecessary spaces and line breaks.
        :param code: Input code
        :return: Minified code
        """
        # Remove all line breaks and multiple spaces
        code = re.sub(r'(?<!\/\/ SPDX-License-Identifier: MIT)\s+', ' ', code)
        # Remove spaces around curly braces and semicolons
        code = re.sub(r'\s*{\s*', '{', code)
        code = re.sub(r'\s*}\s*', '}', code)
        code = re.sub(r'\s*;\s*', ';', code)
        return code.strip()

    def obfuscate(self, code):
        """
        Apply control flow obfuscation
        :param code: Input code
        :return: Obfuscated code
        """
        # Complexify simple conditionals
        code = self.complexify_conditions(code)
        # Minify the code
        code = self.minify_code(code)
        # Shuffle code block order
        code = self.shuffle_code_blocks(code)

        return code