# Dependencies both indoor and from third party
from egttools.plotting.simplified import plot_pairwise_comparison_rule_dynamics_in_simplex_without_roots
import egttools as egt
import matplotlib.pylab as plt
import streamlit as st
import Macros

# Heading of Markov Page.
st.markdown("# Markov Process: Finite Population")
st.markdown("## Inputs")

# User input to select the model, population, mutation prob. and intensity of selection (user wants to apply markov)
population = int(st.number_input('Insert Population Size', value=100, key=1))
mu = st.number_input('Insert the Mutation Probability', value = 0.5, format="%.2f")
beta = st.number_input('Insert the Selection Strength', value = 0.5, format="%.2f")
selected_payoff = st.selectbox("Select the desired payoff matrix representing a local model.", Macros.LOCAL_MODELS)

# Dont allow user to proceed without having selected a model
if (selected_payoff != "None"): 

    # Query the payoff matrix associated with user selection
    A = Macros.LOCAL_MODEL_PAYOFF_DICT[selected_payoff]
    st.markdown("## Payoff Matrix") # prints payoff
    st.write(A)

    # Start of output section
    st.markdown("---")
    st.markdown("## Outputs")
    
    # Doing the heavy calculation of this approach by calling the implemented methods
    simplex, gradient_function, game, evolver = plot_pairwise_comparison_rule_dynamics_in_simplex_without_roots(payoff_matrix = A, group_size = 2, population_size = population, beta = beta, ax=ax)
    transitions = evolver.calculate_transition_matrix(beta=beta, mu=mu)
    sd = egt.utils.calculate_stationary_distribution(transitions.transpose())
    
    # Series of uncommented code that I use to understand what I was getting back from the library method
    # st.markdown("## Transition Probabilities")
    # st.write(transitions)

    # st.markdown("## Standard Deviation")
    # st.write(sd)

    # st.markdown("## Game")
    # st.write(game)

    # Creating the Simplex plot as shown in EGTtools tutorial
    plot = (simplex.draw_triangle()
                .add_vertex_labels(Macros.STRATEGY_TYPES, epsilon_bottom=0.1, epsilon_top=0.03)
                .draw_stationary_distribution(sd, alpha=1, shrink=0.5,edgecolors='gray', cmap='binary', shading='gouraud', zorder=0)
                .draw_gradients(zorder=2, linewidth=1.5)
                .add_colorbar(shrink=0.5))
    
    # Defines the figure 
    fig, ax = plt.subplots(figsize=(10,8))
    ax.axis('off')
    ax.set_aspect('equal')
    plt.xlim((-.05,1.05))
    plt.ylim((-.02, simplex.top_corner + 0.05))

    st.markdown("## Simplex")
    st.pyplot(fig)

else: 
    st.warning("No local model has been chosen.")


