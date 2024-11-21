import re
import random
import string


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
        self.fake_code_templates = [
            "function fakeFunction{}() public {{}}",
            "uint256 constant FAKE_VAR{} = {};",
            "// Fake comment {}"
        ]

    def generate_random_name(self, length=8):
        """
        Generate a random string
        :param length: Length of the string
        :return: Random name
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def obfuscate_variables(self, code):
        """
        Obfuscate variable names
        :param code: Input code
        :return: Code with obfuscated variable names
        """
        pattern = r'\b(uint256|address|bool|string)\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        matches = re.findall(pattern, code)

        for var_type, var_name in matches:
            if var_name not in self.variable_map:
                self.variable_map[var_name] = self.generate_random_name()
                code = re.sub(rf'\b{var_name}\b', self.variable_map[var_name], code)

        return code

    def obfuscate_functions(self, code):
        """
        Obfuscate function names
        :param code: Input code
        :return: Code with obfuscated function names
        """
        pattern = r'function\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        matches = re.findall(pattern, code)

        for func_name in matches:
            if func_name not in self.variable_map:
                self.variable_map[func_name] = self.generate_random_name()
                code = re.sub(rf'\b{func_name}\b', self.variable_map[func_name], code)

        return code

    def insert_fake_code(self, code, num_fake_items=3):
        """
        Insert fake code and comments
        :param code: Input code
        :param num_fake_items: Number of fake items to insert
        :return: Code with added fake code
        """
        fake_items = []
        for _ in range(num_fake_items):
            template = random.choice(self.fake_code_templates)
            fake_items.append(template.format(random.randint(0, 100)))

        return code.strip() + '\n\n' + '\n'.join(fake_items)

    def shuffle_code_blocks(self, code):
        """
        Shuffle the order of functions and contract members
        :param code: Input code
        :return: Code with shuffled blocks
        """
        pragma_match = re.search(r'pragma\s+solidity.*?;', code)
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
        blocks = re.findall(r'(function.*?}|mapping.*?;|uint.*?;|event.*?;|modifier.*?}|constructor.*?})', body_content, flags=re.DOTALL)
        random.shuffle(blocks)

        shuffled_body = '\n\n'.join(blocks)
        return f"{pragma}\n\n{contract_def}\n{shuffled_body}\n}}"

    def minify_code(self, code):
        """
        Minify Solidity code by removing all unnecessary spaces and line breaks.
        :param code: Input code
        :return: Minified code
        """
        # Remove all line breaks and multiple spaces
        code = re.sub(r'\s+', ' ', code)
        # Remove spaces around curly braces and semicolons
        code = re.sub(r'\s*{\s*', '{', code)
        code = re.sub(r'\s*}\s*', '}', code)
        code = re.sub(r'\s*;\s*', ';', code)
        return code.strip()

    def obfuscate(self, code):
        """
        Apply layout obfuscation
        :param code: Input code
        :return: Obfuscated code
        """
        # 1. Obfuscate variable names
        code = self.obfuscate_variables(code)
        # 2. Obfuscate function names
        code = self.obfuscate_functions(code)
        # 3. Insert fake code and comments
        code = self.insert_fake_code(code)
        # 4. Shuffle code block order
        code = self.shuffle_code_blocks(code)
        # 5. Minify the code
        code = self.minify_code(code)

        return code