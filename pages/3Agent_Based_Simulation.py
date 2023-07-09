# Dependencies both indoor and from third party
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

# Default settings of plots
sns.set_style("whitegrid")
plt.rcParams['svg.fonttype'] = 'none'
os.environ['KMP_DUPLICATE_LIB_OK']='True'
egt.Random.init()
seed = egt.Random._seed

# Heading ABS
st.markdown("# Agent-Based-Simulation")
st.markdown("## Inputs")

# User inputs
population = int(st.number_input('Insert population size', value=1200, help="Make sure it is a number divisible by 3 since we have three agents."))
allC = int(st.number_input('Insert number of Cooperator agents in the population', value=400))
allD = int(st.number_input('Insert number of Defector agents in the population', value=400))
allRandom = int(st.number_input('Insert number of Random agents in the populatiio', value=400))
mu = st.number_input('Insert the Mutation Probability', value = 1e-1, format="%.2f")
beta = st.number_input('Insert the Selection Strength', value = 1.0, format="%.2f")
selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS)
rounds = 1

# Dont allow user to proceed without having selected a model
if (selected_payoff != "None"): 
   
   # Making sure all params are given
   if st.button('Simulate'):
        
        # Query the payoff matrix associated with user selection
        A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]

        # Calling out pre-defined behavior 
        strategies = [Cooperator(), Defector(), Random()]
        strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]

        # Create NormalFormGame Representation
        game = egt.games.NormalFormGame(rounds, A, strategies)

        # Model payoff    
        st.markdown("## Payoff Matrix")
        st.write(A)

        # Start of output section
        st.markdown("---")
        st.markdown("## Output")

        # 1 Run of numerical simulation as shown in EGTtool tutorial
        st.markdown("### Population Development over Generation")
        st.info("Here 1 single run has been considered.")

        # Creates the evolver object 
        evolver = egt.numerical.PairwiseComparisonNumerical(population, game, 1000)
       
        # Run simulation once for 1e7 generations and starting agent population states
        output = evolver.run(int(1e7), 1, 1e-3, [allC, allD, allRandom])
        
        # Setting up plot configurations (style)
        colors = sns.color_palette("colorblind", len(strategies))
        plt.rc('axes', prop_cycle=(cycler('color', colors)))

        # Creates matplotlib figure
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

        # Adds figure to app
        st.pyplot(fig)

        # Now consider 10 runs and take the average of the observed population frequencies as in EGTtool Tutorial
        st.markdown("### Strategy Distribution")
        st.info("Here 10 runs have been considered and the frequency is the average of them.")
        
        # Calculates the distribution
        distribution = evolver.estimate_strategy_distribution(10, int(1e7), int(1e3), beta, mu)
        
        # Creates 2nd Figure
        figTwo, ax = plt.subplots(figsize=(8, 3))
        ax = sns.barplot(x=strategy_labels, y=distribution)
        ax.set_ylabel('frequency', fontsize=15)
        ax.tick_params(bottom = False, labelsize=15)
        sns.despine()

        # Adds to app
        st.pyplot(figTwo)
   else:
        st.warning('Once the inputs are set, press "Simulate"')
else: 
    st.warning("No local model has been chosen.")