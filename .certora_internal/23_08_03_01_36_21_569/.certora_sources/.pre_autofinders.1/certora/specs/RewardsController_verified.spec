import "methods/Methods_base.spec";
using DummyERC20_rewardToken as reward;

///////////////// Properties ///////////////////////

    function global_requires(env e, address user) {
        require e.msg.sender != currentContract;
        require e.msg.sender == user;
        require e.block.timestamp == 42;
    }


    rule accruedRewardsSent() {
        env e;
        global_requires(e, e.msg.sender);

        address[] assets;
        address[] rewardsList;
        uint256[] unclaimedAmounts;
        uint256[] claimedAmounts;

        //assets length is 1 and AToken is the only asset
        require assets[0] == AToken;
        require assets.length == 1;

        //_rewardsList length is 1.
        address[] _rewardsList = getRewardsList(e);
        require _rewardsList.length == 1;

        uint128 accruedForUserBefore = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
        require accruedForUserBefore == 0;

        updateRewards(e, assets, e.msg.sender);

        uint128 accruedForUserAfter = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
        require accruedForUserAfter > 0;

        // assert 1 == 1;
        rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, e.msg.sender);

        rewardsList, claimedAmounts = claimAllRewards(e, assets, e.msg.sender);
        //Is accrued reward == claimedAmounts
        assert claimedAmounts[0] == unclaimedAmounts[0];
    }


    // rule accruedRewardsSent() {
    //     env e;
    //     global_requires(e, e.msg.sender);

    //     address[] assets;
    //     address[] rewardsList;
    //     uint256[] unclaimedAmounts;
    //     uint256[] claimedAmounts;

    //     //assets length is 1 and AToken is the only asset
    //     require assets[0] == AToken;
    //     require assets.length == 1;

    //     //_rewardsList length is 1.
    //     address[] _rewardsList = getRewardsList(e);
    //     require _rewardsList.length == 1;

    //     uint128 accruedForUserBefore = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
    //     require accruedForUserBefore == 0;

    //     storage beforeUpdate = lastStorage;

    //     updateRewards(e, assets, e.msg.sender);

    //     storage afterUpdate = lastStorage;

    //     require beforeUpdate != afterUpdate;

    //     uint128 accruedForUserAfter = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
    //     require accruedForUserAfter > 0;

    //     // assert 1 == 1;
    //     rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, e.msg.sender);

    //     rewardsList, claimedAmounts = claimAllRewards(e, assets, e.msg.sender);
    //     //Is accrued reward == claimedAmounts
    //     assert claimedAmounts[0] == unclaimedAmounts[0];
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