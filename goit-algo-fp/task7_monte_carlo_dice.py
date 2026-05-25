
import random
from collections import Counter

import matplotlib.pyplot as plt


def monte_carlo_dice_simulation(rolls=100000):
    sums = []

    for _ in range(rolls):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        sums.append(dice_sum)

    counts = Counter(sums)

    probabilities = {
        total: counts[total] / rolls
        for total in range(2, 13)
    }

    return probabilities


if __name__ == "__main__":
    probabilities = monte_carlo_dice_simulation()

    print("Sum | Probability")
    print("-" * 20)

    for total, probability in probabilities.items():
        print(f"{total:>3} | {probability:.4%}")

    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel("Dice Sum")
    plt.ylabel("Probability")
    plt.title("Monte Carlo Dice Simulation")
    plt.show()
