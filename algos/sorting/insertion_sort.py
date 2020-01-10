"""
In-place insertion sort
"""

def swap(L, idx1, idx2):
    temp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = temp

def insertion_sort(L):
    for i in range(1, len(L)):
        for j in reversed(range(i)):
            # pairwise swap
            if L[j+1] < L[j]:
                swap(L, j+1, j)
            else:
                break
if __name__ == "__main__":
    L1 = [2, 4, 3, 6, 5, 1]
    insertion_sort(L1)

    expected = [1, 2, 3, 4, 5, 6]
    if L1 == expected:
        print("sorted!")
    else:
        print("not sorted!")

    print(", ".join([str(elem) for elem in L1]))
