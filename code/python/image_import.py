from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from os import getcwd, path
import error_handler

class ImageImport():
    def __init__(self, source_folder, width, height):
        #path to source folder
        self.__path_to_source = path.join(getcwd(), source_folder)
        #Image transforms
        self.__transforms = transforms.Compose([transforms.Resize((height, width)),transforms.CenterCrop((height, width)),transforms.ToTensor()])
        
    def import_image(self):
        try:
            self.__images_dataset = DataLoader(datasets.ImageFolder(self.__path_to_source, transform=self.__transforms),  batch_size=1, shuffle = False)
        except FileNotFoundError:
            raise error_handler.InvalidSourceStructure() 
        return self.__images_dataset