# Dictionary Time!
import random


def char_count(string):
    chars = {}
    for c in string:
        chars[c] = chars.get(c, 0) + 1
    return chars


def word_count(string):
    words = {}
    for c in string.split():
        words[c] = words.get(c, 0) + 1
    return words


def random_dices(iters):
    rolls = dict(zip(range(2, 13), [0] * 11))
    for i in range(iters):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        roll = r1 + r2
        """
        if roll not in rolls:
            rolls[roll] = 0
        """
        rolls[roll] += 1
    return rolls


# Examples
print("Count chars of Hello World")
print(char_count("Hello World!"))
print("Count words of Hello World Wonderful World")
print(word_count("Hello World Wonderful World"))
print("Roll 2 dices 100 times!")
print(random_dices(100))
