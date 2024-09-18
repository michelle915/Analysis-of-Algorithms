def amount(A, S):
    result = []
    A.sort()

    def backtrack(start, target, combo):
        # Base case: if target sum is reached, add the current combo to the result
        if target == 0:
            result.append(combo)
            return
        
        for i in range(start, len(A)):
            # Skip duplicates
            if A[i] == A[i-1] and i > start:
                continue
            
            # If remaining numbers will create sums greater than target, break
            if A[i] > target:
                break

            backtrack(i +1, target - A[i], combo + [A[i]])
    
    backtrack(0, S, [])
    return result

print(amount([11,1,3,2,6,1,5], 8)) # result = [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]]