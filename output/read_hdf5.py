import h5py

hdf=h5py.File('out.h5', 'r')
print("Image Array: \n", hdf['/Train/Images'][2])
print("Coordinates: \n", hdf['/Train/Coords'][2])
hdf.close()