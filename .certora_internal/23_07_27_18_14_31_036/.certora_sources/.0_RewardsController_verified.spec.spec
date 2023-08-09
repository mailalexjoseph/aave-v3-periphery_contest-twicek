import "methods/Methods_base.spec";

///////////////// Properties ///////////////////////

    // Property: only an authorized user or the user itself can cause a reduction in accrued rewards for this user
    rule VerifyAccruedRewards(address[] assets, address[] reward) {

        //All accrued rewards for all reward tokens
        accruedRewards = getAllUserRewards(assets, user);

        (address[] rewardsList, uint256[] claimedAmounts) = claimAllRewards(assets, reward);

        //Is accrued reward == claimedAmounts
        assert(accruedRewards == claimedAmounts);
    }