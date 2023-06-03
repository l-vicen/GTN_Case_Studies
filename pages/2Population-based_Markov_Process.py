from egttools.plotting.simplified import plot_pairwise_comparison_rule_dynamics_in_simplex_without_roots
from egttools.analytical import PairwiseComparison
from egttools.plotting import plot_gradients
import egttools as egt
import matplotlib.pylab as plt
import streamlit as st
import numpy as np
import Macros

st.markdown("# Markov Process: Infinite Population")
st.markdown("## Inputs")
population = int(st.number_input('Insert Population Size', value=100, key=1))
beta = st.number_input('Insert the Selection Strength', value = 1)
mu = 1/population
selected_X_player_game = st.selectbox("Select the desired number of players for your game:", Macros.NUMBER_STRATEGY_GAMES, key = 0)
if (selected_X_player_game == "2-Strategy Game"):
    pass
    # # Payoff matrix
    # V = 2; D = 3; T = 1
    # A = np.array([
    #         [ (V-D)/2, V],
    #         [ 0      , (V/2) - T],
    #     ])
    # st.markdown("### Payoff Matrix")
    # st.write(A)

    # pop_states = np.arange(0, population + 1, 1)
    # game = egt.games.Matrix2PlayerGameHolder(number_strategy = 2, payoff =A)
    # evolver = PairwiseComparison(population, game)

    # st.markdown("### Analytical Calculation of Gradients")
    # gradients = np.array([evolver.calculate_gradient_of_selection(beta, np.array([x, population-x])) for x in range(population + 1)])
    # st.write(gradients)

    # # Plot gradient of selections
    # st.pyplot(plot_gradients(gradients[:, 0], xlabel="Frequency of Cooperator  (% population)", marker="o").get_figure())
    # st.pyplot(plot_gradients(gradients[:, 1], xlabel="Frequency of Free-rider (% population)", marker="o").get_figure())


else:
        
    selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS)

    if (selected_payoff != "None"): 
        A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]
        st.markdown("## Payoff Matrix")
        st.write(A)

        st.markdown("---")
        st.markdown("## Outputs")
        fig, ax = plt.subplots(figsize=(12,10))
        simplex, gradient_function, game, evolver = plot_pairwise_comparison_rule_dynamics_in_simplex_without_roots(payoff_matrix = A, group_size = 2, population_size = population, beta = beta, ax=ax)
        transitions = evolver.calculate_transition_matrix(beta=beta, mu=mu)
        sd = egt.utils.calculate_stationary_distribution(transitions.transpose())
        plot = (simplex.draw_triangle()
                    .add_vertex_labels(Macros.STRATEGY_TYPES, epsilon_bottom=0.1, epsilon_top=0.03)
                    .draw_stationary_distribution(sd, alpha=1, shrink=0.5,edgecolors='gray', cmap='binary', shading='gouraud', zorder=0)
                    .draw_gradients(zorder=2, linewidth=1.5)
                    .add_colorbar(shrink=0.5))
        ax.axis('off')
        ax.set_aspect('equal')

        st.markdown("## Transition Probabilities")
        st.write(transitions)

        st.markdown("## Standard Deviation")
        st.write(sd)

        st.markdown("## Game")
        st.write(game)

        plt.xlim((-.05,1.05))
        plt.ylim((-.02, simplex.top_corner + 0.05))

        st.markdown("## Simplex")
        st.pyplot(fig)

    else: 
        st.warning("No local model has been chosen.")


