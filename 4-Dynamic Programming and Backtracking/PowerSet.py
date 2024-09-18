def powerset(inputSet):
    result = [] 
    
    def backtrack(start, currentSubset):
        # Add a copy of the current subset to the result
        result.append(currentSubset.copy())
        
        # Explore further subsets
        for i in range(start, len(inputSet)):
            # Include the current element and move to the next element
            currentSubset.append(inputSet[i])
            backtrack(i + 1, currentSubset)
            # Backtrack to explore subsets without the current element
            currentSubset.pop()
    
    backtrack(0, [])
    return result

print(powerset([1, 2, 3]))  # Output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
print(powerset([]))         # Output: [[]]       
