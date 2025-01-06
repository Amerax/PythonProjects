import numpy as np
import matplotlib.pyplot as plt

# Data from the experiment (inhibition zones in cm)
data = {
    "Control": [0, 0, 0, 0, 0, 0],
    "Ampicillin": [1.9, 1.6, 1.8, 1.9, 1.7, 1.6],
    "Kanamycin": [2.6, 2.5, 2.4, 2.4, 2.4, 2.6],
    "Tetracycline": [3.1, 2.9, 3.0, 2.8, 3.0, 3.0]
}

# Simulate random variations (Monte Carlo simulation)
simulations = 10000  # Number of Monte Carlo runs
results = {}

for antibiotic, zones in data.items():
    mean = np.mean(zones)
    std_dev = np.std(zones)
    simulated_zones = np.random.normal(mean, std_dev, simulations)
    results[antibiotic] = simulated_zones

# Plot distributions
for antibiotic, simulated_zones in results.items():
    plt.hist(simulated_zones, bins=50, alpha=0.6, label=antibiotic)

plt.title("Monte Carlo Simulation of Inhibition Zones")
plt.xlabel("Inhibition Zone Size (cm)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Calculate confidence intervals
for antibiotic, simulated_zones in results.items():
    lower_ci = np.percentile(simulated_zones, 2.5)
    upper_ci = np.percentile(simulated_zones, 97.5)
    print(f"{antibiotic} 95% Confidence Interval: {lower_ci:.2f} - {upper_ci:.2f}")
