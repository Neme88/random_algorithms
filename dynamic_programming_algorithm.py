# Dynamic Programming: Coin Change Problem
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
# Example usage:
coins = [1, 2, 5]
amount = 11
print(f"Minimum coins needed: {coin_change(coins, amount)}")
