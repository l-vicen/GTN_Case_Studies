from egttools.behaviors.pgg_behaviors import PGGOneShotStrategy
from egttools.games import PGG
from egttools.analytical import PairwiseComparison
from egttools.plotting.indicators import plot_gradients
import numpy as np
import matplotlib.pyplot as plt

# Create PGGOneShotStrategy instances
strategy0 = PGGOneShotStrategy(0)
strategy1 = PGGOneShotStrategy(1)
strategies = [strategy0, strategy1]

# Create a PGG game instance
group_size = 2
pgg = PGG(group_size, 10, 1.1, strategies)

# Calculate and print the payoffs
payoffs = pgg.calculate_payoffs()
print("Payoffs:")
print(payoffs)

# Z = 100
# beta = 1
# pop_states = np.arange(0, Z + 1, 1)
# evolver = PairwiseComparison(Z, pgg)
# gradients = np.array([evolver.calculate_gradient_of_selection(beta, np.array([x, Z - x])) for x in range(Z + 1)])

# # Plot the gradients
# plt.figure(figsize=(6, 5))
# plt.plot(gradients[:, 0], marker="o", markersize=5)
# plt.xlabel("Strategy " + str(pgg.strategies_[0].get_action()))
# plt.ylabel("Gradient of selection")
# plt.title("Pairwise Comparison: Gradient of Selection")
# plt.grid(True)
# plt.show()