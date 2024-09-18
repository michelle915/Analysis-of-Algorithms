# def dna_match_topdown1(DNA1, DNA2):
#     memo = {}

#     def lcs(i, j):
#         if i == len(DNA1) or j == len(DNA2):
#             return 0
#         if (i, j) in memo:
#             return memo [(i, j)]

#         if DNA1[i] == DNA2[j]:
#             memo[(i, j)] = 1 + lcs(i + 1, j + 1)
#         else:
#             memo[(i, j)] = max(lcs(i + 1, j), lcs(i, j + 1))
        
#         return memo[(i, j)]

#     return lcs(0,0)

def dna_match_topdown(DNA1, DNA2):
    m, n = len(DNA1) - 1, len(DNA2) -1
    memo = {}

    def lcs(i, j):
        if i < 0 or j < 0:
            return 0
        
        if (i, j) in memo:
            return memo [(i, j)]

        if DNA1[i] == DNA2[j]:
            memo[(i, j)] = 1 + lcs(i - 1, j - 1)
        else:
            memo[(i, j)] = max(lcs(i - 1, j), lcs(i, j - 1))
        
        return memo[(i, j)]

    return lcs(m,n)

def dna_match_bottomup(DNA1, DNA2):
    m, n = len(DNA1), len(DNA2)

    cache = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i==0 or j==0:
                cache[i][j] = 0
            elif DNA1[i-1] == DNA2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j]= max(cache[i-1][j] , cache[i][j-1])

    return cache[m][n]

# DNA1 = "TAGTTCCGTCAAA"
# DNA2 = "TGTTCCCGTCAAA"
# print(dna_match_topdown1(DNA1, DNA2))  
# print(dna_match_topdown2(DNA1, DNA2))  
# print(dna_match_bottomup(DNA1, DNA2)) 
