def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivotIdx = len(arr) - 1
    startIdx = 0

    while startIdx < pivotIdx:
        if arr[startIdx] > arr[pivotIdx]:
            temp = arr[startIdx]
            arr[startIdx] = arr[pivotIdx-1]
            arr[pivotIdx-1] = arr[pivotIdx]
            arr[pivotIdx] = temp
        else:
            startIdx += 1

    # sort left of pivot & right of pivot recursively
    arr[:pivotIdx] = quick_sort(arr[:pivotIdx])
    arr[pivotIdx+1:] = quick_sort(arr[pivotIdx+1:])

    return arr

if __name__ == "__main__":
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print(quick_sort(test))

