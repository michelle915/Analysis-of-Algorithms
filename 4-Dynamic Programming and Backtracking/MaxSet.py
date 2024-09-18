# This version did not pass all gradescope tests, but everything seems to be working

def max_independent_set(nums):
    if not nums:
        return []

    n = len(nums)

    if n == 0:
        return []
    elif n == 1:
        return [nums[0]] if nums[0] >= 0 else []
    
    dp = [0] * n            # dynamic programming (DP) table to store subproblems (max sums)
    selected = [False] * n  # array to track which elements are included in the optimal solution
    
    dp[0] = nums[0]
    selected[0] = nums[0] > 0
    
    for i in range(1, n):
        include = nums[i] + (dp[i-2] if i > 1 and dp[i-2] > 0 else 0)
        exclude = dp[i-1]
        
        if include > exclude:
            dp[i] = include
            selected[i] = True
        else:
            dp[i] = exclude
    
    # Reconstruct the solution
    solution = []
    i = n - 1
    while i >= 0:
        if selected[i]:
            solution.append(nums[i])
            i -= 2 
        else:
            i -= 1
    
    return solution[::-1]  # Return reversed solution to maintain original order


print(max_independent_set([7,2,5,8,6]))         # Output: [7,5,6]
print(max_independent_set([2,6,5,8,9]))         # Output: [2,5,9]
print(max_independent_set([-1, -1, 0]))         # Output: [0]
print(max_independent_set([-1, -1, -10, -34]))  # Output: []
print(max_independent_set([0]))                 # Output: [0]
print(max_independent_set([-1,-2,1,3]))         # Output: [3]
print(max_independent_set([-1,-2,1,-2,4]))      # Output: [1, 4]