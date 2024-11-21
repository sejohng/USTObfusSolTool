![image](https://github.com/user-attachments/assets/34d45afb-7b0f-4e40-8522-628ba53942ed)# USTObfusSolTool
**Developed as part of CSIT 5730 Group7 Project**

## Author
- **Shijun Jiang** - [sejohng](https://github.com/sejohng): Design code structures, develop project code, and deliver testing solutions
- **Qifan Liao** - [lqfcn](https://github.com/lqfcn): Refine the preliminary code, implement test cases, and enhance the functionality of the obfuscator
- **Qiutong Li**: Responsible for drafting project plans and reports, as well as offering testing and functional recommendations
- **Yibo Xu**: Provide support for project presentation preparation, slide creation, and post-production verification.
- **Yanxi Yang**: Responsible for drafting project plans and reports, as well as offering testing and functional recommendations

## Intro

USTObfusSolTool is a Solidity code obfuscation tool designed to enhance the security of Ethereum smart contracts by applying multiple obfuscation techniques. The tool obfuscates Solidity code at the source level to make it more challenging for attackers or reverse engineers to analyze the code while maintaining its original functionality.


## Features
- Layout Obfuscation: Renames variables, functions, and events to obscure intent.
- Dataflow Obfuscation: Introduces temporary variables, splits constants, and modifies assignment logic.
- Control Flow Obfuscation: Adds fake conditions, loops, and complex conditional expressions.
- Dead Code Insertion: Inserts meaningless code to increase complexity.
- String Obfuscation: Encodes and splits strings.
- Arithmetic Obfuscation: Adds redundant calculations to arithmetic expressions.
- Function Obfuscation: Inlines simple functions and splits complex ones.
- Comment Obfuscation: Removes existing comments and inserts misleading ones.
- Hash-Based Obfuscation: Converts variable and function names into hashed identifiers.

## Usage

Obfuscation Tool

Run the obfuscation tool from the command line with the following syntax:
```bash
python main.py examples/input1.sol examples/output1.sol --all
```
or

```bash
python3 main.py examples/input1.sol examples/output1.sol --all
```

Apply specific obfuscators (see Options below):
```bash
python main.py examples/input1.sol examples/output1.sol --layout --dataflow
```
or

```bash
python3 main.py examples/input1.sol examples/output1.sol --layout --dataflow
```

## Options

`--layout` : Apply layout obfuscation.

`--dataflow` : Apply dataflow obfuscation.

`--controlflow` : Apply control flow obfuscation.

`--deadcode` : Apply dead code insertion.

`--string` : Apply string obfuscation.

`--arithmetic` : Apply arithmetic obfuscation.

`--function` : Apply function inlining and splitting.

`--comment` : Apply comment masking obfuscation.

`--hash` : Apply hash-based obfuscation for variable and function names.

`--all` : Apply all obfuscation techniques.


## Running Tests

About the Tests

The tests/ folder contains unit tests for all major obfuscation modules and utilities. Each test file verifies the functionality of a specific obfuscator or utility.
To run all test cases at once, use the following command:

```bash
python3 -m unittest discover -s tests
```
To run a specific test file, for example, test_layout.py:

```bash
python3 -m unittest tests/test_layout.py
```

## Contact

For questions or assistance, please contact the authors:
- Shijun Jiang (shijun.jiang@connect.ust.hk)


