import netCDF4 as nc
import numpy as np

### DEFINE FILE PATH
input_file = '../data/ezaki.nc'
output_file = '../data/ezaki_timeslice.nc'

### LOAD ORIGINAL FILE
with nc.Dataset(input_file, 'r') as src:
    # MAKE NEW OUTPUT FILE
    with nc.Dataset(output_file, 'w') as dst:
        # DUPRICATE DIMENTIONS
        for name, dimension in src.dimensions.items():
            if name == 'time':
                dst.createDimension(name, 1)  # 'time', 1 dimention
            else:
                dst.createDimension(name, len(dimension))
        
        # DUPRICATE VARIABLE
        for name, variable in src.variables.items():
            # DIFINE NEW SIZE
            dimensions = variable.dimensions
            if 'time' in dimensions:
                new_dimensions = tuple('time' if dim == 'time' else dim for dim in dimensions)
                new_shape = (1,) + variable.shape[1:]
            else:
                new_dimensions = dimensions
                new_shape = variable.shape
            
            # MAKE VARIABLES
            new_var = dst.createVariable(name, variable.datatype, new_dimensions)
            
            # COPY DATA: EXTRACT LAST TIME
            if 'time' in dimensions:
                new_var[:] = variable[-1, ...]
            else:
                new_var[:] = variable[:]
            
            # COPY TYPE
            new_var.setncatts({k: variable.getncattr(k) for k in variable.ncattrs()})
        
        # COPY GLOBAL TYPE
        dst.setncatts({k: src.getncattr(k) for k in src.ncattrs()})
