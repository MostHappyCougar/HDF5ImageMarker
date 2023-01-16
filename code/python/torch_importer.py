from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from obj_marking import marking
from os.path import dirname, join
from config_parser import height, width, source_folder
from ErrorHandler import iss_handler

dirname = dirname(__file__)
source_path = join(dirname, source_folder)

img_transforms = transforms.Compose([transforms.Resize((height, width)),transforms.CenterCrop((height, width)),transforms.ToTensor()])

try:
    importer = DataLoader(datasets.ImageFolder(source_path, transform=img_transforms),  batch_size=1, shuffle = False) 
except FileNotFoundError:
    iss_handler("Import Error", f'No subdirectory in "{source_folder}" or no content stored in existing subdirectory! \nCheck if the source folder have this architecture: {source_folder}\<any_subdirectory_name>\<content>', "imp_err01")

for data, label in importer:
    marking(data[0,:,:,:])
    



