fn maxProfit(prices: &mut Vec<i32>) -> i32{
    let mut total = 0;

    for i in 0..prices.len() - 1{
        if prices[i + 1] - prices[i] > 0 {
            total += prices[i + 1] - prices[i]
        }
    }

    return total;
}

fn main() {
    let mut arr = vec![7,1,5,3,6,4];
    let result = maxProfit(&mut arr);
    println!("{}", result);
}
