// Max heap, structured as an array and visually
// represented as a nearly-complete binary tree
//
// [null, 32, 25, 23, 19, 20]
// [  0 ,  1,  2,  3,  4,  5]
//
// parent = Math.floor(i / 2)
// leftChild = i * 2
// rightChild = i * 2 + 1

class MaxHeap<T> {
  container: Array<T>

  constructor() {
    this.container = [null]
  }

  private swap(idxA: number, idxB: number): void {
    const temp: T = this.container[idxA]
    this.container[idxA] = this.container[idxB]
    this.container[idxB] = temp
  }

  heapSize(): number {
    // Heap size is always 1 less than length because
    // first item of container array is null
    return this.container.length - 1
  }

  max(): T {
    try {
      return this.container[1]
    } catch (e) {
      throw new Error("Nothing in this heap yet")
    }
  }

  bottomUpMaxHeapify(idx: number): void {
    const parentIdx: number = Math.floor(idx / 2)
    if (idx > 1 && this.container[idx] > this.container[parentIdx]) {
      this.swap(idx, parentIdx)
      this.bottomUpMaxHeapify(parentIdx)
    }
  }

  topDownMaxHeapify(idx: number): void {
    let largestIdx: number = idx
    let leftIdx: number = idx * 2
    let rightIdx: number = idx * 2 + 1

    // Inside of bounds check
    if (leftIdx <= this.heapSize() && this.container[leftIdx] > this.container[largestIdx]) {
      largestIdx = leftIdx
    }

    // Inside of bounds check
    if (rightIdx <= this.heapSize() && this.container[rightIdx] > this.container[largestIdx]) {
      largestIdx = rightIdx
    }

    if (largestIdx !== idx) {
      this.swap(idx, largestIdx)
      this.topDownMaxHeapify(largestIdx)
    }
  }

  insert(val: T): void {
    // Push to end of container, then swim up
    // until it's in the correct place
    this.container.push(val)
    let n = this.heapSize()
    this.bottomUpMaxHeapify(n)
  }

  serialize(): string {
    return this.container.slice(1).join("-")
  }
}

const mh = new MaxHeap()
mh.insert(4)
mh.insert(3)
mh.insert(8)
console.log(mh.serialize())
