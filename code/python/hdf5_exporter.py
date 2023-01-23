import h5py
import numpy as np
from os import path
import torch

class hdf5_exporter():
    def __init__(self, out_folder, filename, dataset_name):
        self.__dirname = path.dirname(__file__)
        self.__out_folder = path.join(self.__dirname, out_folder)
        self.__filename = filename + ".h5"
        self.__dataset_name = dataset_name
        self.__marks_array, self.__img_array = [], []
        return
        
        
    def export_image(self, image: torch.FloatTensor , marks: list[float]) -> None:
        self.__marks_array, self.__img_array = np.array(marks, ndmin=3), np.array(image, ndmin=4)
        if path.exists(path.join(self.__out_folder, self.__filename)):
            with h5py.File(path.join(self.__out_folder, self.__filename), 'a') as hdf5_dataset:
                if f'{self.__dataset_name}' in hdf5_dataset:
                    train_group = hdf5_dataset.get(self.__dataset_name)
                    images, coords = train_group.get('Images'), train_group.get('Marks')
                    images.resize(images.shape[0] + 1, axis=0)
                    coords.resize(coords.shape[0] + 1, axis=0)
                    images[-1] = self.__img_array
                    coords[-1] = self.__marks_array
                else:
                    train_group = hdf5_dataset.create_group(self.__dataset_name)
                    train_group.create_dataset("Images", data=self.__img_array, chunks=True, maxshape=(None, self.__img_array.shape[1], self.__img_array.shape[2], self.__img_array.shape[3]))
                    train_group.create_dataset("Marks", data=self.__marks_array, chunks=True, maxshape=(None, self.__marks_array.shape[1], self.__marks_array.shape[2]))
        else:
            with h5py.File(path.join(self.__out_folder, self.__filename), 'w') as hdf5_dataset:
                train_group = hdf5_dataset.create_group(self.__dataset_name)
                train_group.create_dataset("Images", data=self.__img_array, chunks=True, maxshape=(None, self.__img_array.shape[1], self.__img_array.shape[2], self.__img_array.shape[3]))
                train_group.create_dataset("Marks", data=self.__marks_array, chunks=True, maxshape=(None, self.__marks_array.shape[1], self.__marks_array.shape[2]))
        return