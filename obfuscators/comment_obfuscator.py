import re
import random

class CommentObfuscator:
    """
    Comment Obfuscator
    """

    def __init__(self):
        self.fake_comments = [
            "// TODO: Optimize this function",
            "// WARNING: Potential overflow here",
            "// This function handles critical business logic",
            "// Random note: Refactor later",
            "// Performance-critical section",
        ]

    def remove_existing_comments(self, code):
        """
        Remove existing comments
        :param code: Input code
        :return: Code with comments removed
        """
        pattern = r'(//.*?$|/\*.*?\*/)'
        return re.sub(pattern, "", code, flags=re.DOTALL | re.MULTILINE)

    def insert_fake_comments(self, code):
        """
        Insert fake comments
        :param code: Input code
        :return: Code with fake comments inserted
        """
        pattern = r'(;|\{|\})'  # Match delimiters or block boundaries in the code

        def add_comment(match):
            fake_comment = random.choice(self.fake_comments)
            return f"{match.group(1)} {fake_comment}"

        return re.sub(pattern, add_comment, code)

    def obfuscate(self, code):
        """
        Apply comment obfuscation
        :param code: Input code
        :return: Code with applied obfuscation
        """
        code = self.remove_existing_comments(code)
        code = self.insert_fake_comments(code)
        return code