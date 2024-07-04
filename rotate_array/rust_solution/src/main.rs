// https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

struct Solution;

impl Solution {
    pub fn reverse(nums: &mut Vec<i32>, mut low: usize, mut high: usize) {
        while low < high {
            let mut temp = nums[low];
            nums[low] = nums[high];
            nums[high] = temp;
            low += 1;
            high -= 1;
        }
    }

    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let k = k as usize % nums.len();
        let n = nums.len();
        if k > 0 {
            Solution::reverse(nums, 0, n - 1);
            Solution::reverse(nums, 0, k - 1);
            Solution::reverse(nums, k, n - 1);
        }
    }
}

fn main(){
    let mut my_vec: Vec<i32> = Vec::from([1, 2, 3, 4, 5, 6, 7]);
    let k = 3;
    Solution::rotate(&mut my_vec, k);
    println!("{:?}", my_vec);
}
