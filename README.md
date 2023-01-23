# Decription
This utility is applicable to marking up any points of an image according to neural network creators requirements irrespective to count of these points. 

With this utility you may get coordinates of any image points that are keys accordingly to your purposes and write down these image and coordinates into the dataset at the all your points have been marked up
## How to install
```
git clone https://github.com/MostHappyCougar/HDF5ImageMarker.git
```
### Requirements
| Package | Version |
| ------------- | ------------- |
| torchvision  | 0.14.0+cu117  |
| torch  | 1.13.0+cu117  |
|	 h5py    |  3.7.0 |
|  matplotlib |  3.5.3 |
|  numpy | 1.23.1  |
		
## How to use
1. Create your input folder where the images for marking will be take from
    - This folder should be created upon the directory the `img_marker.py` is stored in
2. Create subdirectory in this folder and put your image set into this subdirectory
3. Set the name of input folder into the `<source_folder>` tag of `config.xml` file
4. Create output folder upon directory the `img_marker.py` is stored in
5. Set the name of output folder into the `<output_folder>` tag of `config.xml` file

Now you can use this util via running `img_marker.py` as regular python script
- To mark up the key point just click to an image in required position
- To cancel last point - press `z`. You may cancel all points for current image
- When all points have been marked up press `Enter` to save
## Detail configuring
You can also configure some parameters of marking via `config.xml`. Be aware changing any parameters when `img_marker.py` is still running is not prodlike scenario. You may change any parameter in `config.xml` only before `img_marker.py` is ran.
### Parameters overview
- `img_w` and `img_h` - the sizes that an each image will be resized to. `img_w` is image width, `img_h` is image height
- `source_folder` - The folder that images for marking is store in
- `output_folder` - the folder where the HDF5 file will be save
- `marks_count` - count of poits that will be marked up
- `file_name` - name of HDF5 file. Should be specitied without file extention
- `dataset_name` name of dataset inside the HDF5 file


