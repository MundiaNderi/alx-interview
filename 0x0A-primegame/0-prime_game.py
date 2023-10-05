#!/usr/bin/python3
"""
Given a set of consecutive integers starting from 1 up to and including n, 
they take turns choosing a prime number from the set and removing that number and 
its multiples from the set. The player that cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round. 
"""


def isPrime(num):
    # Return 'True' if n is a prime number. False otherwise
    # Eliminates multiples of 2 and 3
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while 1 * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
        return True


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    """
    def canWin(n):
        # Create a list to store the results of the subproblems
        dp = [False] * (n + 1)

        # Base case: Ben wins when there are no prime numbers left
        dp[0] = False

        # Check all numbers from 1 to n
        for i in range(2, n + 1):
            # If the curent number is prime and there exists a move such that
            # Maria loses, then Ben wins
            for j in range(2, i + 1):
                if isPrime(j) and i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break

        return dp[n]

    # Initialize counters to keep track of wins
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
