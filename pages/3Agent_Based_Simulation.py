import numpy as np
import matplotlib.pyplot as plt
import egttools as egt
import streamlit as st
from matplotlib.ticker import AutoMinorLocator
import seaborn as sns
import os
from cycler import cycler
import Macros
from egttools.behaviors.NormalForm.TwoActions import (Cooperator, Defector, Random)
from egttools.plotting.simplified import plot_pairwise_comparison_rule_dynamics_in_simplex_without_roots
from egttools.plotting import plot_pairwise_comparison_rule_dynamics_in_simplex

sns.set_style("whitegrid")
plt.rcParams['svg.fonttype'] = 'none'
os.environ['KMP_DUPLICATE_LIB_OK']='True'

egt.Random.init()
seed = egt.Random._seed

st.markdown("# Normal-Form-Game: Agent-Based-Simulation")

selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS, key = 1)

if (selected_payoff != "None"): 
    A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]

    strategies = [Cooperator(), Defector(), Random()]
    population = 100

    game = egt.games.NormalFormGame(100, A, strategies)
    strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]
    st.write(game.expected_payoffs())

    st.markdown("### Population Development over Generation")
    evolver = egt.numerical.PairwiseComparisonNumerical(population, game, 100)
    output = evolver.run(int(1e7), 1, 1e-3, [30,30,40])
    colors = sns.color_palette("colorblind", len(strategies))
    plt.rc('axes', prop_cycle=(cycler('color', colors)))
    fig, ax = plt.subplots(figsize=(10, 4))
    lines = ax.plot(np.arange(1e7+1)[::100], output[::100]/population)
    plt.setp(lines, linewidth=2)
    ax.legend([s for s in strategy_labels], frameon=False, fontsize=12)
    ax.set_ylabel('Population (%)', fontsize=15, fontweight='bold')
    ax.set_xlabel('Generation', fontsize=15, fontweight='bold')
    ax.set_xscale('log')
    ax.set_xlim(1, 1e7)
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis='x', which='both', direction='in', labelsize=15, width=2)
    ax.tick_params(axis='y', which='both', direction='in', labelsize=15, width=2)

    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontweight('bold')
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontweight('bold')
    st.pyplot(fig)

    st.markdown("### Simplex Representation")
    type_labels = ['Mask', 'No-Mask', 'Dynamic']
    strategies = [Cooperator(), Defector(), Random()]

    game = egt.games.NormalFormGame(population, A, strategies)
    st.write(game)
    beta = 1
    mu = 1/population

    fig, ax = plt.subplots(figsize=(12,10))
    simplex, gradient_function, game, evolver = plot_pairwise_comparison_rule_dynamics_in_simplex_without_roots(payoff_matrix =game.expected_payoffs(), group_size = 2, population_size = population, beta = beta, ax=ax)
    transitions = evolver.calculate_transition_matrix(beta=beta, mu=mu)
    sd = egt.utils.calculate_stationary_distribution(transitions.transpose())
    plot = (simplex.draw_triangle()
                .add_vertex_labels(type_labels, epsilon_bottom=0.1, epsilon_top=0.03)
                .draw_stationary_distribution(sd, alpha=1, shrink=0.5,edgecolors='gray', cmap='binary', shading='gouraud', zorder=0)
                .draw_gradients(zorder=2, linewidth=1.5)
                .add_colorbar(shrink=0.5))
    ax.axis('off')
    ax.set_aspect('equal')

    plt.xlim((-.05,1.05))
    plt.ylim((-.02, simplex.top_corner + 0.05))

    st.markdown("## Simplex")
    st.pyplot(fig)

else: 
    st.warning("No local model has been chosen.")