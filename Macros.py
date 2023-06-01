import numpy as np

STRATEGY_TYPES = ["Mask", "Dynamic Mask", "No Mask"]

LOCAL_MODELS = ["Basic Model", "Fine for not waering masks", "Subsidies for wearing masks", "Low Medical Level", "High Medical Level"]

BASIC_MODEL_PAYOFF = np.array([
        [-1, -20, -10], # Mask 
        [ -30, -90, -60], # No Mask
        [-15, -47, -31] # Dynamic Mask
])

FINES_MODEL_PAYOFF = np.array([
        [-1, -20, -10], # Mask 
        [ -40, -100, -70], # No Mask
        [-25, -57, -41] # Dynamic Mask
])

SUBSIDIES_MODEL_PAYOFF = np.array([
        [5, -15, -5], # Mask 
        [ -30, -90, -60], # No Mask
        [-15, -47, -31] # Dynamic Mask
])

LOW_MED_MODEL_PAYOFF = np.array([
        [-1, -40, -20], # Mask 
        [ -60, -180, -120], # No Mask
        [-30, -94, -62] # Dynamic Mask
])

HIGH_MED_MODEL_PAYOFF = np.array([
        [-1, -10, -5], # Mask 
        [ -15, -45, -30], # No Mask
        [-5.5, -23.5, -15.5] # Dynamic Mask
])

LOCAL_MODEL_PAYOFF_DICT = {
    LOCAL_MODELS[0]: BASIC_MODEL_PAYOFF,
    LOCAL_MODELS[1]: FINES_MODEL_PAYOFF,
    LOCAL_MODELS[2]: SUBSIDIES_MODEL_PAYOFF,
    LOCAL_MODELS[3]: LOW_MED_MODEL_PAYOFF,
    LOCAL_MODELS[4]: HIGH_MED_MODEL_PAYOFF,
}
