
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    ratio_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True,
    )

    total_cost = 0
    total_calories = 0
    chosen = []

    for item, data in ratio_items:
        if total_cost + data["cost"] <= budget:
            chosen.append(item)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return chosen, total_cost, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = names[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(
                    dp[i - 1][b],
                    dp[i - 1][b - cost] + calories,
                )
            else:
                dp[i][b] = dp[i - 1][b]

    chosen = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item = names[i - 1]
            chosen.append(item)
            b -= items[item]["cost"]

    total_cost = sum(items[item]["cost"] for item in chosen)
    total_calories = sum(items[item]["calories"] for item in chosen)

    return chosen, total_cost, total_calories


if __name__ == "__main__":
    budget = 100

    print("Greedy algorithm:")
    print(greedy_algorithm(items, budget))

    print()

    print("Dynamic programming:")
    print(dynamic_programming(items, budget))
