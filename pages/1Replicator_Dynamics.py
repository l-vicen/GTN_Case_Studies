import Macros

import matplotlib.pylab as plt
import pandas as pd
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

    # st.markdown("### Analytical Calculation of Roots of the ODE System")
    # st.write(roots)

    # st.write("### Strategy frequency for every point of interest")
    transf = [[ "{0:.0%}".format(elem) if elem >= 0 else "0%" for elem in one_root ] for one_root in roots]
    # st.write(transf)

    # st.markdown("### Analytical Calculation of Stability of Roots")
    # st.write(stability)
    
    ax.axis('off')
    ax.set_aspect('equal')

    # st.markdown("### Roots")
    # st.write(roots)

    # st.markdown("### Roots X and Y")
    # st.write(roots_xy)

    # st.markdown("### Stability")
    # st.write(stability)

    # Create the third column based on the values of the first column
    encoded_column = ['Stable' if val == 1 else 'Unstable' if val == -1 else 'Saddle' for val in stability]
    list_of_tuples = [tuple(arr) for arr in transf]

    # Trick to remove non-unique coordinates
    seen = set()
    removed_indexes = [i for i, elem in enumerate(list_of_tuples) if elem in seen or seen.add(elem)]

    # Clean up of repetitive values
    unique_points_prob = [elem for i, elem in enumerate(list_of_tuples) if i not in removed_indexes]
    unique_points_stability = [elem for i, elem in enumerate(stability) if i not in removed_indexes]
    unique_points_encoded = [elem for i, elem in enumerate(encoded_column) if i not in removed_indexes]

    # Create the dataframe
    df = pd.DataFrame({
        'Stability': unique_points_stability,
        'Stability Category': unique_points_encoded,
        'Strategy Distribution (Mask : Dyn. Mask : No Mask)': unique_points_prob,
    })


    st.markdown("### Table Summary")
    st.write(df)

    plot = (simplex.draw_triangle()
            .add_vertex_labels(Macros.STRATEGY_TYPES, epsilon_bottom=0.1)
            .draw_stationary_points(roots_xy, stability)
            .draw_gradients(zorder=2)
            .add_colorbar()
            .draw_scatter_shadow(gradient_function, 1000, color='gray', marker='.', s=0.1)
            )

    st.write("### Simplex")
    plt.xlim((-.05,1.05))
    plt.ylim((-.02, simplex.top_corner + 0.05))
    st.pyplot(fig)

else: 
    st.warning("No local model has been chosen.")
