# Dependencies both indoor and from third party
import Macros
import matplotlib.pylab as plt
import pandas as pd
import streamlit as st
from egttools.plotting import plot_replicator_dynamics_in_simplex

# Heading of Rep. Dyn. Page.
st.markdown("# Replicator Dynamics: Infinite Population")
st.markdown("## Inputs")

# User input to select the model, user wants to apply rep. dynamic on
selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS, key = 1)

# Dont allow user to proceed without having selected a model
if (selected_payoff != "None"): 

    # Query the payoff matrix associated with user selection
    A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]
    st.markdown("### Payoff Matrix") # prints payoff
    st.write(A)

    # Start of output section
    st.markdown("---")
    st.markdown("## Outputs")

    # Creating Matplotlib figure
    fig, ax = plt.subplots(figsize=(10,8))
    ax.axis('off')
    ax.set_aspect('equal')

    # Calling function from EGTtools Tutorial that applies rep. dynamics and returns simplex, grad, etc ...
    simplex, gradient_function, roots, roots_xy, stability = plot_replicator_dynamics_in_simplex(A, ax=ax)

    # Series of uncommented code that I use to understand what I was getting back from the library method

    # st.markdown("### Analytical Calculation of Roots of the ODE System")
    # st.write(roots)

    # st.write("### Strategy frequency for every point of interest")
    # st.write(transf)

    # st.markdown("### Analytical Calculation of Stability of Roots")
    # st.write(stability)

    # st.markdown("### Roots")
    # st.write(roots)

    # st.markdown("### Roots X and Y")
    # st.write(roots_xy)

    # st.markdown("### Stability")
    # st.write(stability)


    # Transforming roots into readable coordinates
    transf = [[ "{0:.0%}".format(elem) if elem >= 0 else "0%" for elem in one_root ] for one_root in roots]
    
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

    # Display Table Output summary
    st.markdown("### Table Summary")
    st.write(df)

    # Creating the Simplex plot as shown in EGTtools tutorial
    plot = (simplex.draw_triangle()
            .add_vertex_labels(Macros.STRATEGY_TYPES, epsilon_bottom=0.1)
            .draw_stationary_points(roots_xy, stability)
            .draw_gradients(zorder=2)
            .add_colorbar()
            .draw_scatter_shadow(gradient_function, 1000, color='gray', marker='.', s=0.1) 
            # Considered 1000 starting states instead of original value
            )
    
    # Displaying plot in app
    st.write("### Simplex")
    plt.xlim((-.05,1.05))
    plt.ylim((-.02, simplex.top_corner + 0.05))
    st.pyplot(fig)

else: 
    st.warning("No local model has been chosen.")
