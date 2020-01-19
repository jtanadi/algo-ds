// Max heap, structured as an array and visually
// represented as a nearly-complete binary tree
//
// [null, 32, 25, 23, 19, 20]
// [  0 ,  1,  2,  3,  4,  5]
//
// parent = Math.floor(i / 2)
// leftChild = i * 2
// rightChild = i * 2 + 1

class MaxHeap {
  container: Array<number>

  constructor() {
    this.container = [null]
  }

  swap(idxA: number, idxB: number): void {
    const temp = this.container[idxA]
    this.container[idxA] = this.container[idxB]
    this.container[idxB] = temp
  }

  heapSize(): number {
    return this.container.length - 1
  }

  max(): number {
    try {
      return this.container[1]
    } catch (e) {
      throw new Error("Nothing in this heap yet")
    }
  }

  maxHeapify(idx: number): void {
    let current: number = this.container[idx]
    let leftIdx: number = idx * 2
    let rightIdx: number = idx * 2 + 1
    let largestIdx: number = idx

    let leftChild: number = null
    let rightChild: number = null

    // Inside of bounds check
    if (leftIdx <= this.heapSize()) {
      leftChild = this.container[leftIdx]
      if (leftChild > current) {
        largestIdx = leftIdx
      }
    }

    // Inside of bounds check
    if (rightIdx <= this.heapSize()) {
      rightChild = this.container[rightIdx]

      if (rightChild > this.container[largestIdx]) {
        largestIdx = rightIdx
      }
    }

    if (largestIdx !== idx) {
      this.swap(idx, largestIdx)
      this.maxHeapify(largestIdx)
    }
  }

  insert(val: number): void {
    // Push to end of container, then swim up
    // until it's in the correct place
    this.container.push(val)
    let n = this.heapSize()

    while (n > 0) {
      this.maxHeapify(n)
      n = Math.floor(n / 2)
    }
  }



}
