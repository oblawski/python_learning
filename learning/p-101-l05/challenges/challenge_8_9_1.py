from random import random

region_1 = 0.87
region_2 = 0.65
region_3 = 0.17

win_overall = 0
lose_overall = 0
num_trials = 10_000
for i in range(num_trials):
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

ratio = win_overall / num_trials
print(f"Candidate A has {ratio:.1%} chance to win")
print(f"Candidate B has {1 - ratio:.1%} chance to win")


