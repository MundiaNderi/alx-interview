#!/usr/bin/python3


def makeChange(coins, total):
    """
    Return: 
    fewest number of coins needed to meet total
    If total is 0 or less, return 0
    """
    if total < 1:
        return 0

    # Initialize a list to store the minimum number of coins needed for each value from 0 to total
    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    # Iterate through each coin and update the dp list
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
