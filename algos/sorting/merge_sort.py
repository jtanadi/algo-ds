"""
Not-in-place merge sort
merge_sort() returns sorted array
"""

def merge(L1, L2):
    """
    L1 and L2 are both sorted

    L1 = [1, 2, 5]
    L2 = [3, 4, 6]
    """

    i = 0
    j = 0
    merged = []

    # two-finger algo for merging two arrays into one,
    # from smallest to largest
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            merged.append(L2[j])
            j += 1
        else:
            merged.append(L1[i])
            merged.append(L2[j])
            i += 1
            j += 1

    # If there are leftovers in either array,
    # just push those remaining elements into merged array,
    # since both input arrays are already sorted
    if i < len(L1):
        merged.extend(L1[i:])
    elif j < len(L2):
        merged.extend(L2[j:])

    return merged

def merge_sort(L):
    if len(L) <= 1:
        return L
    else:
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        return merge(sorted_left, sorted_right)

if __name__ == "__main__":
    L1 = [2, 4, 3, 6, 5, 1]
    L2 = merge_sort(L1)

    expected = [1, 2, 3, 4, 5, 6]
    if L2 == expected:
        print("sorted!")
    else:
        print("not sorted!")

    print(", ".join([str(elem) for elem in L2]))
