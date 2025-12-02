# Stochastic Vape Cost Simulator (Monte Carlo)

This project uses **Monte Carlo simulation** to model and compare the long-term cost of different disposable vapes under **random daily usage**. Daily consumption is modeled as a **Poisson process**, and thousands of simulated futures are generated to estimate expected cost curves and uncertainty bands.

The tool is useful for:
- Cost forecasting under randomness
- Comparing competing products under stochastic demand
- Visualizing financial uncertainty over time

---

## Features

- Models **random daily vape usage** using a Poisson distribution
- Simulates **thousands of possible future cost trajectories**
- Computes:
  - Expected total cost over time
  - 90% confidence bands (5th–95th percentile)
- Supports **multiple vape products**
- Generates clean **Matplotlib visualizations**
- Fully object-oriented design

---

## Mathematical Model

Let:
- Daily usage ~ Poisson(λ)
- Each vape has a fixed number of usable "units"
- When remaining capacity ≤ 0, a new vape is purchased

Each simulation tracks:
- Discrete daily consumption
- Capacity depletion
- Random refill timing
- Cumulative cost accumulation


## Technologies Used

- Python 3.10+
- NumPy
- Matplotlib

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/vape-cost-simulator.git
cd vape-cost-simulator
