def counting_sort(L):
    n = len(L)

    pos = [0] * n
    for num in L:
        pos[num] += 1

    num_count = n
    for i in reversed(range(n)):
        pos[i] = num_count - pos[i]
        num_count = pos[i]

    sorted_L = [None] * n
    for i in range(n):
        item = L[i]
        new_idx = pos[item]
        sorted_L[new_idx] = item
        pos[item] += 1

    return sorted_L

if __name__ == "__main__":
    l = [2, 3, 4, 3, 1]
    new_l = counting_sort(l)
    print(new_l)
