fn maxProfit(prices: &mut Vec<i32>) -> i32{
    let mut min_price: i32 = std::i32::MAX;
    let mut max_price: i32 = 0;

    for price in prices.iter(){
        if *price < min_price {
            min_price = *price
        }

        if *price - min_price > max_price {
            max_price = *price - min_price
        }
    }

    max_price
}

fn main() {
    let mut prices = Vec::from([7,1,5,3,6,4]);
    let mut result = maxProfit(&mut prices);
    println!("{}", result);
}
