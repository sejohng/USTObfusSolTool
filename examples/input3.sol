// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * Example Solidity contract for testing obfuscation.
 * Author: Shijun Jiang @HKUST
 */

contract AdvancedExample {
    struct User {
        address userAddress;
        uint256 balance;
        bool isActive;
    }

    mapping(address => User) private users;
    address private owner;

    event UserCreated(address indexed user, uint256 balance);
    event FundsDeposited(address indexed user, uint256 amount);
    event FundsWithdrawn(address indexed user, uint256 amount);
    event UserDeactivated(address indexed user);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    modifier onlyActiveUser(address user) {
        require(users[user].isActive, "User is not active");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function createUser(address user, uint256 initialBalance) public onlyOwner {
        require(users[user].userAddress == address(0), "User already exists");
        users[user] = User(user, initialBalance, true);
        emit UserCreated(user, initialBalance);
    }

    function depositFunds(address user, uint256 amount) public payable onlyActiveUser(user) {
        require(msg.value == amount, "Transferred value must match the deposit amount");
        users[user].balance += amount;
        emit FundsDeposited(user, amount);
    }

    function withdrawFunds(uint256 amount) public onlyActiveUser(msg.sender) {
        require(users[msg.sender].balance >= amount, "Insufficient balance");
        users[msg.sender].balance -= amount;
        payable(msg.sender).transfer(amount);
        emit FundsWithdrawn(msg.sender, amount);
    }

    function deactivateUser(address user) public onlyOwner {
        require(users[user].isActive, "User is already deactivated");
        users[user].isActive = false;
        emit UserDeactivated(user);
    }

    function getUserBalance(address user) public view returns (uint256) {
        if (users[user].balance > 0){
            return users[user].balance;
        } else {
            return 0;
        }
    }

    function getUserStatus(address user) public view returns (bool) {
        return users[user].isActive;
    }

    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}