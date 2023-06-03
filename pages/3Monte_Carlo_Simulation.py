import numpy as np
import matplotlib.pyplot as plt
import egttools as egt
import streamlit as st
from egttools.behaviors.NormalForm.TwoActions import (Cooperator, Defector, Random)
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

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
st.markdown("### Evolver")
st.write(evolver)

transition_matrix, fixation_probabilities = evolver.calculate_transition_and_fixation_matrix_sml(beta)

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
                                              ax=ax)
plt.axis('off')
st.pyplot(fig)


V = 2; D = 3; T = 1
B = np.array([
        [ (V-D)/2, V],
        [ 0      , (V/2) - T],
    ])

st.markdown("### Numerical Evolver")
x = np.arange(0, Z+1)/Z
gameTwo = egt.games.NormalFormGame(100, B, strategies)
evolverNumerical = egt.numerical.PairwiseComparisonNumerical(Z, gameTwo, 100)
st.write(evolverNumerical)

dist = evolverNumerical.estimate_stationary_distribution(10, int(1e6), int(1e3), 1, 1e-3)

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
