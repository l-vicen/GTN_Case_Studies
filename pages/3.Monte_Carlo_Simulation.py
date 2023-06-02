import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import egttools as egt

st.markdown("# Monte Carlo Simulation")

strategies = [egt.behaviors.NormalForm.TwoActions.Cooperator(), 
              egt.behaviors.NormalForm.TwoActions.Defector(), 
              egt.behaviors.NormalForm.TwoActions.Random()]

T=4; R=2; P=1; S=0
A = np.array([
    [P, T, P],
    [S, R, S],
    [T, S, T]
])

strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]
st.write(strategy_labels)

game = egt.games.NormalFormGame(100, A, strategies)
st.write(game)

Z= 100; beta=1
evolver = egt.analytical.PairwiseComparison(Z, game)
st.write(evolver)

transition_matrix,fixation_probabilities = evolver.calculate_transition_and_fixation_matrix_sml(beta)
st.write("### Transition Matrix")
st.write(transition_matrix)

st.markdown("### Fixation Probabilities")
st.write(fixation_probabilities)

stationary_distribution = egt.utils.calculate_stationary_distribution(transition_matrix.transpose())