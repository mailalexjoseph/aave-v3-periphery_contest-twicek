import "methods/Methods_base.spec";
using DummyERC20_rewardToken as reward;

///////////////// Properties ///////////////////////

    function global_requires(env e, address user) {
        require e.msg.sender != currentContract;
        require e.msg.sender == user;
        require e.block.timestamp == 42;
    }

    // function sub(uint256 a, uint256 b) returns uint256{
    //     require (b <= a);
    //     return assert_uint256(a - b);
    // }

    // function mul(uint256 a, uint256 b) returns uint256{
    //     if (a == 0 || b == 0){
    //         return assert_uint256(0);
    //     }

    //     uint256 c = assert_uint256(a * b);
    //     require b == (c / a);

    //     return c;
    // }

    // BUG 1
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


    //     claimAllRewards(e, assets, e.msg.sender);

    //     indexAfter, emissionPerSecondAfter, lastUpdateTimestampAfter, distributionEndAfter = getRewardsData(e, AToken, reward);

    //     // index is updated
    //     // require indexAfter > 0;

    //     // is timestamp updated?
    //     assert indexBefore > indexAfter;

    // }

    // BUG 2
    function rewardBalance(env e, address user) returns uint256 {
        return reward.balanceOf(e, user); 
    }

    rule noZeroAddressTransfer() {
        env e;

        address[] assets;
        uint256 amount;
        address to;

        uint256 balanceBefore = rewardBalance(e, 0);
        
        claimRewards(e, assets, amount, to, reward);

        uint256 balanceAfter = rewardBalance(e, 0);

        assert balanceBefore == balanceAfter;
    }

    // BUG 3 (this one might be slow but should work)
    rule accruedRewardsSent() {
        env e;

        address[] assets;
        address[] rewardsList;
        uint256[] unclaimedAmounts;
        uint256[] claimedAmounts;

        // _rewardsList length is 1.
        address[] _rewardsList = getRewardsList(e);
        require _rewardsList.length == 1;

        // Update rewards
        uint128 accruedForUserBefore = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
        require accruedForUserBefore == 0;

        updateRewards(e, assets, e.msg.sender);

        uint128 accruedForUserAfter = getRewardAccruedForUser(e, AToken, reward, e.msg.sender);
        require accruedForUserAfter > 0;

        // calculate current unclaimed rewards
        rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, e.msg.sender);

        // claim rewards
        rewardsList, claimedAmounts = claimAllRewards(e, assets, e.msg.sender);

        // Is accrued reward == claimed amounts?
        assert claimedAmounts[0] == unclaimedAmounts[0];
    }

    // DEFAULT PROPERTIES

    // Property: Reward index monotonically increase
    rule index_keeps_growing(address asset, method f) filtered { f -> !f.isView } {
        uint256 _index = getAssetRewardIndex(asset, reward);

        env e; calldataarg args;
        f(e, args);

        uint256 index_ = getAssetRewardIndex(asset, reward);
        
        assert index_ >= _index;
    }

    // Property: only an authorized user or the user itself can cause a reduction in accrued rewards for this user
    rule onlyAuthorizeCanDecrease(method f) filtered { f -> !f.isView } {

        address user;
        uint256 before = getUserAccruedRewards(user, reward);

        env e;
        calldataarg args;
        f(e,args);

        uint256 after = getUserAccruedRewards(user, reward);

        assert after < before => (getClaimer(user) == e.msg.sender || user == e.msg.sender);
    }

    // Property: User index cannot surpass reward index
    // invariant user_index_LEQ_index(address asset, address reward, address user)
    //     getUserAssetIndex(user, asset, reward) <= getAssetRewardIndex(asset, reward);


    // check this rule for every change in setup to make sure all is reachable 
    // use builtin rule sanity;

    //  Property: claiming reward twice is equivalent to one claim reward 
    //  Note : this rule is implemented by comparing the whole storage 
    rule noDoubleClaim() {

        env e; 
        //arbitrary array of any length (might be constrained due to loop unrolling )
        address[] assets; 
        uint256 l = assets.length;
        address to;
        claimAllRewards(e, assets, to);
        storage afterFirst = lastStorage;
        claimAllRewards(e, assets, to);
        storage afterSecond = lastStorage;

        assert afterSecond == afterFirst;
    }

    // PERMISSIONNED FUNCTIONS

    rule setDistributionEndRestriction() {
        env e;

        calldataarg args;

        address EMISSION_MANAGER = getEmissionManager(e);

        require e.msg.sender != EMISSION_MANAGER;

        setDistributionEnd@withrevert(e, args);

        assert lastReverted;
    }

    rule setEmissionPerSecondRestriction() {
        env e;

        calldataarg args;

        address EMISSION_MANAGER = getEmissionManager(e);

        require e.msg.sender != EMISSION_MANAGER;

        setEmissionPerSecond@withrevert(e, args);

        assert lastReverted;
    }

    rule configureAssetsRestriction() {
        env e;

        calldataarg args;

        address EMISSION_MANAGER = getEmissionManager(e);

        require e.msg.sender != EMISSION_MANAGER;

        configureAssets@withrevert(e, args);

        assert lastReverted;
    }

    rule setTransferStrategyRestriction() {
        env e;

        calldataarg args;

        address EMISSION_MANAGER = getEmissionManager(e);

        require e.msg.sender != EMISSION_MANAGER;

        setTransferStrategy@withrevert(e, args);

        assert lastReverted;
    }

    rule setRewardOracleRestriction() {
        env e;

        calldataarg args;

        address EMISSION_MANAGER = getEmissionManager(e);

        require e.msg.sender != EMISSION_MANAGER;

        setRewardOracle@withrevert(e, args);

        assert lastReverted;
    }

    rule setClaimerRestriction() {
        env e;

        calldataarg args;

        address EMISSION_MANAGER = getEmissionManager(e);

        require e.msg.sender != EMISSION_MANAGER;

        setClaimer@withrevert(e, args);

        assert lastReverted;
    }

    // INPUT SANATIZATION

    // claiming with amount == 0 returns 0 rewards
    rule claimRewards_amount_0() {
        env e;
        address[] assets;
        uint256 amount;
        address to;
        uint256 value;

        require amount == 0;

        value = claimRewards(e, assets, amount, to, reward);

        assert value == 0;
    }

    rule claimRewardsOnBehalf_amount_0() {
        env e;
        address[] assets;
        uint256 amount;
        address to;
        address user;
        uint256 value;

        require amount == 0;

        value = claimRewardsOnBehalf(e, assets, amount, user, to, reward);

        assert value == 0;
    }

    rule claimRewardsToSelf_amount_0() {
        env e;
        address[] assets;
        uint256 amount;
        uint256 value;

        require amount == 0;

        value = claimRewardsToSelf(e, assets, amount, reward);

        assert value == 0;
    }

    // Claiming on behalf with user == address(0) should revert

    rule claimAllRewardsOnBehalf_user_0() {
        env e;

        address[] assets;
        address user;
        address to;

        require user == 0;
        
        claimAllRewardsOnBehalf@withrevert(e, assets, user, to);

        assert lastReverted;
    }

    rule claimRewardsOnBehalf_user_0() {
        env e;

        address[] assets;
        uint256 amount;
        address user;
        address to;

        require user == 0;
        
        claimRewardsOnBehalf@withrevert(e, assets, amount, user, to, reward);

        assert lastReverted;
    }

    // OTHER

    // global index is capped
    rule checkIndexIsCapped() {
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
        address to;

        claimAllRewards(e, assets, e.msg.sender);

        indexAfter, emissionPerSecondAfter, lastUpdateTimestampAfter, distributionEndAfter = getRewardsData(e, AToken, reward);

        assert indexAfter < max_uint104;
    }

    // Index updated for RewardData should update UserData's mapping index as well
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


        //Get rewardData before
        indexBefore, emissionPerSecondBefore, lastUpdateTimestampBefore, distributionEndBefore = getRewardsData(e, AToken, reward);

        //Update rewards
        claimAllRewards(e, assets, e.msg.sender);

        //Get rewardData after
        indexAfter, emissionPerSecondAfter, lastUpdateTimestampAfter, distributionEndAfter = getRewardsData(e, AToken, reward);

        //global index is updated
        require indexBefore < indexAfter;
        uint104 userIndex = getRewardIndexForUser(e, AToken, reward, e.msg.sender);

        //user index should be updated to current global index
        assert assert_uint104(indexAfter) == userIndex;
    }