function merge<T>(left: Array<T>, right: Array<T>): Array<T> {
  let i: number = 0
  let j: number = 0
  const merged: Array<T> = []

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      merged.push(left[i])
      i++
    } else {
      merged.push(right[j])
      j++
    }
  }

  while (i < left.length) {
    merged.push(left[i])
    i++
  }

  while (j < right.length) {
    merged.push(right[j])
    j++
  }

  return merged
}

function mergeSort<T>(arr: Array<T>): Array<T> {
  if (arr.length <= 1) {
    return arr
  }

  const midIdx: number = Math.floor(arr.length / 2)
  const leftArr: Array<T> = arr.slice(0, midIdx)
  const rightArr: Array<T> = arr.slice(midIdx)

  return merge(mergeSort(leftArr), mergeSort(rightArr))
}

const arrToSort: number[] = [2, 1, 5, 20, -1, 80]
console.log(mergeSort(arrToSort))
