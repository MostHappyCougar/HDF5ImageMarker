from torchvision import datasets, transforms
import torch
import pandas as pd
from obj_marking import marking
import os
import config_parser
import sys

dirname = os.path.dirname(__file__)
log_path = os.path.join(dirname, config_parser.log_folder)
source_path = os.path.join(dirname, config_parser.source_folder)

__log_import_raw=[]

def write_import_logs():
    if bool(int(config_parser.import_logs)) == 1:
        from datetime import datetime
        current_date = datetime.now().date()
        current_time = datetime.now().time()   
        __log_import_raw.append([data.numpy()[0, :,:,:].shape, data.mean().numpy(), current_time])
        if os.path.exists(f"{log_path}/{current_date}") == False:
            os.mkdir(f"{log_path}/{current_date}") 
        frame = pd.DataFrame(__log_import_raw, columns=["img_shape", "img_mean", "img_import_timestamp"])
        frame.to_xml(f"{log_path}/{current_date}/import_logs.xml")

img_transforms = transforms.Compose([transforms.Resize((int(config_parser.height), int(config_parser.width))),transforms.CenterCrop((int(config_parser.height), int(config_parser.width))),transforms.ToTensor()])

try:
    loaders = {'import': torch.utils.data.DataLoader(datasets.ImageFolder(source_path, transform=img_transforms),  batch_size=1, shuffle = False)}   
except FileNotFoundError:
    print(f"Directory \"{source_path}\" doesn't exist or no content stored there!!!")
    print("In the INPUT directory should be contained at least one sub directory with at least one .jpg, .png or eather graphic format files")
    sys.exit()

for data, label in loaders['import']:
    write_import_logs()
    marking(data[0,:,:,:])
    



