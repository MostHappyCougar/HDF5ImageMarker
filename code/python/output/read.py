import h5py

with h5py.File('test_suite.h5', 'r') as hdf:
    print("Image Array Shapes: \n", hdf['/Test/Images'].shape)
    print("Coordinates Shapes: \n", hdf['/Test/Marks'].shape)
    
    print("Image Array: \n", hdf['/Test/Images'][:])
    print("Coordinates: \n", hdf['/Test/Marks'][:])