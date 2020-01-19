def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

                   # i  j
arrToSort = [3, 1, 5, 2, 4]
bubble_sort(arrToSort)

print(arrToSort)
