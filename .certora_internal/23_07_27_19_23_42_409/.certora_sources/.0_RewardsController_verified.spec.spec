import "methods/Methods_base.spec";

///////////////// Properties ///////////////////////

    // Property: only an authorized user or the user itself can cause a reduction in accrued rewards for this user
    rule VerifyAccruedRewards() {
        env e;

        address[] assets;
        address[] reward;
        address user;
        //All accrued rewards for all reward tokens
        address[] rewardsList uint256[] unclaimedAmounts = getAllUserRewards(assets, user);

        address[] rewardsList uint256[] claimedAmounts = claimAllRewards(assets, reward);

        //Is accrued reward == claimedAmounts
        assert unclaimedAmounts == claimedAmounts;
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