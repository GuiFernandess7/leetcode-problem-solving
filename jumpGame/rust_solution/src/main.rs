fn canJump(prices: &mut Vec<i32>) -> bool {
    let mut jump_idx = 0;

    for n in prices.iter(){
        if jump_idx < 0 {
            return false;
        }

        if *n > jump_idx {
            jump_idx = *n;
        }

        jump_idx -= 1
    }

    return true;
}

fn main() {
    let mut arr = vec![1,2,1,0,1];
    let result = canJump(&mut arr);
    println!("{}", result);
}
