import h5py
from config_parser import filename


with h5py.File(filename, 'r') as hdf:
    print("Image Array Shapes: \n", hdf['/Test/Images'])
    print("Coordinates Shapes: \n", hdf['/Test/Marks'])
    
    print("Image Array: \n", hdf['/Test/Images'][:])
    print("Coordinates: \n", hdf['/Test/Marks'][:])
