import matplotlib.pylab as plt
import streamlit as st
import numpy as np
import egt
import Macros

from egttools.analytical.utils import (calculate_gradients, find_roots, check_replicator_stability_pairwise_games)
from egttools.plotting.simplified import plot_replicator_dynamics_in_simplex

st.markdown("# Replicator Dynamics: Infinite Population")
st.markdown("## Inputs")
selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS)

if (selected_payoff != "None"): 
    A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]
    st.markdown("### Payoff Matrix")
    st.write(A)

    st.markdown("### Strategy Mix")
    x = np.linspace(0, 1, num=101, dtype=np.float64)
    st.write(x)

    st.markdown("### Gradient Function")
    gradient_function = lambda x: egt.analytical.replicator_equation(x, A) 
    st.markdown()
    st.write(gradient_function)

    st.markdown("### Gradients")
    gradients = calculate_gradients(np.array((x, 1 - x)).T, gradient_function)
    st.write(gradients)

    st.markdown("### Roots")
    roots = find_roots(gradient_function, nb_strategies=2, nb_initial_random_points=10, method="hybr")

    st.markdown("### Stability")
    stability = check_replicator_stability_pairwise_games(roots, A)

    st.markdown("---")
    st.markdown("## Outputs")
    fig, ax = plt.subplots(figsize=(10,8))
    simplex, gradient_function, roots, roots_xy, stability = plot_replicator_dynamics_in_simplex(A, ax=ax)
    plot = (simplex.draw_triangle()
            .add_vertex_labels(Macros.STRATEGY_TYPES, epsilon_bottom=0.1)
            .draw_stationary_points(roots_xy, stability)
            .draw_gradients(zorder=0)
            .add_colorbar()
            .draw_scatter_shadow(gradient_function, 100, color='gray', marker='.', s=0.1)
            )
    ax.axis('off')
    ax.set_aspect('equal')

    st.markdown("### Roots")
    st.write(roots)

    st.markdown("### Roots X and Y")
    st.write(roots_xy)

    st.markdown("### Stability")
    st.write(stability)

    st.write("### Simplex")
    plt.xlim((-.05,1.05))
    plt.ylim((-.02, simplex.top_corner + 0.05))
    st.pyplot(fig)

else: 
    st.warning("No local model has been chosen.")