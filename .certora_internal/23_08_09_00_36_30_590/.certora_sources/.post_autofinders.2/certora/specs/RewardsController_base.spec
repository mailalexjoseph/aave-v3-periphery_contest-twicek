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

    // rule BetterRewardsAreUpdated() {
    //     // env e1;
    //     env e;

    //     uint256 indexBefore;
    //     uint256 indexAfter;
    //     uint256 emissionPerSecondBefore;
    //     uint256 emissionPerSecondAfter;
    //     uint256 lastUpdateTimestampBefore;
    //     uint256 lastUpdateTimestampAfter;
    //     uint256 distributionEndBefore;
    //     uint256 distributionEndAfter;

    //     address[] assets;
    //     // _rewardsList length is 1.
    //     address[] _rewardsList = getRewardsList(e);
    //     require _rewardsList.length == 1;


    //     indexBefore, emissionPerSecondBefore, lastUpdateTimestampBefore, distributionEndBefore = getRewardsData(e, AToken, reward);

    //     require emissionPerSecondBefore > 0;
    //     require distributionEndBefore > 0;

    //     // Claim rewards

    //     // require e2.block.timestamp > e1.block.timestamp;
    //     // require e2.block.number > e1.block.number;
    //     // uint128 rewardCount = getRewardsCountForAsset(e2, AToken);
    //     // require rewardCount > 0;
    //     // require e1.msg.sender == e2.msg.sender;

    //     // uint256 userAssetBalancesLength = getUserAssetBalancesLength(e2, assets, e2.msg.sender);
    //     // require userAssetBalancesLength > 0;

    //     updateRewards(e, assets, e.msg.sender);

    //     // bool lastRev = lastReverted;

    //     indexAfter, emissionPerSecondAfter, lastUpdateTimestampAfter, distributionEndAfter = getRewardsData(e, AToken, reward);

    //     require indexAfter >= indexBefore;
    //     require emissionPerSecondAfter == emissionPerSecondBefore;
    //     require distributionEndAfter == distributionEndBefore;
    //     // require lastUpdateTimestampAfter > lastUpdateTimestampBefore;

    //     assert lastUpdateTimestampAfter == e.block.timestamp;
    // }

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


    // A AToken balance is needed to update rewards?

    // if index has increased and user balance is positive -> rewards should accrue for user

    // rule indexBalance_accrue() {
    //     env e;


    //     uint256 indexBefore;
    //     uint256 indexAfter;
    //     uint256 emissionPerSecondBefore;
    //     uint256 emissionPerSecondAfter;
    //     uint256 lastUpdateTimestampBefore;
    //     uint256 lastUpdateTimestampAfter;
    //     uint256 distributionEndBefore;
    //     uint256 distributionEndAfter;

    //     address[] assets;

    //     // _rewardsList length is 1.
    //     address[] _rewardsList = getRewardsList(e);
    //     require _rewardsList.length == 1;
    //     require _rewardsList[0] == reward;

    //     uint256 userBalance = getUserAssetBalancesUserBalance(e, assets, e.msg.sender);
    //     require userBalance > 0;

    //     indexBefore, emissionPerSecondBefore, lastUpdateTimestampBefore, distributionEndBefore = getRewardsData(e, AToken, reward);

    //     require emissionPerSecondBefore > 0;
    //     require distributionEndBefore > 0;

    //     uint128 accruedBefore = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);

    //     updateRewards(e, assets, e.msg.sender);

    //     indexAfter, emissionPerSecondAfter, lastUpdateTimestampAfter, distributionEndAfter = getRewardsData(e, AToken, reward);

    //     require indexAfter > indexBefore;
    //     require emissionPerSecondAfter == emissionPerSecondBefore;
    //     require distributionEndAfter == distributionEndBefore;
    //     require lastUpdateTimestampAfter > lastUpdateTimestampBefore;

    //     uint128 accruedAfter = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);

    //     assert accruedAfter > accruedBefore;
    // }

    // function single_env_conditions(env e) {

    // }

    function two_env_conditions(env e1, env e2) {
        require e1.msg.sender == e2.msg.sender;
        require e2.block.timestamp > e1.block.timestamp;
    }

    function initializeRewardData(uint256 index, uint256 emissionPerSecond, uint256 lastUpdateTimestamp, uint256 distributionEnd) {
        require emissionPerSecond > 0;
        require distributionEnd > 0;
        require index < distributionEnd;
    }

    function sanatizeRewardData(uint256 emissionPerSecondBefore, uint256 emissionPerSecondAfter, uint256 distributionEndBefore, uint256 distributionEndAfter) {
        require emissionPerSecondAfter == emissionPerSecondBefore;
        require distributionEndAfter == distributionEndBefore;
    }

    rule indexBalance_accrued() {
        env e;
        env e2;

        // ADD ENV CONDITIONS SINGLE AND DOUBLE BLOCK
        two_env_conditions(e, e2);

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
        require _rewardsList[0] == reward;

        //BLOCK e

        //Check userBalance is positive
        uint256 userBalance = getUserAssetBalancesUserBalance(e, assets, e.msg.sender);
        require userBalance > 0;

        //Get accrued before
        uint128 accruedBefore = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
        //Check accrued was already positive
        require accruedBefore != 0;

        //Get rewardData
        indexBefore, emissionPerSecondBefore, lastUpdateTimestampBefore, distributionEndBefore = getRewardsData(e, AToken, reward);

        // ADD INITIALIZATION OF CONTRACT (emission > 0, dend > 0, etc)
        initializeRewardData(indexBefore, emissionPerSecondBefore, lastUpdateTimestampBefore, distributionEndBefore);
        require emissionPerSecondBefore > 0;
        require distributionEndBefore > 0;
        require indexBefore < distributionEndBefore;

        //BLOCK e2

        //Update rewards
        updateRewards(e2, assets, e.msg.sender);

        //Get informations at block e2
        indexAfter, emissionPerSecondAfter, lastUpdateTimestampAfter, distributionEndAfter = getRewardsData(e2, AToken, reward);
        sanatizeRewardData(emissionPerSecondBefore, emissionPerSecondAfter, distributionEndBefore, distributionEndAfter);
        require emissionPerSecondAfter == emissionPerSecondBefore;
        require distributionEndAfter == distributionEndBefore;   
        require indexBefore < indexAfter;
        uint128 accruedAfter = getRewardAccruedForUser(e, AToken, reward, e2.msg.sender);
        uint104 userIndex = getRewardIndexForUser(e, AToken, reward, e2.msg.sender);

        //Check index has increased enough to generate accrual
        require indexAfter - indexBefore >= 10^AToken.decimals(e2);
        require assert_uint104(indexAfter) > userIndex;

        //Rewards should accrue for user
        assert accruedAfter > accruedBefore;
    }


    // index updated for RewardData should update UserData mapping as well

    rule globalIndex_userIndex() {
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
        require _rewardsList[0] == reward;


        //Get rewardData
        indexBefore, emissionPerSecondBefore, lastUpdateTimestampBefore, distributionEndBefore = getRewardsData(e, AToken, reward);


        //BLOCK e2

        //Update rewards
        claimAllRewards(e, assets, e.msg.sender);

        //Get informations at block e2
        indexAfter, emissionPerSecondAfter, lastUpdateTimestampAfter, distributionEndAfter = getRewardsData(e, AToken, reward);

        require indexBefore < indexAfter;
        uint104 userIndex = getRewardIndexForUser(e, AToken, reward, e.msg.sender);

        // //Check index has increased enough to generate accrual
        // require indexAfter - indexBefore >= 10^AToken.decimals(e2);
        assert assert_uint104(indexAfter) == userIndex;
    }








