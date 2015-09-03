"""It's not cgi- it's computer generated dice rolls- cgdr for short
"""

import random
import time

def roll(howmany=1,sides=6):
    """Returns the result from rolling `howmany` of `sides`-sided dice"""
    total = 0
    for count in range(howmany):
        total += random.randint(1,sides)
    return total

def parse(text):
    """Parses traditional dice notation (ex: 3d6)"""
    howmany, sides = text.split('d')
    return (int(howmany), int(sides))

def parse_roll(text):
    """parses traditional dice notation and then rolls (ex: 3d6)"""
    howmany, sides =parse(text)
    return roll(howmany,sides)

if __name__ == '__main__':
    import colors as c
    while True:
        print(roll())
        time.sleep(0.5)
