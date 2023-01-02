import h5py
import numpy as np
from os import path
from config_parser import filename, mode, dataset

def expore_image(output_folder, image, coords):    
        
    coords_arr, img_arr  = np.array(coords, ndmin=3), np.array(image, ndmin=4)

    if path.exists(path.join(output_folder, filename)) == True:
        with h5py.File(path.join(output_folder, filename), mode) as hdf5_dataset:
            train_group = hdf5_dataset.get(dataset)
            
            try:
                images, coords = train_group.get('Images'), train_group.get('Marks')
                images.resize(images.shape[0] + 1, axis=0)
                coords.resize(coords.shape[0] + 1, axis=0)
            except AttributeError:
                train_group = hdf5_dataset.create_group(dataset)
                train_group.create_dataset("Images", data=img_arr, chunks=True, maxshape=(None, img_arr.shape[1], img_arr.shape[2], img_arr.shape[3]))
                train_group.create_dataset("Marks", data=coords_arr, chunks=True, maxshape=(None, coords_arr.shape[1], coords_arr.shape[2]))
                
            
            images[img_arr.shape[0]-1:] = image
            coords[coords.shape[0]-1:] = coords_arr
    else:
        with h5py.File(path.join(output_folder, filename), 'w') as hdf5_dataset:
            train_group = hdf5_dataset.create_group(dataset)
            train_group.create_dataset("Images", data=img_arr, chunks=True, maxshape=(None, img_arr.shape[1], img_arr.shape[2], img_arr.shape[3]))
            train_group.create_dataset("Marks", data=coords_arr, chunks=True, maxshape=(None, coords_arr.shape[1], coords_arr.shape[2]))
    