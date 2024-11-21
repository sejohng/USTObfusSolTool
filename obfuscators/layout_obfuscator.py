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
            "// This is a fake comment {}"
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
        pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        matches = re.findall(pattern, code)

        for match in matches:
            if match not in self.variable_map and not self.is_reserved_word(match):
                self.variable_map[match] = self.generate_random_name()
                code = re.sub(r'\b' + match + r'\b', self.variable_map[match], code)

        return code

    def obfuscate_functions(self, code):
        """
        Obfuscate function names
        :param code: Input code
        :return: Code with obfuscated function names
        """
        pattern = r'\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\b'
        matches = re.findall(pattern, code)

        for match in matches:
            if match not in self.function_map:
                self.function_map[match] = self.generate_random_name()
                code = re.sub(r'\b' + match + r'\b', self.function_map[match], code)

        return code

    def shuffle_code_blocks(self, code):
        """
        Shuffle the order of functions and contract members
        :param code: Input code
        :return: Code with shuffled blocks
        """
        # Extract functions or other code blocks
        blocks = re.findall(r'(function.*?}|mapping.*?;|uint.*?;|event.*?;|modifier.*?}|constructor.*?})', code, flags=re.DOTALL)
        random.shuffle(blocks)  # Shuffle the order
        return '\n\n'.join(blocks)

    def insert_fake_code(self, code, num_fake_items=3):
        """
        Insert fake code and comments
        :param code: Input code
        :param num_fake_items: Number of fake items to insert
        :return: Code with added fake code
        """
        fake_items = []
        for i in range(num_fake_items):
            template = random.choice(self.fake_code_templates)
            if "{}" in template:
                fake_items.append(template.format(random.randint(0, 100)))
        return code + '\n\n' + '\n'.join(fake_items)

    def is_reserved_word(self, word):
        """
        Check if a word is a reserved Solidity keyword
        :param word: Input word
        :return: Whether the word is reserved
        """
        reserved_words = {
            "uint", "address", "string", "public", "private", "function", "mapping", "event", "modifier",
            "constructor", "bool", "require", "emit", "revert", "return", "returns", "if", "else", "for", "while",
            "pragma", "contract", "interface", "library", "assembly", "memory", "storage", "pure", "view", "external"
        }
        return word in reserved_words

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

        return code