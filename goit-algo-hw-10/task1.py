


from timeit import timeit


COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> dict[int, int]:
  #the greedy algorithm.
  
    if amount < 0:
        raise ValueError("Amount must be non-negative")

    result = {}

    for coin in COINS:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount: int) -> dict[int, int]:
    if amount < 0:
        raise ValueError("Amount must be non-negative")

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for current_amount in range(1, amount + 1):
        for coin in COINS:
            if coin <= current_amount and dp[current_amount - coin] + 1 < dp[current_amount]:
                dp[current_amount] = dp[current_amount - coin] + 1
                last_coin[current_amount] = coin

    result = {}
    current_amount = amount

    while current_amount > 0:
        coin = last_coin[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return dict(sorted(result.items()))


def compare_algorithms(amounts: list[int], repeats: int = 1000) -> None:
    """Compares execution time of both algorithms."""
    print("Coin denominations:", COINS)
    print()

    for amount in amounts:
        greedy_result = find_coins_greedy(amount)
        dp_result = find_min_coins(amount)

        greedy_time = timeit(lambda: find_coins_greedy(amount), number=repeats)
        dp_time = timeit(lambda: find_min_coins(amount), number=repeats)

        print(f"Amount: {amount}")
        print(f"Greedy result: {greedy_result}")
        print(f"Dynamic programming result: {dp_result}")
        print(f"Greedy time for {repeats} runs: {greedy_time:.6f} seconds")
        print(f"DP time for {repeats} runs: {dp_time:.6f} seconds")
        print("-" * 60)


if __name__ == "__main__":
    test_amounts = [113, 999, 10_000]
    compare_algorithms(test_amounts)
