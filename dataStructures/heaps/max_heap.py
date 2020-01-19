class MaxHeap(object):
    def __init__(self):
        """
        Initialize empty heap array with None in 0th idx
        so our arithmetic will be easier later
        (real values start at 1st idx)
        """
        self.heap_array = [None]

    def _swap(self, idx_a, idx_b):
        """
        Swap values of two indices
        """
        temp = self.heap_array[idx_a]
        self.heap_array[idx_a] = self.heap_array[idx_b]
        self.heap_array[idx_b] = temp

    def heap_size(self):
        """
        Convenience method
        Heap size doesn't include first element (None)
        """
        return len(self.heap_array) - 1

    def max(self):
        """
        Convenience method
        """
        return self.heap_array[1]

    def insert(self, value):
        """
        Insert new value by adding to end of heap
        then swimming value into place as necessary

        Time complexity: O(log n)

        >>> L4 = [4, 2, 1]
        >>> heap4 = MaxHeap()
        >>> heap4.build_max_heap(L4)
        >>> print(heap4.heap_array)
        [None, 4, 2, 1]

        >>> heap4.insert(5)
        >>> print(heap4.heap_array)
        [None, 5, 4, 1, 2]

        >>> heap4.insert(3)
        >>> print(heap4.heap_array)
        [None, 5, 4, 1, 2, 3]
        """
        self.heap_array.append(value)
        n = self.heap_size()
        self.bottom_up_max_heapify(n)

    def extract_max(self):
        """
        Extract max value by swapping with last element
        and then "swimming" next largest item to top

        Time complexity: O(log n)
        """
        self._swap(1, self.heap_size())
        ret_val = self.heap_array.pop()

        # In case the array is empty after pop()
        if self.heap_size() >=1 :
            self.top_down_max_heapify(1)

        return ret_val

    def sort(self, input_array):
        """
        Max heap sort by building a max heap
        and calling extract_max() until heap is empty

        Time complexity: O(n log n)
        """
        self.build_max_heap(input_array)

        sorted_array = []
        while self.heap_size():
            sorted_array.append(self.extract_max())

        return sorted_array

    def build_max_heap(self, input_array):
        """
        Builds a max heap out of an unordered array

        Time complexity (simple analysis): O(n log n)
        Time complexity (tighter analysis): O(n)

        >>> L1 = [4, 3, 1, 6, 5, 2]
        >>> heap1 = MaxHeap()
        >>> heap1.build_max_heap(L1)
        >>> print(heap1.heap_array)
        [None, 6, 5, 2, 3, 4, 1]

        heap_array = [None, 4, 3, 1, 6, 5, 2]
        heap_size  = 6
        n // 2 = 3

            0  1  2  3  4  5  6
        [None, 4, 3, 1, 6, 5, 2]
        heap_array[3] = 1

            4
         3     1
        6 5   2
        """
        self.heap_array.extend(input_array)
        n = len(input_array)

        # range goes up to but not including max
        # [1, 2, ...n)
        # if n = 6, n // 2 + 1 = 4
        # range(1, 4) = 1, 2, 3; reversed = 3, 2, 1
        for i in reversed(range(1, n // 2 + 1)):
            self.top_down_max_heapify(i)

    def bottom_up_max_heapify(self, i):
        """
        Bottom-up approach of creating a max heap
        starting at node `i`, up to root

        Time complexity: O(log n)
        """
        if i > 1:
            parentIdx = i // 2
            if self.heap_array[i] > self.heap_array[parentIdx]:
                self._swap(i, parentIdx)

            self.bottom_up_max_heapify(parentIdx)

    def top_down_max_heapify(self, i):
        """
        Top-down approach of creating a max heap
        starting at node `i`, down to leaf

        Time complexity: O(log n)
        """
        largest_idx = i
        left_idx = i * 2
        right_idx = i * 2 + 1

        # make sure not out of bounds
        if left_idx <= self.heap_size() and\
            self.heap_array[left_idx] > self.heap_array[largest_idx]:
                largest_idx = left_idx

        # make sure not out of bounds
        if right_idx <= self.heap_size() and\
            self.heap_array[right_idx] > self.heap_array[largest_idx]:
                largest_idx = right_idx

        if largest_idx != i:
            self._swap(i, largest_idx)

            # recurse to swapped child to make sure
            # max heap property isn't violated down the line
            # (largest_idx is no longer the largest post-swap)
            self.top_down_max_heapify(largest_idx)


if __name__ == "__main__":
    import doctest, random
    doctest.testmod()

    L1 = [4, 3, 1, 6, 5, 2]
    heap1 = MaxHeap()
    heap1.build_max_heap(L1)
    print(heap1.heap_array)

    L2 = [3, 2, 5, 1, 4, 6]
    heap2 = MaxHeap()
    sorted_L2 = heap2.sort(L2)
    print("sorted", sorted_L2)

    # L3 = []
    # for i in range(10000):
    #     num = random.randint(0, i)
    #     L3.append(num)

    # heap3 = MaxHeap()
    # sorted_L3 = heap3.sort(L3)
    # print("sorted", sorted_L3)

    L4 = [4, 2, 1]
    heap4 = MaxHeap()
    heap4.build_max_heap(L4)
    print("heap4 pre", heap4.heap_array)

    heap4.insert(5)
    print("heap4 with 5 inserted", heap4.heap_array)

    heap4.insert(3)
    print("heap4 with 3 inserted", heap4.heap_array)
