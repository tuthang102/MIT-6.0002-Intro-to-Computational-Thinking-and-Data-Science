###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Thang Tran
# Collaborators: Thang Tran
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    # First Method
    # egg_list = []
    # for w in sorted(egg_weights, reverse=True):
    #     egg_count = int(target_weight / w)
    #     egg_list += [w, ] * egg_count
    #     target_weight -= w * egg_count
    #
    # return egg_list

    # Second Method
    minEggs = target_weight
    if target_weight in egg_weights:
        memo[target_weight] = 1
        return 1
    elif memo[target_weight] > 0:
        return memo[target_weight]
    else:
        for i in [c for c in egg_weights if c <= target_weight]:
            numEggs = 1 + dp_make_weight(egg_weights, target_weight - i, memo)
            if numEggs < minEggs:
                minEggs = numEggs
                memo[target_weight] = minEggs
    return minEggs

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n, memo = [0]*(n + 1)))
    print()