from egttools.plotting.simplified import plot_replicator_dynamics_in_simplex
import matplotlib.pylab as plt
import streamlit as st
import Macros

st.markdown("# Replicator Dynamics: Infinite Population")

st.markdown("## Inputs")
selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS)

if (selected_payoff != None): 
    A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]
    st.write(A)
else: 
    st.warning("No local model has been chosen.")

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

st.markdown("## Model Outputs")
st.write(roots)
st.write(roots_xy)
st.write(stability)


plt.xlim((-.05,1.05))
plt.ylim((-.02, simplex.top_corner + 0.05))
st.pyplot(fig)