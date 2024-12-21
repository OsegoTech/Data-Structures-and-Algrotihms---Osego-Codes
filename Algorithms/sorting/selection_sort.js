function find_smallest(arr) {
  let smallest_element = arr[0];
  let smallest_index = 0;

  for (let index = 1; index < arr.length; index++) {
    if (arr[index] < smallest_element) {
      smallest_element = arr[index];
      smallest_index = index;
    }
  }
  return smallest_index;
}

console.log(find_smallest([5, 3, 6, 2, 10]));

function selection_sort(arr) {
  let sorted_arr = [];
  let arr_length = arr.length;

  for (let i = 0; i < arr_length; i++) {
    let smallest_index = find_smallest(arr);
    sorted_arr.push(arr.splice(smallest_index, 1)[0]);
  }
  return sorted_arr;
}

console.log(selection_sort([5, 3, 6, 2, 10]));
