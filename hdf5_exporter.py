import h5py
import numpy as np

def expore_image(output_folder, image, x_coordinate, y_coordinate):
    copordinates = np.array([x_coordinate, y_coordinate])
    
    hdf5_dataset = h5py.File(output_folder+"/test.h5", 'w')
    train_group = hdf5_dataset.create_group('Train')
    train_group.create_dataset("Images", data=image)
    train_group.create_dataset("Coordinates", data=copordinates)
    hdf5_dataset.close()
    