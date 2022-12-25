import h5py
import numpy as np
from os import path

def expore_image(output_folder, image, x_coordinate, y_coordinate):    
    
    coords_arr, img_arr  = np.array([x_coordinate, y_coordinate], ndmin=2), np.array(image, ndmin=4)

    if path.exists(path.join(output_folder, "out.h5")) == True:
        with h5py.File(path.join(output_folder, "out.h5"), 'a') as hdf5_dataset:
            train_group = hdf5_dataset.get('Train')
            
            images, coords = train_group.get('Images'), train_group.get('Coords')
            images.resize(images.shape[0] + 1, axis=0)
            coords.resize(coords.shape[0] + 1, axis=0)
            
            images[img_arr.shape[0]-1:,:,:] = image
            coords[coords.shape[0]-1] = coords_arr
    else:
        with h5py.File(path.join(output_folder, "out.h5"), 'w') as hdf5_dataset:
            train_group = hdf5_dataset.create_group('Train')
            train_group.create_dataset("Images", data=img_arr, chunks=True, maxshape=(None, image.shape[1], image.shape[2], 3))
            train_group.create_dataset("Coords", data=coords_arr, chunks=True, maxshape=(None,2))
            hdf5_dataset.close()
    