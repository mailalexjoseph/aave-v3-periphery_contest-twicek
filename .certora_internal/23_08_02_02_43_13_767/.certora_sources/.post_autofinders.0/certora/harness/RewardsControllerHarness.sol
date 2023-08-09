// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.10;

import {RewardsController} from '../../contracts/rewards/RewardsController.sol';

contract RewardsControllerHarness is RewardsController {
    
    constructor(address emissionManager) RewardsController(emissionManager) {}
    // returns an asset's reward index
    function getAssetRewardIndex(address asset, address reward) external view returns (uint256) {
        return _assets[asset].rewards[reward].index;
    }

    function updateRewards(address[] calldata assets, address user) external {
        _updateDataMultiple(user, _getUserAssetBalances(assets, user));
    }

    function getRewardsCountForAsset(address asset) external view returns (uint128) {
        return _assets[asset].availableRewardsCount;
    }

    function getRewardAddressForAssetAtIndex(address asset, uint128 index) external view returns (address) {
        return _assets[asset].availableRewards[index];
    }

    function getRewardList(address asset, uint128 index) external view returns (address) {
        return _assets[asset].availableRewards[index];
    }

    function getRewardAccruedForUser(address asset, address reward, address user) external view returns (uint128){
        return _assets[asset].rewards[reward].usersData[user].accrued;
    }



}