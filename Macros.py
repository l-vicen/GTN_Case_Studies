import numpy as np

STRATEGY_TYPES = ["Mask", "Dynamic Mask", "No Mask"]

LOCAL_MODELS = ["Basic Model", "Fine for not waering masks", "Subsidies for wearing masks", "Low Medical Level", "High Medical Level"]

BASIC_MODEL_PAYOFF = np.array([
        [-1, -5.7, -3.35], # Mask 
        [ -4.7, -88.36, -44.18], # No Mask
        [-2.35, -44.18, -22.09] # Dynamic Mask
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
    LOCAL_MODELS[0]: BASIC_MODEL_PAYOFF,
    LOCAL_MODELS[1]: FINES_MODEL_PAYOFF,
    LOCAL_MODELS[2]: SUBSIDIES_MODEL_PAYOFF,
    LOCAL_MODELS[3]: LOW_MED_MODEL_PAYOFF,
    LOCAL_MODELS[4]: HIGH_MED_MODEL_PAYOFF,
}
