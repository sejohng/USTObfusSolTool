# USTObfusSolTool
**Developed as part of CSIT 5730 Group 7 Project**

## Author
- **Shijun Jiang** - [sejohng](https://github.com/sejohng): Design code structures, develop project code, and deliver testing solutions
- **Qifan Liao** - [lqfcn](https://github.com/lqfcn): Implement and enhance the obfuscators, refine the preliminary code, and implement test cases
- **Qiutong Li**: Responsible for drafting project plans and reports, as well as offering testing and functional recommendations
- **Yibo Xu**: Provide support for project presentation preparation, slide creation, and post-production verification.
- **Yanxi Yang**: Responsible for drafting project plans and reports, as well as offering testing and functional recommendations

## Intro

USTObfusSolTool is a Solidity code obfuscation tool intended to enhance the security of Ethereum smart contracts by applying manifold obfuscation techniques. The source-level Solidity code could be obfuscated with this tool in such a way that it will be tougher for attackers or reverse engineers to understand the code while keeping intact the original functionality.


## Features
- **Layout Obfuscation**: Renames variables, functions, and events, in order to mask intent.
- **Dataflow Obfuscation**: Introduces temporary variables, splits constants, and modifies assignment logic.
- **Control Flow Obfuscation**: Adds fake conditions, loops, and complex conditional expressions.
- **Dead Code Insertion**: Inserts meaningless code to increase complexity.
- **String Obfuscation**: Encodes and splits strings.

## Usage

Obfuscation Tool

Run the obfuscation tool from the command line with the following syntax:
```bash
python main.py examples/input1.sol examples/output1.sol --all
```
or (Determine based on your system version and different python versions)

```bash
python3 main.py examples/input1.sol examples/output1.sol --all
```

Apply specific obfuscators (see Options below):
```bash
python main.py examples/input1.sol examples/output1.sol --layout --dataflow
```
or (Determine based on your system version and different python versions)

```bash
python3 main.py examples/input1.sol examples/output1.sol --layout --dataflow
```

## Options

`--layout` : Apply layout obfuscation.

`--dataflow` : Apply dataflow obfuscation.

`--controlflow` : Apply control flow obfuscation.

`--deadcode` : Apply dead code insertion.

`--string` : Apply string obfuscation.

`--all` or leave blank : Apply all obfuscation techniques.


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
- Qifan Liao (qliaoad@connect.ust.hk)


