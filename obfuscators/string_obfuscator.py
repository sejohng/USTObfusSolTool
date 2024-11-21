import re

class StringObfuscator:
    """
    String Obfuscator
    """

    def encode_string(self, string):
        """
        Encode a string by splitting it into parts and concatenating it
        :param string: Input string
        :return: Obfuscated string
        """
        parts = [string[i:i + 2] for i in range(0, len(string), 2)]
        encoded = " + ".join(f'"{part}"' for part in parts)
        return f"string(abi.encodePacked({encoded}))"

    def obfuscate_strings(self, code):
        """
        Obfuscate strings in the given code
        :param code: Input code
        :return: Code with strings obfuscated
        """
        # Match strings enclosed in double quotes
        pattern = r'"([^"]+)"'

        def replace_string(match):
            original_string = match.group(1)
            if len(original_string.strip()) == 0:
                # Skip empty strings
                return '""'
            return self.encode_string(original_string)

        return re.sub(pattern, replace_string, code)

    def obfuscate(self, code):
        """
        Apply string obfuscation to the input code
        :param code: Input code
        :return: Code with string obfuscation applied
        """
        return self.obfuscate_strings(code)

# Example usage
if __name__ == "__main__":
    # Example Solidity code
    solidity_code = '''
    pragma solidity ^0.8.0;

    contract Example {
        function greet() public pure returns (string memory) {
            return "Hello, World!";
        }

        function errorMessage() public pure returns (string memory) {
            return "Something went wrong";
        }
    }
    '''

    obfuscator = StringObfuscator()
    obfuscated_code = obfuscator.obfuscate(solidity_code)

    print(obfuscated_code)