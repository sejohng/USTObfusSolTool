// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * Example Solidity contract for testing obfuscation.
 * Author: Group7 @HKUST
 */

contract ComplexExample {
    uint256 public totalSupply;
    mapping(address => uint256) private balances;
    address private owner;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 initialSupply) {
        totalSupply = initialSupply;
        balances[msg.sender] = initialSupply;
        owner = msg.sender;
        emit OwnershipTransferred(address(0), msg.sender);
    }

    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Invalid address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    function mint(uint256 amount) public onlyOwner {
        totalSupply += amount;
        balances[owner] += amount;
    }

    function burn(uint256 amount) public onlyOwner {
        require(balances[owner] >= amount, "Insufficient balance to burn");

        totalSupply -= amount;
        balances[owner] -= amount;
    }

    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}