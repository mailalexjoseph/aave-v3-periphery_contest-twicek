import "methods/Methods_base.spec";
using DummyERC20_rewardToken as reward;

///////////////// Properties ///////////////////////

    // Property: only an authorized user or the user itself can cause a reduction in accrued rewards for this user
    rule accruedRewardsSent() {
        env e;

        address[] assets;
        address user;

        address[] rewardsList;
        uint256[] unclaimedAmounts;
        uint256[] claimedAmounts;

        //Asset is unique
        require assets.length == 1;
        require assets[0] == AToken;

        //Asset has a unique reward token
        address[] rewards;
        rewards = getRewardsByAsset(e, AToken);
        require rewards.length == 1;
        require rewards[0] == reward;

        //Update rewards
        // updateRewards(e, assets, user);
        
        //All accrued rewards for all reward tokens
        // rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, user);

        rewardsList, claimedAmounts = claimAllRewards(e, assets, user);

        //Is accrued reward == claimedAmounts
        assert  claimedAmounts[0] == reward.balanceOf(e, user);
    }


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

    // rule rewardsAreUpdated() {
    //     env e;

    //     address[] assets;
    //     // address asset;
    //     address user;

    //     uint256 index;
    //     uint256 emissionPerSecond;
    //     uint256 lastUpdateTimestampBefore;
    //     uint256 lastUpdateTimestampAfter;
    //     uint256 distributionEnd;

    //     require assets.length == 1;
    //     require assets[0] == AToken;
    //     require AToken.decimals(e) == 18;
        

    //     index, emissionPerSecond, lastUpdateTimestampBefore, distributionEnd = getRewardsData(e, AToken, reward);

    //     claimAllRewards(e, assets, user);

    //     index, emissionPerSecond, lastUpdateTimestampAfter, distributionEnd = getRewardsData(e, AToken, reward);

    //     assert lastUpdateTimestampAfter >= lastUpdateTimestampBefore;

    // }