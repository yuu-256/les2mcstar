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

### TO SAVE TEXT TO FILE ###
def save_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
    return

### COMBINE TEXT FILES TO INOUT FORMAT###
def write_combined_text_files(outpath, imax):
    with open(outpath, 'w') as outfile:
        for i in range(0, imax + 1):
            ### FILENAME ###
            filename = f'../data/volume_concentration_{i}.txt'
            try:
                with open(filename, 'r') as infile:
                    content = infile.read()
                    
                    # 書き出すテキストのフォーマット
                    outfile.write(f'1 {i+1}  ipoly lz/cconc(i,j,lz,ipoly)\n')
                    outfile.write(content)
                    outfile.write(f'1 {i+1+1}  ipoly lz/cconc(i,j,lz,ipoly)\n')
            except FileNotFoundError:
                print(f"{filename} not found. Skipping...")
                continue  
    return
