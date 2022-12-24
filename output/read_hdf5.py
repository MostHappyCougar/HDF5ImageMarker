import h5py

hdf=h5py.File('out.h5', 'r')
print(hdf['/Train/Coords'][:])
hdf.close()