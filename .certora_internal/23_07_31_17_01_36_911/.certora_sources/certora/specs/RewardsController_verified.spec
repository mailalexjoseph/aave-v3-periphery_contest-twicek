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

        require e.msg.sender == user;


        //Asset decimals is 18
        uint8 decimals;
        decimals = getAssetDecimals(e, AToken);
        require decimals == 18;

        //Asset has a unique reward token which is reward
        uint128 rewardsCount;
        rewardsCount = getRewardsCountForAsset(e, AToken);
        require rewardsCount == 1;
        // address availableReward;
        // availableReward = getRewardAddressForAssetAtIndex(e, AToken, 0);
        // require availableReward == reward;

        //Constraint _assets mapping
        uint256 index;
        uint256 emissionPerSecond;
        uint256 lastUpdateTimestamp;
        uint256 distributionEnd;

        index, emissionPerSecond, lastUpdateTimestamp, distributionEnd = getRewardsData(e, AToken, reward);

        require emissionPerSecond > 0;
        require distributionEnd > 0;


        //Update rewards
        // updateRewards(e, assets, user);
        
        //All accrued rewards for all reward tokens
        // rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, user);

        // uint256 balanceBefore = reward.balanceOf(e, user);

        // rewardsList, claimedAmounts = claimAllRewards(e, assets, user);

        // uint256 balanceAfter = reward.balanceOf(e, user);

        // require balanceBefore <= balanceAfter;

        // uint256 balance = assert_uint256(balanceAfter - balanceBefore);

        rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, user);

        rewardsList, claimedAmounts = claimAllRewards(e, assets, user);
        //Is accrued reward == claimedAmounts
        assert claimedAmounts[0] == unclaimedAmounts[0];
    }

    function sub(uint256 a, uint256 b) returns uint256{
        require (b <= a);
        return assert_uint256(a - b);
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

    //     // ADD user = msg.sender
        

    //     index, emissionPerSecond, lastUpdateTimestampBefore, distributionEnd = getRewardsData(e, AToken, reward);

    //     claimAllRewards(e, assets, user);

    //     index, emissionPerSecond, lastUpdateTimestampAfter, distributionEnd = getRewardsData(e, AToken, reward);

    //     assert lastUpdateTimestampAfter >= lastUpdateTimestampBefore;

    // }