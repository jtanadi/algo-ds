function inPlaceBubble<T>(arr: T[]): void {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] > arr[j]) {
        const temp: T = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
      }
    }
  }
}

function outOfPlaceBubble<T>(arr: T[]): T[] {
  const sortedArr: T[] = [...arr]
  inPlaceBubble(sortedArr)
  return sortedArr
}

const arrToSort1: number[] = [3, 2, 5, 1, 4]
inPlaceBubble(arrToSort1)
console.log(arrToSort1) // [1, 2, 3, 4, 5]

const arrToSort2: number[] = [5, -1, -3, 100, 2]
console.log(outOfPlaceBubble(arrToSort2)) // [-3, -1, 2, 5, 100]
