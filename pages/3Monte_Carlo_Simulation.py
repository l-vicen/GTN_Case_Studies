import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import egttools as egt
import networkx as nx

from egttools.behaviors.NormalForm.TwoActions import (Cooperator,Defector, TFT, Pavlov, GRIM, Random)


egt.Random.init()
seed = egt.Random._seed

Z = 1

# Define which strategies can be present in the population
strategies = [Cooperator(), Defector(), TFT(), Pavlov(), Random(), GRIM()]
# define the game
payoffs = np.array([[1, 3],[0, 2]])
game = egt.games.NormalFormGame(100, payoffs, strategies)
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

st.write(fixation_probabilities)

st.write(stationary_distribution)