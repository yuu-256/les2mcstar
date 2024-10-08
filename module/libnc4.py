### This module is used to read the netCDF4 data files and extract the data from them.

### IMPORTING LIBRARIES ###
import numpy as np
import netCDF4 as nc
import os
import matplotlib.pyplot as plt

### FUNCTION DEFINITIONS ###

### PLOT A SLICE AT Z=Z ###
def plot_slice_at_z(dataset, variable, z_index):
    """
    :param data: 3D masked_array (x, y, z)
    :param z_index: index of z-axis
    """
    data = dataset.variables[variable][:]
    if z_index < 0 or z_index >= data.shape[2]:
        print("Invalid z_index")
        return
    
    ### GET A SLICE AT Z=Z ###
    slice_data = data[z_index, :, :]
    
    ### PLOT THE SLICE ###
    plt.figure(figsize=(6, 6))
    plt.imshow(slice_data, cmap='viridis', origin='lower')
    plt.colorbar(label=f'{variable} values')
    plt.title(f'Layer at z={z_index}')
    plt.show()
    
def plot_slice_at_z_simple(data, z_index):
    """
    :param data: 3D masked_array (x, y, z)
    :param z_index: index of z-axis
    """
    if z_index < 0 or z_index >= data.shape[2]:
        print("Invalid z_index")
        return
    
    ### GET A SLICE AT Z=Z ###
    slice_data = data[z_index, :, :]
    
    ### PLOT THE SLICE ###
    plt.figure(figsize=(6, 6))
    plt.imshow(slice_data, cmap='viridis', origin='lower')
    plt.colorbar(label= 'values')
    plt.title(f'Layer at z={z_index}')
    plt.show()

### GET SUMMATION OF NDC VALUES IN ONE SLICE ###
def get_sum(data, z):
    return np.sum(data[z, :, :])

### PLOT np.sum(data[z, :, :]) FOR ALL Z VALUES, IN VERTICAL ###
def plot_sum(dataset, variable):
    data = dataset.variables[variable][:]
    sums = [get_sum(data, z) for z in range(data.shape[0])]
    plt.plot(sums)
    plt.xlabel('z')
    plt.ylabel(f'Sum of {variable} values')
    plt.title(f'Sum of {variable} values at each z')
    plt.show()
    
### CALCULATE THE RELATUIVE VALUE OF THE MATRIX ###
def calculate_relative_value(matrix):
    """
    Calculate the relative value of the matrix
    Parameters:
    matrix (numpy.ndarray): The matrix to calculate the relative value of
    Returns:
    numpy.ndarray: The matrix with the relative values
    """
    # Calculate the maximum value of the matrix
    max_value = np.max(matrix)

    # Calculate the relative value of the matrix (normalized by the maximum value)
    relative_value = matrix / max_value
    
    # Clip very small values to 0 for numerical stability (adjust the threshold as needed)
    relative_value = np.clip(relative_value, 0, None)
    
    return relative_value

### CONVERT THE DATA TO RELATIVE VALUE ###
def conv_to_relative_value(dataset, var_name):
    """
    Convert the variable data to relative value
    Parameters:
    dataset (netCDF4.Dataset): The dataset containing the variable data
    var_name (str): The name of the variable to convert
    Returns:
    numpy.ndarray: The variable data in relative value
    """
    # Get the variable data from the dataset
    data = dataset.variables[var_name][:]
    
    # Calculate the relative value of the variable data
    relative_value = calculate_relative_value(data)
    
    return relative_value