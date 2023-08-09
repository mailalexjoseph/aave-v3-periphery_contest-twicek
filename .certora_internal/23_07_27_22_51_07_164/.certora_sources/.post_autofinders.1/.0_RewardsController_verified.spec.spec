import "methods/Methods_base.spec";

///////////////// Properties ///////////////////////

    // Property: only an authorized user or the user itself can cause a reduction in accrued rewards for this user
    // rule accruedRewardsSent() {
    //     env e;

    //     address[] assets;
    //     address user;

    //     address[] rewardsList;
    //     uint256[] unclaimedAmounts;
    //     uint256[] claimedAmounts;
    //     //All accrued rewards for all reward tokens
    //     rewardsList, unclaimedAmounts = getAllUserRewards(e, assets, user);

    //     rewardsList, claimedAmounts = claimAllRewards(e, assets, user);

    //     //Is accrued reward == claimedAmounts
    //     assert unclaimedAmounts[0] == claimedAmounts[0];
    //     assert unclaimedAmounts[1] == claimedAmounts[1];
    //     assert unclaimedAmounts[2] == claimedAmounts[2];
    // }

    rule noZeroAddressTransfer() {
        env e;

        address[] assets;
        uint256 amount;
        address to;
        address reward;

        uint256 balanceBefore = reward.balanceOf(address(0));
        
        claimRewards(e, assets, amount, to, reward);

        uint256 balanceAfter = reward.balanceOf(address(0));

        assert balanceBefore == balanceAfter;
    }

