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
        
        pattern = r'(\b[a-zA-Z_][a-zA-Z0-9_]*\s*[\+\-\*/]\s*[a-zA-Z_0-9]+\b|\b\d+\s*[\+\-\*/]\s*\d+\b)'
        
        def replace_arithmetic(match):
            expression = match.group(1)  
            return f"(({expression}) + 0 - 0)"  
        
        return re.sub(pattern, replace_arithmetic, code)
    
    def obfuscate(self, code):
        """
        Apply arithmetic obfuscation
        :param code: Input code
        :return: Code with applied obfuscation
        """
        return self.obfuscate_arithmetic(code)
    
    
    