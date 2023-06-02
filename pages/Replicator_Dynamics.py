import matplotlib.pylab as plt
import streamlit as st
import numpy as np
import egttools as egt
import Macros

from egttools.analytical.utils import (calculate_gradients, find_roots, check_replicator_stability_pairwise_games)
from egttools.plotting.simplified import plot_replicator_dynamics_in_simplex

st.markdown("# Replicator Dynamics: Infinite Population")

selected_X_player_game = st.selectbox("Select the desired number of players for your game:", Macros.PLAYER_GAMES, key = 0)
x = np.linspace(0, 1, num=101, dtype=np.float64)

if (selected_X_player_game == "2-Player Game"):
    A = Macros.TWO_PLAYER_BASIC_MODEL_PAYOFF
    st.markdown("### Payoff Matrix")
    st.write(A)

    gradient_function = lambda x: egt.analytical.replicator_equation(x, A)
    gradients = calculate_gradients(np.array((x, 1 - x)).T, gradient_function)

    # Find roots and stability
    roots = find_roots(gradient_function, nb_strategies=2, nb_initial_random_points=10, method="hybr")
    stability = check_replicator_stability_pairwise_games(roots, A)

    # Plot the gradient
    egt.plotting.plot_gradients(gradients[:, 0], xlabel="frequency of hawks", roots=roots, stability=stability)
    fig, ax = plt.subplots(figsize=(10,8))
    st.pyplot(fig)

else: 
    st.markdown("## Inputs")
    selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS, key = 1)

    if (selected_payoff != "None"): 
        A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]
        st.markdown("### Payoff Matrix")
        st.write(A)

        gradient_function = lambda x: egt.analytical.replicator_equation_n_player(x, A, group_size=3)
        gradients = calculate_gradients(np.array((x, 1 - x)).T, gradient_function)

        st.markdown("### Gradients")
        st.write(gradients)

        
        fig = plt.figure()
        ax = egt.plotting.plot_gradients(gradients[:, 0], xlabel="frequency of hawks")
        plt.show()
    
        st.pyplot(plt.figure())

        st.markdown("---")
        st.markdown("## Outputs")
        fig, ax = plt.subplots(figsize=(10,8))
        simplex, gradient_function, roots, roots_xy, stability = plot_replicator_dynamics_in_simplex(A, ax=ax)
        
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