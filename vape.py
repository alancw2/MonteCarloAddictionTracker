import numpy as np
from matplotlib import pyplot as plt


class Vape:
    def __init__(self, name: str, price: float, days_of_use: int, initial_cost: float):
        self.name = name # name of the vape brand/model
        self.price = price # cost to replace/refill vape
        self.days_of_use = days_of_use # number of days one vape lasts
        self.initial_cost = initial_cost # initial cost of the vape device


def simulate_one_random_cost_path(vape: Vape, total_days: int, lam=0.25): 
    cost = vape.initial_cost
    total_costs = []
    remaining_juice = vape.days_of_use

    for _ in range(total_days):
        daily_uses = np.random.poisson(lam=lam)
        remaining_juice -= daily_uses

        if remaining_juice <= 0:
            cost += vape.price # add the cost of a new vape or refill
            remaining_juice = vape.days_of_use # sets the vape to full juice (i.e. all days of use available)

        total_costs.append(cost) 

    return np.array(total_costs)


def monte_carlo_simulation(vape: Vape, total_days: int, num_simulations: int = 1000):
    all_paths = []

    for _ in range(num_simulations):
        path = simulate_one_random_cost_path(vape, total_days)
        all_paths.append(path)

    return np.array(all_paths)   # shape: (num_simulations, total_days)


def plot_average_cost_curves(vapes: list[Vape], total_days: int, num_simulations: int = 1000):
    days = np.arange(1, total_days + 1)
    plt.figure(figsize=(10, 6))

    for vape in vapes:
        all_paths = monte_carlo_simulation(vape, total_days, num_simulations)

        average_curve = np.mean(all_paths, axis=0)
        lower_band = np.percentile(all_paths, 5, axis=0)
        upper_band = np.percentile(all_paths, 95, axis=0)

        plt.plot(days, average_curve, label=f"{vape.name} (Avg)")
        plt.fill_between(days, lower_band, upper_band, alpha=0.25)

    plt.title("Expected Vape Cost Over Time")
    plt.xlabel("Days")
    plt.ylabel("Total Cost ($)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    vuse = Vape(name="Vuse", price=10.0, days_of_use=4, initial_cost=20.0)
    geek_italy = Vape(name="Geek Italy", price=30.0, days_of_use=7, initial_cost=0.0)
    geek_bar = Vape(name="Geekbar", price=35.0, days_of_use=7, initial_cost=0.0)

    vapes = [vuse, geek_italy, geek_bar]

    plot_average_cost_curves(vapes, total_days=100, num_simulations=2000)
