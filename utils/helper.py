import random
import string
import os

def save_output(output_path, code):
    """
    Save obfuscated Solidity code to a file.
    :param output_path: Path to the output file.
    :param code: The obfuscated code to save.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(code)
        print(f"File saved successfully: {output_path}")
    except Exception as e:
        raise IOError(f"Failed to save file at {output_path}: {e}")

def generate_random_identifier(length=8):
    """
    Generate a random alphanumeric identifier.
    :param length: Length of the generated identifier.
    :return: A random string.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_output_dir_if_not_exists(directory):
    """
    Create the output directory if it doesn't exist.
    :param directory: The directory path.
    """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Directory created: {directory}")
        except Exception as e:
            raise IOError(f"Failed to create directory {directory}: {e}")

def log_message(message, level="INFO"):
    """
    Log a message with a given severity level.
    :param message: The message to log.
    :param level: The severity level (e.g., "INFO", "ERROR").
    """
    print(f"[{level}] {message}")