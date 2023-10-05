#!/usr/bin/python3
"""
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that
number and its multiples from the set. The player that
cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round.
"""


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    """
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * 1 <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def play_round(win):
        maria_turn = True
        while num > 0:
            if is_prime(num):
                return "Maria" if maria_turn else "Ben"
            for i in range(num, 0, -1):
                if is_prime(i):
                    num -= i
                    maria_turn = not maria_turn
                    break

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
