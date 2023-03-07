import random


def flip_coin():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


flips = 0
trial = 10000
for i in range(10_000):
    if flip_coin() == "heads":
        flips += 1
        while flip_coin() == "heads":
            flips += 1
        flips += 1

    else:
        flips += 1
        while flip_coin() == "tails":
            flips += 1
        flips += 1
print(f"There were needed {flips/trial} flips on average for the sequence to contain both")

