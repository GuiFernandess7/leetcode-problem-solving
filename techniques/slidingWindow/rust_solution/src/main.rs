use std::collections::HashMap;

fn maxSubsetSum(nums: &mut Vec<i32>, k: usize) -> i32 {
    /* Calculates the maximum sum of a subarray of length `k` in the given vector `nums`.

    Args:
    - nums: A mutable reference to a vector of integers.
    - k: The length of the subarray for which to find the maximum sum.

    Returns:
    - The maximum sum found among all subarrays of length `k`. */

    let mut current_sum = 0;
    let mut max_value = i32::MIN;

    for i in 0..nums.len(){
        current_sum += nums[i];

        if i >= k + 1 {
            max_value = max_value.max(current_sum);
            current_sum -= nums[i - (k + 1)]
        }
    }

    return max_value;
}

fn min_array_size_from_sum(target: i32, nums: Vec<i32>) -> i32 {
    /* Calculates the minimum size of a subarray whose sum is at least a target value.

    This function iterates through the `nums` vector and uses a sliding window approach to find
    the smallest subarray size where the sum of elements is at least `target`.

    Args:
    - `target`: The target value that the sum of the subarray must reach or exceed.
    - `nums`: A vector of integers from which we are searching for the subarray.

    Returns:
    - The minimum size of the subarray whose sum is greater than or equal to `target`. Returns 0
    if no valid subarray size is found. */

    let mut min_arr_size = i32::MAX;
    let mut window_start = 0;
    let mut window_sum = 0;

    for i in 0..nums.len(){
        window_sum += nums[i];

        while window_sum >= target {
            min_arr_size = min_arr_size.min((i - window_start + 1) as i32);
            window_sum -= nums[window_start];
            window_start += 1;
        }
    }

    return min_arr_size;
}

fn fruits_into_basket(fruits: Vec<usize>) -> i32 {
    let mut max_fruits = 0;
    let mut seen: HashMap<usize, i32> = HashMap::new();
    let mut start = 0;
    let mut current_counter = 0;

    for end in 0..fruits.len(){
        let fruit_value = fruits[end];
        if let Some(value) = seen.get_mut(&fruit_value){
            *value += 1;
        } else {
            seen.insert(fruit_value, 1);
        }
        current_counter += 1;

        while fruits.len() < 2{
            let left_fruit_value = fruits[start];
            if let Some(counter) = seen.get_mut(&left_fruit_value){
                *counter -= 1;
                current_counter += 1;
                if *counter == 0 {
                    seen.remove(&left_fruit_value);
                }
            }
            start += 1
        }

        max_fruits = max_fruits.max(current_counter);
    }

    return max_fruits;
}


fn main() {
    //let nums = vec![15, 7, 31, 30, 21, 22, 19, 17, 24, 27, 50, 26, 33, 6, 22, 17, 42, 21, 17, 37, 49, 31, 37];
    let fruits = vec![1, 2, 1];
    //let mut max_subset = maxSubsetSum(&mut nums, 3 as usize);
    //let min_subset = min_array_size_from_sum(59, nums);
    let max_fruits = fruits_into_basket(fruits);
    println!("{}", max_fruits);
}
