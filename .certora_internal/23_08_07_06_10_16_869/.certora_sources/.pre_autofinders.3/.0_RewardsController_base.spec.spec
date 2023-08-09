import "methods/Methods_base.spec";
using DummyERC20_rewardToken as reward;

///////////////// Properties ///////////////////////

    // Property: Reward index monotonically increase
    rule index_keeps_growing(address asset, address reward, method f) filtered { f -> !f.isView } {
        uint256 _index = getAssetRewardIndex(asset, reward);

        env e; calldataarg args;
        f(e, args);

        uint256 index_ = getAssetRewardIndex(asset, reward);
        
        assert index_ >= _index;
    }











