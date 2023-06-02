import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import egttools as egt
import networkx as nx

egt.Random.init()
seed = egt.Random._seed

T=4; R=2; P=1; S=0
A = np.array([
    [P, T],
    [S, R]
])

strategies = [egt.behaviors.NormalForm.TwoActions.Cooperator(), 
              egt.behaviors.NormalForm.TwoActions.Defector(), 
              egt.behaviors.NormalForm.TwoActions.TFT(),
              egt.behaviors.NormalForm.TwoActions.Pavlov(), 
              egt.behaviors.NormalForm.TwoActions.Random(), 
              egt.behaviors.NormalForm.TwoActions.GRIM()]

strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]
st.write(strategy_labels)

game = egt.games.NormalFormGame(100, A, strategies)

Z= 100; beta=1
evolver = egt.analytical.PairwiseComparison(Z, game)

transition_matrix,fixation_probabilities = evolver.calculate_transition_and_fixation_matrix_sml(beta)
stationary_distribution = egt.utils.calculate_stationary_distribution(transition_matrix.transpose())

# Plot the invasion diagram
fig, ax = plt.subplots(figsize=(5, 5), dpi=150)
G = egt.plotting.draw_invasion_diagram(strategy_labels,
                                              1/Z, fixation_probabilities, stationary_distribution,
                                              node_size=600, 
                                              font_size_node_labels=8,
                                              font_size_edge_labels=8,
                                              font_size_sd_labels=8,
                                              edge_width=1,
                                              min_strategy_frequency=0.00001, 
                                              ax=ax)
plt.axis('off')
# plt.show() # display
st.pyplot(fig)

# fig, ax = plt.subplots()
# pos = nx.kamada_kawai_layout(G)
# nx.draw(G,pos, with_labels=True)
# st.pyplot(fig)