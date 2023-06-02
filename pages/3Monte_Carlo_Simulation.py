import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import egttools as egt
import networkx as nx

# egt.Random.init()
# seed = egt.Random._seed

# st.markdown("# Monte Carlo Simulation")

# strategies = [egt.behaviors.NormalForm.TwoActions.Cooperator(), 
#               egt.behaviors.NormalForm.TwoActions.Defector(), 
#               egt.behaviors.NormalForm.TwoActions.Random()]

# T=4; R=2; P=1; S=0
# A = np.array([
#     [P, T],
#     [S, R]
# ])

# strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]
# st.write(strategy_labels)

# game = egt.games.NormalFormGame(100, A, strategies)
# st.write(game)

# Z= 100; beta=1
# evolver = egt.analytical.PairwiseComparison(Z, game, 1000)
# st.write(evolver)

# transition_matrix,fixation_probabilities = evolver.calculate_transition_and_fixation_matrix_sml(beta)
# st.write("### Transition Matrix")
# st.write(transition_matrix)

# st.markdown("### Fixation Probabilities")
# st.write(fixation_probabilities)

# stationary_distribution = egt.utils.calculate_stationary_distribution(transition_matrix.transpose())
# st.markdown("### Stationary Distribution")
# st.write(stationary_distribution)

# G = egt.plotting.draw_invasion_diagram([strategy.type().replace(”NFGStrategies:”, ”) for strategy in strategies], 1/Z, fixation_probabilities, stationary_distribution)

from egttools.behaviors.NormalForm.TwoActions import (Cooperator,Defector, TFT, Pavlov, GRIM, Random)

Z = 10000
beta = 1.0

# Define which strategies can be present in the population
strategies = [Cooperator(), Defector(), Random()]

# Define the game
payoffs = np.array([[1, 3],[0, 2]])
game = egt.games.NormalFormGame(100000, payoffs, strategies)

# Define the parameters of the population and instantiate the evolver
evolver = egt.analytical.PairwiseComparison(Z, game)

# Calculate the transition and fixation probabilities and the stationary distribution
transition_matrix,fixation_probabilities = evolver.calculate_transition_and_fixation_matrix_sml(beta)
stationary_distribution = egt.utils.calculate_stationary_distribution(transition_matrix)

# Plot the invasion diagram
G = egt.plotting.draw_invasion_diagram([strategy.type().replace("NFGStrategies:", "") for strategy in
strategies], 1/Z, fixation_probabilities, stationary_distribution)
fig, ax = plt.subplots()
pos = nx.kamada_kawai_layout(G)
nx.draw(G,pos, with_labels=True)
st.pyplot(fig)