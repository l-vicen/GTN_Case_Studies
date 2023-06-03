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
        [-1, -5.7, -3.35], # Mask 
        [ 5.3, -78.36, -34.18], # No Mask
        [2.65, -39.18, -17.09] # Dynamic Mask
])

FINES_MODEL_PAYOFF = np.array([
        [-1, -5.7, -3.35], # Mask 
        [ -14.7, -98.36, -54.18], # No Mask
        [-12.35, -54.18, -32.09] # Dynamic Mask
])

SUBSIDIES_MODEL_PAYOFF = np.array([
        [4, -0.7, -1.65], # Mask 
        [ -14.7, -98.36, -54.18], # No Mask
        [-12.35, -54.18, -32.09] # Dynamic Mask
])

LOW_MED_MODEL_PAYOFF = np.array([
        [-1.38, -8.05, -4.53], # Mask 
        [ -7.05, -132.54, -66.27], # No Mask
        [-3.53, -66.27, -33.14] # Dynamic Mask
])

HIGH_MED_MODEL_PAYOFF = np.array([
        [-1, -4.76, -2.88], # Mask 
        [ -3.76, -70.69, -35.34], # No Mask
        [-1.88, -35.34, -17.67] # Dynamic Mask
])

LOCAL_MODEL_PAYOFF_DICT = {
    LOCAL_MODELS[1]: BASIC_MODEL_PAYOFF,
    LOCAL_MODELS[2]: FINES_MODEL_PAYOFF,
    LOCAL_MODELS[3]: SUBSIDIES_MODEL_PAYOFF,
    LOCAL_MODELS[4]: LOW_MED_MODEL_PAYOFF,
    LOCAL_MODELS[5]: HIGH_MED_MODEL_PAYOFF,
    LOCAL_MODELS[6]: LUCAS_THREE
}
