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

sns.set_style("whitegrid")
plt.rcParams['svg.fonttype'] = 'none'
os.environ['KMP_DUPLICATE_LIB_OK']='True'

egt.Random.init()
seed = egt.Random._seed

st.markdown("# Agent-Based-Simulation")
st.markdown("## Inputs")

population = int(st.number_input('Insert population size', value=120, help="Make sure it is a number divisible by 3 since we have three agents."))
allC = int(st.number_input('Insert number of Cooperator agents in the population', value=40))
allD = int(st.number_input('Insert number of Defector agents in the population', value=40))
allRandom = int(st.number_input('Insert number of Random agents in the populatiio', value=40))
# rounds = int(st.number_input('Insert Number of Rounds', value=10))
mu = st.number_input('Insert the Mutation Probability', value = 0.5, format="%.2f")
beta = st.number_input('Insert the Selection Strength', value = 0.5, format="%.2f")
selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS)
rounds = 1

if (selected_payoff != "None"): 

   if st.button('Simulate'):
        A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]
        strategies = [Cooperator(), Defector(), Random()]
        game = egt.games.NormalFormGame(rounds, A, strategies)
        strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]
        st.markdown("## Payoff Matrix")
        st.write(A)

        st.markdown("---")
        st.markdown("## Output")

        st.markdown("### Population Development over Generation")
        st.info("Here 1 single run has been considered.")
        evolver = egt.numerical.PairwiseComparisonNumerical(population, game, 1000)
        output = evolver.run(int(1e7), 1, 1e-3, [allC, allD, allRandom])
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

        st.markdown("### Strategy Distribution")
        st.info("Here 10 runs have been considered and the frequency is the average of them.")
        distribution = evolver.estimate_strategy_distribution(10, int(1e7), int(1e3), beta, mu)
        figTwo, ax = plt.subplots(figsize=(8, 3))
        ax = sns.barplot(x=strategy_labels, y=distribution)
        ax.set_ylabel('frequency', fontsize=15)
        ax.tick_params(bottom = False, labelsize=15)
        sns.despine()
        st.pyplot(figTwo)
   else:
        st.warning('Once the inputs are set, press "Simulate"')
else: 
    st.warning("No local model has been chosen.")