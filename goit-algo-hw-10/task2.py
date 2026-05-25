

import random

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x: float) -> float:
    """Function to integrate."""
    return x ** 2


def monte_carlo_integral(a: float, b: float, num_points: int = 100_000) -> float:
    total = 0

    for _ in range(num_points):
        x = random.uniform(a, b)
        total += f(x)

    average_value = total / num_points
    return (b - a) * average_value


def plot_function(a: float, b: float) -> None:
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2)

    ix = np.linspace(a, b, 200)
    iy = f(ix)
    ax.fill_between(ix, iy, alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axvline(x=a, linestyle="--")
    ax.axvline(x=b, linestyle="--")
    ax.set_title(f"Integral of f(x) = x^2 from {a} to {b}")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    a = 0
    b = 2
    num_points = 100_000

    monte_carlo_result = monte_carlo_integral(a, b, num_points)
    quad_result, quad_error = spi.quad(f, a, b)

    print(f"Monte Carlo result: {monte_carlo_result}")
    print(f"quad result: {quad_result}")
    print(f"quad error estimate: {quad_error}")
    print(f"Absolute difference: {abs(monte_carlo_result - quad_result)}")

    plot_function(a, b)
