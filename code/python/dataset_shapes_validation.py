import error_handler
import h5py
import os

class DatasetValudation():
    def __init__(self, dataset_params):
        self.__params = dataset_params
        
        self.__dirname = os.path.dirname(__file__)
        self.__out_file = os.path.join(self.__dirname, self.__params["output_folder"], self.__params["out_file_name"]+".h5")
        
        if os.path.exists(self.__out_file):
            with h5py.File(self.__out_file, 'r') as out_file:
                self.__dataset_shapes = [out_file[self.__params["out_dataset_name"]+"/Images"][0].shape, out_file[self.__params["out_dataset_name"]+"/Marks"][0].shape]
                if self.__dataset_shapes != [(3, self.__params["height"], self.__params["width"]), (self.__params["marks_count"], 2)]:
                    raise error_handler.InvalidConfiguration([(3, self.__params["height"], self.__params["width"]), (self.__params["marks_count"], 2)], self.__dataset_shapes)
            
