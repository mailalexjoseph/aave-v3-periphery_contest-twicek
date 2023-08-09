import "methods/Methods_base.spec";
using DummyERC20_rewardToken as reward;
using DummyERC20_rewardTokenB as rewardB;

///////////////// Properties ///////////////////////
    rule accruedRewardsSent() {
        env e;

        address[] assets;
        address[] rewardsList;
        uint256[] unclaimedAmounts;
        uint256[] claimedAmounts;

        // _rewardsList length is 1.
        address[] _rewardsList = getRewardsList(e);
        require _rewardsList.length == 2;

        // Update rewards
        uint128 accruedForUserBefore = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
        require accruedForUserBefore == 0;
        uint128 accruedForUserBeforeB = getRewardAccruedForUser(e, AToken, rewardB, e.msg.sender);
        require accruedForUserBeforeB == 0;

        updateRewards(e, assets, e.msg.sender);

        uint128 accruedForUserAfter = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
        require accruedForUserAfter > 0;

        uint128 accruedForUserAfterB = getRewardAccruedForUser(e, AToken, rewardB, e.msg.sender);
        require accruedForUserAfterB > 0;

        // calculate current unclaimed rewards
        rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, e.msg.sender);

        // claim rewards
        rewardsList, claimedAmounts = claimAllRewards(e, assets, e.msg.sender);

        // Is accrued reward == claimed amounts?
        assert claimedAmounts[0] == unclaimedAmounts[0];
        assert claimedAmounts[1] == unclaimedAmounts[1];
    }