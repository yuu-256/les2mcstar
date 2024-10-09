### This module contains functions to generate settings for mcstar ###
import numpy as np

### TO GENERATE RANDOM ATMOSPHERE COEFFICIENTS ###
def generate_random_coeff(rows, cols):
    ### MAKING RANDOM ARRAY ###
    random_array = np.random.rand(rows, cols)
    
    ### FORMATTING TEXT ###
    formatted_text = "\n".join(" ".join(f"{value:.1f}" for value in row) for row in random_array)
    
    return formatted_text

### TO CONVERT ARRAY TO TEXT INPUT ###
def array_to_input(array):
    lines = []
    ### ITERATING OVER ROWS ###
    for row in array:
        ### FORMATTING ROW ###
        formatted_row = '  '.join(f'{val:.1E}' for val in row)
        lines.append(formatted_row)
    ### JOINING ALL ROWS ###
    text_output = '\n'.join(lines)
    return text_output

def save_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
    return