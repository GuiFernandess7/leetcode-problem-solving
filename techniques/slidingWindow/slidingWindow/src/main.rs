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

fn minArraySizeFromSum(target: i32, nums: Vec<i32>) -> i32 {
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

fn main() {
    let mut nums = vec![15, 7, 31, 30, 21, 22, 19, 17, 24, 27, 50, 26, 33, 6, 22, 17, 42, 21, 17, 37, 49, 31, 37];
    let mut maxSubset = maxSubsetSum(&mut nums, 3 as usize);
    let mut minSubset = minArraySizeFromSum(59, nums);
    println!("{}", minSubset);
}
