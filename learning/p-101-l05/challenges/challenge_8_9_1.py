from random import random

region_1 = 87
region_2 = 65
region_3 = 17

win_overall = 0
lose_overall = 0

for i in range(10_000):
    win = 0
    lose = 0
    if random() < region_1:
        win += 1
    else:
        lose += 1
    if random() < region_2:
        win += 1
    else:
        lose += 1
    if random() < region_3:
        win += 1
    else:
        lose += 1

    if win > lose:
        win_overall += 1
    else:
        lose_overall += 1
ratio = lose_overall / win_overall
print(f"Candidate A has {ratio:.1%} chance to win")
print(f"Candidate B has {1 - ratio:.1%} chance to win")


