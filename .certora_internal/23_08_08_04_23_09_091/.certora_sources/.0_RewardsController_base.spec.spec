import "methods/Methods_base.spec";
using DummyERC20_rewardToken as reward;

///////////////// Properties ///////////////////////

    // rule rewardsAreUpdated() {
    //     env e;

    //     address[] assets;
    //     address[] rewardsList;
    //     uint256[] unclaimedAmounts;
    //     uint256[] claimedAmounts;

    //     uint256 indexBefore;
    //     uint256 indexAfter;
    //     uint256 emissionPerSecondBefore;
    //     uint256 emissionPerSecondAfter;
    //     uint256 lastUpdateTimestampBefore;
    //     uint256 lastUpdateTimestampAfter;
    //     uint256 distributionEndBefore;
    //     uint256 distributionEndAfter;

    //     //_rewardsList length is 1.
    //     address[] _rewardsList = getRewardsList(e);
    //     require _rewardsList.length == 1;

    //     require reward.decimals(e) == 18;
    //     require AToken.decimals(e) == 18;

    //     indexBefore, emissionPerSecondBefore, lastUpdateTimestampBefore, distributionEndBefore = getRewardsData(e, AToken, reward);


    //     uint256 time = e.block.timestamp;
    //     require time > lastUpdateTimestampBefore;
    //     require time <= max_uint64;

    //     // require assets[0] == AToken;
    //     uint256 totalSupply = getUserAssetBalancesTotalSupply(e, assets, e.msg.sender);
    //     require totalSupply > 10^18;

    //     require emissionPerSecondBefore != 0;
    //     require distributionEndBefore > lastUpdateTimestampBefore;
    //     require distributionEndBefore > time;


    //     uint256 assetUnit = 10^18;
    //     uint256 timeDelta = assert_uint256(time - lastUpdateTimestampBefore);
    //     require assert_uint256(emissionPerSecondBefore * timeDelta * assetUnit) >= totalSupply;
    //     // index is 0
    //     // require indexBefore == 0;

    //     // Update rewards
    //     uint128 accruedForUserBefore = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
    //     require accruedForUserBefore == 0;

    //     claimAllRewards(e, assets, e.msg.sender);

    //     uint128 accruedForUserAfter = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
    //     require accruedForUserAfter > 0;


    //     indexAfter, emissionPerSecondAfter, lastUpdateTimestampAfter, distributionEndAfter = getRewardsData(e, AToken, reward);

    //     // index is updated
    //     // require indexAfter > 0;

    //     // is timestamp updated?
    //     assert indexBefore > indexAfter;

    // }

    rule BetterRewardsAreUpdated() {
        // env e1;
        env e;

        uint256 indexBefore;
        uint256 indexAfter;
        uint256 emissionPerSecondBefore;
        uint256 emissionPerSecondAfter;
        uint256 lastUpdateTimestampBefore;
        uint256 lastUpdateTimestampAfter;
        uint256 distributionEndBefore;
        uint256 distributionEndAfter;

        address[] assets;
        // _rewardsList length is 1.
        address[] _rewardsList = getRewardsList(e);
        require _rewardsList.length == 1;


        indexBefore, emissionPerSecondBefore, lastUpdateTimestampBefore, distributionEndBefore = getRewardsData(e, AToken, reward);

        // Claim rewards

        // require e2.block.timestamp > e1.block.timestamp;
        // require e2.block.number > e1.block.number;
        // uint128 rewardCount = getRewardsCountForAsset(e2, AToken);
        // require rewardCount > 0;
        // require e1.msg.sender == e2.msg.sender;

        // uint256 userAssetBalancesLength = getUserAssetBalancesLength(e2, assets, e2.msg.sender);
        // require userAssetBalancesLength > 0;

        claimAllRewards@withrevert(e, assets, e.msg.sender);

        bool lastRev == lastReverted;

        indexAfter, emissionPerSecondAfter, lastUpdateTimestampAfter, distributionEndAfter = getRewardsData(e, AToken, reward);

        // require indexAfter > indexBefore;
        // require emissionPerSecondAfter == emissionPerSecondBefore;
        // require distributionEndAfter == distributionEndBefore;
        // require lastUpdateTimestampAfter > lastUpdateTimestampBefore;

        assert !lastRev => lastUpdateTimestampAfter == e.block.timestamp;
    }

    // function rewardBalance(address user) returns uint256 {
    //     env e;
    //     return reward.balanceOf(e, user); 
    // }


    // rule successFalseEqualNoClaim() {
    //     env e;

    //     address[] assets;
    //     address to;

    //     require rewardBalance(e.msg.sender) == 0;

    //     claimAllRewardsToSelf@withrevert(e, assets);

    //     assert !lastReverted => rewardBalance(e.msg.sender) != 0;
    // }

    //Check distributor using Update only maybe


    rule checkIndexCapped() {
        env e;

        address[] assets;
        address to;

        require rewardBalance(e.msg.sender) == 0;

        claimAllRewards@withrevert(e, assets);

        assert index < ;
    }









