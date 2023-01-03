# Decription
With this util you can mark up any key points of the image and write down all pairs image-marks_list into the HDF5 file
## How to use
1. Create your input folder where the images for marking will be take from
    - This folder should be created upon the directory the `torch_importer.py` is stored in
2. Create subdirectory in this folder and put your image set into this subdirectory
3. Set the name of input folder into the `<source_folder>` tag of `config.xml` file
4. Create output folder upon directory the `torch_importer.py` is stored in
5. Set the name of output folder into the `<output_folder>` tag of `config.xml` file

Now you can use this util via running `torch_importer.py` as regular python script
## Detail configuring
You can also configurate some parameters of marking via `config.xml`. Be aware changing any parameters when `torch_importer.py` is still running is not prodlike scenario. You may change any parameter in `config.xml` only before `torch_importer.py` is ran.
### Parameters overview
- `img_w` and `img_h` - the sizes that an each image will be resized to. `img_w` is image width, `img_h` is image height
- `window_size_w` and `window_size_h` - It's aboout size of window an each image will be show upon
- `source_folder` - The folder that images for marking is store in
- `output_folder` - the folder where the HDF5 file will be save
- `marks_counts` - count of poits that will be marked up
- `file_name` - name of HDF5 file. Should be specitied without file extention
- `dataset_name` name of dataset inside the HDF5 file

Parameters that have no mentioned have no impact at this moment


