// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * Example Solidity contract for testing obfuscation.
 * Author: Shijun Jiang @HKUST
 */
contract ExampleContract {
    uint256 public myVariable;
    uint256 private constant initialValue = 100;

    event MyEvent(address indexed sender, uint256 value);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner.");
        _;
    }

    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function setVariable(uint256 newValue) public {
        myVariable = newValue;
    }

    function getDouble(uint256 input) public pure returns (uint256) {
        return input * 2;
    }

    function emitEvent(uint256 value) public {
        emit MyEvent(msg.sender, value);
    }

    function internalLogic() internal view returns (uint256) {
        return myVariable + initialValue;
    }
}