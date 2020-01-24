def counting_sort(L):
    """
    Works only for positive integer keys
    0 to k-1
    
    Time complexity: O(n + k)
    n is length of L
    k is number of keys (ie. length of `pos`)
    """
    n = len(L)

    pos = [0] * n
    for num in L:
        pos[num] += 1

    num_count = n
    for i in reversed(range(n)):
        pos[i] = num_count - pos[i]
        num_count = pos[i]

    sorted_L = [None] * n
    for item in L:
        new_idx = pos[item]
        sorted_L[new_idx] = item
        pos[item] += 1

    return sorted_L

if __name__ == "__main__":
    l = [2, 3, 4, 3, 1]
    new_l = counting_sort(l)
    print(new_l)
