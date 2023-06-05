import matplotlib as plt
import streamlit as st
import numpy as np
import egttools as egt
import Macros

from egttools.analytical.utils import (calculate_gradients,find_roots, check_replicator_stability_pairwise_games)
from egttools.plotting import plot_replicator_dynamics_in_simplex, plot_gradients

st.markdown("# Replicator Dynamics: Infinite Population")

selected_X_player_game = st.selectbox("Select the desired number of players for your game:", Macros.NUMBER_STRATEGY_GAMES, key = 0)
strategy_i = np.linspace(0, 1, num=101, dtype=np.float64)

if (selected_X_player_game == "2-Strategy Game"):

    A = Macros.TWO_STRATEGY_LUCAS_PAYOFF
    st.markdown("### Payoff Matrix")
    st.write(A)

    st.markdown("### Analytical Calculation of Gradients")
    gradient_function = lambda x: egt.analytical.replicator_equation(x, A)
    gradients = calculate_gradients(np.array((strategy_i, 1 - strategy_i)).T, gradient_function)
    st.write(gradients)

    # # Find roots and stability
    st.markdown("### Analytical Calculation of Roots of the ODE System")
    roots = find_roots(gradient_function, nb_strategies=2, nb_initial_random_points=100, method="hybr")
    st.write(roots)

    st.markdown("### Analytical Calculation of Stability of Roots")
    stability = check_replicator_stability_pairwise_games(roots, A)
    st.write(stability)

    # Plot gradient of selections
    st.pyplot(plot_gradients(gradients[:, 0], xlabel="Frequency of Cooperator", roots=roots, stability=stability).get_figure())
    st.pyplot(plot_gradients(gradients[:, 1], xlabel="Frequency of Free-rider", roots=roots, stability=stability).get_figure())

else: 
    st.markdown("## Inputs")
    selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS, key = 1)

    if (selected_payoff != "None"): 
        A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]
        # A = Macros.LUCAS_THREE
        st.markdown("### Payoff Matrix")
        st.write(A)
 
        st.markdown("---")
        st.markdown("## Outputs")
        fig, ax = plt.subplots(figsize=(10,8))
        simplex, gradient_function, roots, roots_xy, stability = plot_replicator_dynamics_in_simplex(A, ax=ax)

        st.markdown("### Analytical Calculation of Roots of the ODE System")
        st.write(roots)

        st.markdown("### Analytical Calculation of Stability of Roots")
        st.write(stability)
        
        ax.axis('off')
        ax.set_aspect('equal')

        st.markdown("### Roots")
        st.write(roots)

        st.markdown("### Roots X and Y")
        st.write(roots_xy)

        st.markdown("### Stability")
        st.write(stability)
        
        plot = (simplex.draw_triangle()
                .add_vertex_labels(Macros.STRATEGY_TYPES, epsilon_bottom=0.1)
                .draw_stationary_points(roots_xy, stability)
                .draw_gradients(zorder=0)
                .add_colorbar()
                .draw_scatter_shadow(gradient_function, 100, color='gray', marker='.', s=0.1)
                )

        st.write("### Simplex")
        plt.xlim((-.05,1.05))
        plt.ylim((-.02, simplex.top_corner + 0.05))
        st.pyplot(fig)

    else: 
        st.warning("No local model has been chosen.")