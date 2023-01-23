import xml.etree.ElementTree as ET
from os import path
import error_handler

class xml_parser():
    def __init__(self, path_to_config: str = None):
        self.__dirname = path.dirname(__file__)
        #When path_to_config is not filled the default path will be used
        if path_to_config:
            self.conf_path = path.join(self.__dirname, path_to_config)
        else:
            self.conf_path = path.join(self.__dirname, "config.xml")
        #Dictionary of parsed parameters
        self.__params = {}
        return
    
    
    def get_conf_params(self) -> tuple:
        self.__conf = ET.parse(self.conf_path)
        self.__conf_root = self.__conf.getroot()
        
        for __tags in self.__conf_root.findall("conf"):
            #Image width
            if int(__tags.find("img_w").text) > 0:
                self.__params["width"] = int(__tags.find("img_w").text)
            else: 
                raise error_handler.InvalidWidth(__tags.find("img_w").text)
            
            #Image height
            if int(__tags.find("img_h").text) > 0:
                self.__params["height"] = int(__tags.find("img_h").text)
            else:
                raise error_handler.InvalidHeight(__tags.find("img_h").text)
            
            #Marks counts
            if int(__tags.find("marks_count").text) > 0:
                self.__params["marks_count"] = int(__tags.find("marks_count").text)
            else:
                raise error_handler.InvalidMarksCount(__tags.find("img_h").text)
            
            #Source folder
            if __tags.find("source_folder").text and __tags.find("source_folder").text.startswith(" ") == False:
                self.__params["source_folder"] = __tags.find("source_folder").text
            else:
                raise error_handler.InvalidSourceFolderName(__tags.find("source_folder").text)
            
            #Output folder
            if __tags.find("output_folder").text and __tags.find("output_folder").text.startswith(" ") == False:
                self.__params["output_folder"] = __tags.find("output_folder").text
            else:
                raise error_handler.InvalidOutputFolderName(__tags.find("output_folder").text)
                
            #Parse output file parameters
            for __output_file_info in __tags.findall("output_file"):
                #Output filename
                if __output_file_info.find("file_name").text and __output_file_info.find("file_name").text.startswith(' ') == False:
                    self.__params["out_file_name"] = __output_file_info.find("file_name").text
                else: 
                    raise error_handler.InvalidOutputFileName(__output_file_info.find("file_name").text)
                
                #Output dataset name
                if __output_file_info.find("dataset_name").text and __output_file_info.find("dataset_name").text.startswith(" ") == False:
                    self.__params["out_dataset_name"] = __output_file_info.find("dataset_name").text
                else:
                    raise error_handler.InvalidDatasetName(__output_file_info.find("dataset_name").text)
        
        return self.__params
            