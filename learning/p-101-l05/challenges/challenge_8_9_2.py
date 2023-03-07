from random import random


def run_regional_election(chance_A_win):
    """checking if candidate won in a region"""
    if random() < chance_A_win:
        return "A"
    else:
        return "B"


def run_election(regional_chances):
    """checking whether candidate won in majority regions"""
    num_regions_won_by_A = 0
    for chance_A_win in regional_chances:
        if run_regional_election(chance_A_win) == "A":
            num_regions_won_by_A += 1

    num_regions_won_by_B = len(regional_chances) - num_regions_won_by_A
    if num_regions_won_by_A > num_regions_won_by_B:
        return "A"
    else:
        return "B"


CHANCES_A_WINS_BY_REGION = [0.87, 0.65, 0.17]
NUM_TRIALS = 10_000
num_times_A_wins = 0
for i in range(NUM_TRIALS):
    if run_election(CHANCES_A_WINS_BY_REGION) == "A":
        num_times_A_wins += 1

print(f"Candidate A has {num_times_A_wins/NUM_TRIALS:.1%} chances to win")
print(f"Candidate B has {1 - num_times_A_wins/NUM_TRIALS:.1%} chances to win")