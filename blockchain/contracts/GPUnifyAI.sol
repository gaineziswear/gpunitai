// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GPUnifyAI is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10**18;
    mapping(address => bool) public verifiedProviders;
    
    event ProviderAdded(address indexed provider);
    event ComputePurchased(address user, uint256 minutes);

    constructor() ERC20("GPUnifyAI", "GPAI") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    function addProvider(address _provider) external onlyOwner {
        verifiedProviders[_provider] = true;
        emit ProviderAdded(_provider);
    }

    function purchaseCompute(uint256 _minutes) external {
        uint256 cost = _minutes * 10**18;
        _burn(msg.sender, cost);
        emit ComputePurchased(msg.sender, _minutes);
    }
}
