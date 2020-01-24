const countingSort = (arr: number[]): number[] => {
  const n = arr.length;

  // initialize pos to [0, 0, 0] (length n)
  const pos: number[] = new Array(n).fill(0)

  // arr = [1, 2, 1]
  // pos = [0, 2, 1]
  for (const num of arr) {
    pos[num] += 1
  }

  // count = 3
  // pos = [0, 2, 1]
  // pos' = [0, 0, 2]
  let count: number = n
  for (let i = n - 1; i >= 0; i--) {
    pos[i] = count - pos[i]
    count = pos[i]
  }

  // [1, 2, 1] => [1, 1, 2]
  const sortedArr: number[] = []
  for (const num of arr) {
    const new_idx: number = pos[num]
    sortedArr[new_idx] = num
    pos[num] += 1
  }

  return sortedArr
}

const startArr = [4, 2, 1, 5, 3, 3]
console.log(countingSort(startArr))
