### This module contains functions to generate settings for mcstar ###
import numpy as np

### TO GENERATE RANDOM ATMOSPHERE COEFFICIENTS ###
def generate_random_coeff(rows, cols):
    ### MAKING RANDOM ARRAY ###
    random_array = np.random.rand(rows, cols)
    
    ### FORMATTING TEXT ###
    formatted_text = "\n".join(" ".join(f"{value:.1f}" for value in row) for row in random_array)
    
    return formatted_text