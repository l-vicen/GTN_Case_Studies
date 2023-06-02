import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import egttools as egt
import networkx as nx


egt.Random.init()
seed = egt.Random._seed

# Payoff matrix
V = 2; D = 3; T = 1
A = np.array([
        [ (V-D)/2, V],
        [ 0      , (V/2) - T],
    ])

strategies = [egt.behaviors.NormalForm.TwoActions.Cooperator(), 
              egt.behaviors.NormalForm.TwoActions.Defector()]

strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]
st.write(strategy_labels)

game = egt.games.NormalFormGame(A, strategies)
st.write(game)

Z = 100
x = np.arange(0, Z+1)/Z
evolver = egt.numerical.PairwiseComparisonNumerical(Z, game, 1000000)
Z = 100
x = np.arange(0, Z+1)/Z
evolver.pop_size = Z

dist = evolver.estimate_stationary_distribution(10, int(1e6), int(1e3), 1, 1e-3)

# We need to reverse, since in this case we are starting from the case
# where the number of Haws is 100%, because of how we map states
fig, ax = plt.subplots(figsize=(5, 4))
fig.patch.set_facecolor('white')
lines = ax.plot(x, list(reversed(dist)))
plt.setp(lines, linewidth=2.0)
ax.set_ylabel('stationary distribution',size=16)
ax.set_xlabel('$k/Z$',size=16)
ax.set_xlim(0, 1)
st.pyplot(fig)

# Z= 100; beta=1
# evolver = egt.analytical.PairwiseComparison(Z, game)

# transition_matrix,fixation_probabilities = evolver.calculate_transition_and_fixation_matrix_sml(beta)
# stationary_distribution = egt.utils.calculate_stationary_distribution(transition_matrix.transpose())

# # Plot the invasion diagram
# fig, ax = plt.subplots(figsize=(5, 5), dpi=150)
# G = egt.plotting.draw_invasion_diagram(strategy_labels,
#                                               1/Z, fixation_probabilities, stationary_distribution,
#                                               node_size=600, 
#                                               font_size_node_labels=8,
#                                               font_size_edge_labels=8,
#                                               font_size_sd_labels=8,
#                                               edge_width=1,
#                                               min_strategy_frequency=0.00001, 
#                                               ax=ax)
# plt.axis('off')
# # plt.show() # display
# st.pyplot(fig)

# # fig, ax = plt.subplots()
# # pos = nx.kamada_kawai_layout(G)
# # nx.draw(G,pos, with_labels=True)
# # st.pyplot(fig)