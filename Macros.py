import numpy as np

STRATEGY_TYPES = ["Mask", "Dynamic Mask", "No Mask"]
LOCAL_MODELS = ["None", "Basic Model", "Fine for not wearing masks", "Subsidies for wearing masks", "Low Medical Level", "High Medical Level", "LUCAS"]
NUMBER_STRATEGY_GAMES = ["2-Strategy Game", "3-Strategy Game"]

TWO_STRATEGY_LUCAS_PAYOFF = np.array([
       [3, 1.5], # Mask
       [1.5, -3] # No Mask
])
LUCAS_THREE = np.array([
       [3, 0, 1.5], # Mask
       [6, 0.5, 0.75], # No Mask
       [2, 0, 1], # Dyn. Mask
])

BASIC_MODEL_PAYOFF = np.array([
        [-1.25, -5.7, -3.35], # Mask 
        [ 25.3, -58.36, -14.18], # No Mask
        [12.65, -29.18, 7.09] # Dynamic Mask
])

FINES_MODEL_PAYOFF = np.array([
        [-1.25, -5.7, -3.35], # Mask 
        [ 15.3, -68.36, -24.18], # No Mask
        [2.65, -39.18, -17.09] # Dynamic Mask
])

SUBSIDIES_MODEL_PAYOFF = np.array([
        [3.75, -0.7, 1.65], # Mask 
        [25.3, -58.36, -14.18], # No Mask
        [12.65, -29.18, -7.09] # Dynamic Mask
])

LOW_MED_MODEL_PAYOFF = np.array([
        [-1.375, -8.05, -4.525], # Mask 
        [ 22.95, -102.54, -36.27], # No Mask
        [-11.475, -51.27, -18.135] # Dynamic Mask
])

HIGH_MED_MODEL_PAYOFF = np.array([
        [-1.2, -4.76, -2.88], # Mask 
        [ 26.24, -40.688, -5.3444], # No Mask
        [13.12, -20.344, -2.672] # Dynamic Mask
])

LOCAL_MODEL_PAYOFF_DICT = {
    LOCAL_MODELS[1]: BASIC_MODEL_PAYOFF,
    LOCAL_MODELS[2]: FINES_MODEL_PAYOFF,
    LOCAL_MODELS[3]: SUBSIDIES_MODEL_PAYOFF,
    LOCAL_MODELS[4]: LOW_MED_MODEL_PAYOFF,
    LOCAL_MODELS[5]: HIGH_MED_MODEL_PAYOFF,
#     LOCAL_MODELS[6]: LUCAS_THREE
}
