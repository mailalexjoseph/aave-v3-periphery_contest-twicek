import "methods/Methods_base.spec";
using DummyERC20_rewardToken as reward;

///////////////// Properties ///////////////////////

    function global_requires(env e, address user) {
        require e.msg.sender != currentContract;
        require e.msg.sender == user;
        require e.block.timestamp == 42;
    }

    // BUG 1
    rule rewardsAreUpdated() {
        env e;

        address[] assets;
        address[] rewardsList;
        uint256[] unclaimedAmounts;
        uint256[] claimedAmounts;

        uint256 indexBefore;
        uint256 indexAfter;
        uint256 emissionPerSecond;
        uint256 lastUpdateTimestampBefore;
        uint256 lastUpdateTimestampAfter;
        uint256 distributionEnd;

        //_rewardsList length is 1.
        address[] _rewardsList = getRewardsList(e);
        require _rewardsList.length == 1;

        indexBefore, emissionPerSecond, lastUpdateTimestampBefore, distributionEnd = getRewardsData(e, AToken, reward);


        require e.block.timestamp > lastUpdateTimestampBefore;
        // index is 0
        require indexBefore == 0;


        claimAllRewards(e, assets, e.msg.sender);

        indexAfter, emissionPerSecond, lastUpdateTimestampAfter, distributionEnd = getRewardsData(e, AToken, reward);

        // index is updated
        require indexAfter > 0;

        // is timestamp updated?
        assert lastUpdateTimestampAfter == e.block.timestamp;

    }

    // // BUG 2
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

    // // BUG 3
    // rule accruedRewardsSent() {
    //     env e;

    //     address[] assets;
    //     address[] rewardsList;
    //     uint256[] unclaimedAmounts;
    //     uint256[] claimedAmounts;

    //     // _rewardsList length is 1.
    //     address[] _rewardsList = getRewardsList(e);
    //     require _rewardsList.length == 1;

    //     // Update rewards
    //     uint128 accruedForUserBefore = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
    //     require accruedForUserBefore == 0;

    //     updateRewards(e, assets, e.msg.sender);

    //     uint128 accruedForUserAfter = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
    //     require accruedForUserAfter > 0;

    //     // calculate current unclaimed rewards
    //     rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, e.msg.sender);

    //     // claim rewards
    //     rewardsList, claimedAmounts = claimAllRewards(e, assets, e.msg.sender);

    //     // Is accrued reward == claimed amounts?
    //     assert claimedAmounts[0] == unclaimedAmounts[0];
    // }