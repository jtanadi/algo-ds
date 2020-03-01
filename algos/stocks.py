def get_max_profit(prices):
    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for i in range(1, len(prices)):
        price = prices[i]

        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

        if price < min_price:
            min_price = price


    return max_profit


if __name__ == "__main__":
    print(get_max_profit([10, 7, 5, 8, 11, 9])) # 6, from 11 - 5
    print(get_max_profit([10, 9, 7, 5, 2, -1])) # -1, from 10 - 9
