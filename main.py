import sys
import os
from obfuscators.layout_obfuscator import LayoutObfuscator
from obfuscators.dataflow_obfuscator import DataflowObfuscator
from obfuscators.controlflow_obfuscator import ControlflowObfuscator
from obfuscators.deadcode_obfuscator import DeadCodeObfuscator
from obfuscators.string_obfuscator import StringObfuscator
from utils.parser import SolidityParser
from utils.helper import save_output

VERSION = "1.0.0"

def print_usage():
    """
    Prints the usage guide for the tool.
    """
    print(f"""
    ========================================================
         USTObfusSol - Solidity Code Obfuscation Tool
                     Version {VERSION}
    ========================================================
    Authors:
                 Shijun Jiang, Qifan Liao, 
             Qiutong Li, Yibo Xu, Yanxi Yang @HKUST

             Developed as part of CSIT 5730 Project

    Description:
        This tool is designed to obfuscate Solidity smart contracts by applying multiple
        obfuscation techniques to enhance code security and protect intellectual property.


    Usage:
        python3 main.py <input_file> <output_file> [options]

    Options:
        --layout         Apply layout obfuscation
        --dataflow       Apply dataflow obfuscation
        --controlflow    Apply control flow obfuscation
        --deadcode       Apply dead code insertion obfuscation
        --string         Apply string obfuscation
        --arithmetic     Apply arithmetic obfuscation
        --hash           Apply hash-based obfuscation
        --function       Apply function inlining/splitting obfuscation
        --comment        Apply comment masking obfuscation
        --all            Apply all obfuscation techniques

    Example:
        python3 main.py examples/input.sol examples/output.sol --all
    """)

def main():
    """
    Main function for the obfuscation tool.
    Parses input, applies obfuscation, and saves the output.
    """
    if len(sys.argv) < 3:
        print("Error: Missing required arguments.")
        print_usage()
        sys.exit(1)
        
    # Parse input and output file paths
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if len(sys.argv) == 3:
        options = ["--all"]     # Default to --all
    else:
        options = sys.argv[3:]  # Additional options for obfuscation techniques
    
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)
        
    # Parse the Solidity code from the input file
    try:
        print(f"Parsing input file '{input_file}'...")
        parser = SolidityParser(input_file)
        parsed_code = parser.parse()
    except Exception as e:
        print(f"Error: Failed to parse the input file. {e}")
        sys.exit(1)
        
    # Initialize and apply obfuscators
    obfuscated_code = parsed_code
    if "--deadcode" in options or "--all" in options:
        print("Applying dead code insertion obfuscation...")
        deadcode_obfuscator = DeadCodeObfuscator()
        obfuscated_code = deadcode_obfuscator.obfuscate(obfuscated_code)

    if "--string" in options or "--all" in options:
        print("Applying string obfuscation...")
        string_obfuscator = StringObfuscator()
        obfuscated_code = string_obfuscator.obfuscate(obfuscated_code)
        
    if "--dataflow" in options or "--all" in options:
        print("Applying dataflow obfuscation...")
        dataflow_obfuscator = DataflowObfuscator()
        obfuscated_code = dataflow_obfuscator.obfuscate(obfuscated_code)

    if "--controlflow" in options or "--all" in options:
        print("Applying control flow obfuscation...")
        controlflow_obfuscator = ControlflowObfuscator()
        obfuscated_code = controlflow_obfuscator.obfuscate(obfuscated_code)

    if "--layout" in options or "--all" in options:
        print("Applying layout obfuscation...")
        layout_obfuscator = LayoutObfuscator()
        obfuscated_code = layout_obfuscator.obfuscate(obfuscated_code)
        
    # Save the obfuscated code to the output file
    try:
        print(f"Saving obfuscated code to '{output_file}'...")
        save_output(output_file, obfuscated_code)
        print(f"Obfuscated code has been saved to '{output_file}'.")
    except Exception as e:
        print(f"Error: Failed to save the output file. {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()