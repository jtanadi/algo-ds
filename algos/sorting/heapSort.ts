// Heap sort implemented as function outside of data structure
// (no python implementation bc sort() method exists in Heap class)

import MaxHeap from "../../dataStructures/heaps/maxHeap"

function sort<T>(arr: T[]): T[] {
  const heap = new MaxHeap<T>()
  heap.buildMaxHeap(arr)

  const sorted: T[] = []
  while (heap.heapSize()) {
    sorted.push(heap.extractMax())
  }
  return sorted
}

const arrToBeSorted: number[] = [3, 0, -1, 4, 2, 8]
console.log(sort(arrToBeSorted))
