import h5py
import numpy as np
from os import path

def expore_image(output_folder, image, x_coordinate, y_coordinate):
    
    copordinates = np.array([x_coordinate, y_coordinate], ndmin=2)
    
    if path.exists(path.join(output_folder, "out.h5")) == True:
        hdf5_dataset = h5py.File(path.join(output_folder, "out.h5"), 'a')
        train_group = hdf5_dataset.get('Train')
        images = train_group.get('Images')
        coords = train_group.get('Coords')
        
        images.resize(images.shape[0] + image.shape[0], axis=0)
        coords.resize(coords.shape[0] + 1, axis=0)
    
        images[images.shape[0]-image.shape[0]:,:,:] = image
        coords[coords.shape[0]-1] = copordinates
        hdf5_dataset.close()
    else:
        hdf5_dataset = h5py.File(path.join(output_folder, "out.h5"), 'w')
        train_group = hdf5_dataset.create_group('Train')
        train_group.create_dataset("Images", data=image, chunks=True, maxshape=(None,image.shape[1],3))
        train_group.create_dataset("Coords", data=copordinates, chunks=True, maxshape=(None,2))
        hdf5_dataset.close()
    