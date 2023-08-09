// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.10;

import {RewardsController} from '../../contracts/rewards/RewardsController.sol';
import {RewardsDataTypes} from '../../contracts/rewards/libraries/RewardsDataTypes.sol';

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

    function getUserAssetBalancesLength(address[] calldata assets, address user) external view returns (uint256){
        RewardsDataTypes.UserAssetBalance[] memory userAssetBalances = _getUserAssetBalances(assets, user);
        return userAssetBalances.length;
    }

    function getUserAssetBalances(address[] calldata assets, address user) external view returns (RewardsDataTypes.UserAssetBalance[] memory userAssetBalances){
        return _getUserAssetBalances(assets, user);
    }

    function getUserAssetBalancesAsset(address[] calldata assets, address user) external view returns (address){
        RewardsDataTypes.UserAssetBalance[] memory userAssetBalances = _getUserAssetBalances(assets, user);
        return userAssetBalances[0].asset;
    }

    function getUserAssetBalancesUserBalance(address[] calldata assets, address user) external view returns (uint256){
        RewardsDataTypes.UserAssetBalance[] memory userAssetBalances = _getUserAssetBalances(assets, user);
        return userAssetBalances[0].userBalance;
    }

    function getUserAssetBalancesTotalSupply(address[] calldata assets, address user) external view returns (uint256){
        RewardsDataTypes.UserAssetBalance[] memory userAssetBalances = _getUserAssetBalances(assets, user);
        return userAssetBalances[0].totalSupply;
    }

}