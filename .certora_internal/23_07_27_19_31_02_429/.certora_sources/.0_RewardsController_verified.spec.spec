import "methods/Methods_base.spec";

///////////////// Properties ///////////////////////

    // Property: only an authorized user or the user itself can cause a reduction in accrued rewards for this user
    rule VerifyAccruedRewards() {
        env e;

        address[] assets;
        address user;

        address[] rewardsList;
        uint256[] unclaimedAmounts;
        uint256[] claimedAmounts;
        //All accrued rewards for all reward tokens
        rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, user);

        rewardsList, claimedAmounts = claimAllRewards(e, assets, user);

        //Is accrued reward == claimedAmounts
        for(uint256 i = 0; i < rewardList.length; i++){
            assert unclaimedAmounts[i] == claimedAmounts[i];
        }
    }


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