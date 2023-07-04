import Macros

import matplotlib.pylab as plt
import streamlit as st
from egttools.plotting import plot_replicator_dynamics_in_simplex

st.markdown("# Replicator Dynamics: Infinite Population")
st.markdown("## Inputs")
selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS, key = 1)

if (selected_payoff != "None"): 
    A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]
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