class Insertion {
  private static swap<T>(arr: T[], idxA: number, idxB: number) {
    const temp: T = arr[idxA]
    arr[idxA] = arr[idxB]
    arr[idxB] = temp
  }

  static sort<T>(arr: T[]): void {
    for (let i = 1; i < arr.length; i++) {
      for (let j = i - 1; j >= 0; j--) {
        if (arr[j + 1] < arr[j]) {
          this.swap(arr, j + 1, j)
        } else {
          break
        }
      }
    }
  }
}

function insertionSort<T>(arr: T[]): void {
  for (let i = 1; i < arr.length; i++) {
    for (let j = i - 1; j >= 0; j--) {
      if (arr[j + 1] < arr[j]) {
        const temp: T = arr[j + 1]
        arr[j + 1] = arr[j]
        arr[j] = temp
      } else {
        break
      }
    }
  }
}

const arrToSort1: number[] = [2, 5, 1, 3, -100, -20]
insertionSort(arrToSort1)
console.log(arrToSort1)

const arrToSort2: string[] = ["z", "b", "d", "a", "x"]
Insertion.sort(arrToSort2)
console.log(arrToSort2)
