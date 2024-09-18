def kthElement(Arr1, Arr2, k):
    """
    This function will return the kth element in a combined sorted array
    by utilizing a divide and conquer technique.
    """
    if len(Arr1) == 0:
        return Arr2[k - 1]
    if len(Arr2) == 0:
        return Arr1[k - 1]
    if k == 1:
        return min(Arr1[0], Arr2[0])

    # Calculate indices to search k//2 elements in each array
    i = min(len(Arr1), k//2)
    j = min(len(Arr2), k//2)

    # Discard whichever set of k//2 elements are smaller and reduce k
    if Arr1[i - 1] < Arr2[j - 1]:
        return kthElement(Arr1[i:], Arr2, k - i)
    else:
        return kthElement(Arr1, Arr2[j:], k - j)
