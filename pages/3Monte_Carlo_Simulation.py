import numpy as np
import matplotlib.pyplot as plt
import egttools as egt
import streamlit as st
from egttools.behaviors.NormalForm.TwoActions import (Cooperator, Defector, Random)

egt.Random.init()
seed = egt.Random._seed

A = np.array([
    [1, -1, -0.5],
    [0, -1, -0.5],
    [1,-1,-0.5]
])

strategies = [egt.behaviors.NormalForm.TwoActions.Cooperator(),
              egt.behaviors.NormalForm.TwoActions.Defector(),
              egt.behaviors.NormalForm.TwoActions.Random()]

strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]

game = egt.games.NormalFormGame(100, A, strategies)

Z= 100; beta=1
evolver = egt.analytical.PairwiseComparison(Z, game)
st.write(evolver)

transition_matrix,fixation_probabilities = evolver.calculate_transition_and_fixation_matrix_sml(beta)

st.markdown("### Transformation Matrix")
st.write(transition_matrix)

st.markdown("### Fixation Probabilities")
st.write(fixation_probabilities)

stationary_distribution = egt.utils.calculate_stationary_distribution(transition_matrix.transpose())
st.markdown("### Stationary Distribution")
st.write(stationary_distribution)

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
st.pyplot(fig)
