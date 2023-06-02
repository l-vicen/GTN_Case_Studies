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