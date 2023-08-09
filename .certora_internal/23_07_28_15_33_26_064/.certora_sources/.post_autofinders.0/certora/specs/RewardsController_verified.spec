import "methods/Methods_base.spec";
using DummyERC20_rewardToken as reward;

///////////////// Properties ///////////////////////

    // Property: only an authorized user or the user itself can cause a reduction in accrued rewards for this user
    // rule accruedRewardsSent() {
    //     env e;

    //     address[] assets;
    //     address user;

    //     address[] rewardsList;
    //     uint256[] unclaimedAmounts;
    //     uint256[] claimedAmounts;

    //     require assets.length == 1;

    //     //Update rewards
    //     updateRewards(e, assets, user);

    //     //All accrued rewards for all reward tokens
    //     rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, user);

    //     rewardsList, claimedAmounts = claimAllRewards(e, assets, user);

    //     //Is accrued reward == claimedAmounts
    //     assert unclaimedAmounts[0] == claimedAmounts[0];
    //     assert unclaimedAmounts[1] == claimedAmounts[1];
    //     assert unclaimedAmounts[2] == claimedAmounts[2];
    // }


    // function rewardBalance(address user) returns uint256 {
    //     env e;
    //     return reward.balanceOf(e, user); 
    // }

    // rule noZeroAddressTransfer() {
    //     env e;

    //     address[] assets;
    //     uint256 amount;
    //     address to;

    //     uint256 balanceBefore = rewardBalance(0);
        
    //     claimRewards(e, assets, amount, to, reward);

    //     uint256 balanceAfter = rewardBalance(0);

    //     assert balanceBefore == balanceAfter;
    // }

    rule rewardsAreUpdated() {
        env e;

        address[] assets;
        address asset;
        address user;

        uint256 index;
        uint256 emissionPerSecond;
        uint256 lastUpdateTimestamp;
        uint256 distributionEnd;
        
        claimAllRewards(e, assets, user);

        index, emissionPerSecond, lastUpdateTimestamp, distributionEnd = getRewardsData(e, asset, reward);

        require e.block.timestamp == lastUpdateTimestamp + 60;

        uint256 time = e.block.timestamp;

        claimAllRewards(e, assets, user);

        index, emissionPerSecond, lastUpdateTimestamp, distributionEnd = getRewardsData(e, asset, reward);

        assert lastUpdateTimestamp == time;

    }