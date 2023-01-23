from matplotlib import pyplot as plt
import hdf5_exporter

class ImgMarking():
    def __init__(self, images_dataset: "DataLoader", out_folder: str, file_name: str, dataset_name: str, marks_counts: int):
        self.__images = images_dataset
        self.__out_folder = out_folder
        self.__file_name = file_name
        self.__dataset_name = dataset_name
        self.__marks_counts = marks_counts
        self.__marks_coords=[]
        self.__markers=[]
        self.__exporter = hdf5_exporter.hdf5_exporter(self.__out_folder, self.__file_name, self.__dataset_name)
        self.__curent_image_id = 1
        return
        
        
    def open_first_img(self) -> None:
        fig, (ax1) = plt.subplots(1, 1, figsize = (16, 8))
        fig.canvas.manager.set_window_title('HDF5ImageMarker')
        ax1.set(title=f"Imported Image 1/{len(self.__images)}; OutFileName: {self.__file_name}; DatasetName: {self.__dataset_name} \n Marks Available: {self.__marks_counts - len(self.__marks_coords)}/{self.__marks_counts}")
        ax1.imshow(list(self.__images)[0][0][0].permute(1,2,0))
        
        def on_click_event(event) -> None:
            if len(self.__marks_coords) < self.__marks_counts:
                self.__marks_coords.append([round(event.xdata, 0), round(event.ydata, 0)])
                self.__markers.extend(ax1.plot(round(event.xdata, 0), round(event.ydata, 0), marker='2', markersize=24))
                ax1.set(title=f"Imported Image {self.__curent_image_id}/{len(self.__images)}; OutFileName: {self.__file_name}; DatasetName: {self.__dataset_name} \n Marks Available: {self.__marks_counts - len(self.__marks_coords)}/{self.__marks_counts}")
                plt.draw()
            return
        
        
        def on_enter_press(event) -> None:
            if event.key == 'enter':
                if len(self.__marks_coords) == self.__marks_counts and self.__curent_image_id < len(self.__images):            
                    self.__exporter.export_image(list(self.__images)[self.__curent_image_id-1][0][0], self.__marks_coords)
                    self.__marks_coords.clear()
                    del self.__marks_coords[:]
                    self.__markers.clear()
                    del self.__markers[:]   
                    plt.cla() 
                    ax1.set(title=f"Imported Image {self.__curent_image_id+1}/{len(self.__images)}; OutFileName: {self.__file_name}; DatasetName: {self.__dataset_name} \n Marks Available: {self.__marks_counts - len(self.__marks_coords)}/{self.__marks_counts}")
                    ax1.imshow(list(self.__images)[self.__curent_image_id][0][0].permute(1,2,0))
                    plt.draw()
                    self.__curent_image_id += 1
                
                elif self.__curent_image_id == len(self.__images):
                    self.__exporter.export_image(list(self.__images)[self.__curent_image_id-1][0][0], self.__marks_coords)
                    plt.clf()
                    plt.draw()
            return
        
        
        def on_z_press(event) -> None:
            if event.key == 'z':
                if len(self.__marks_coords) > 0 and len(self.__markers) > 0:
                    del self.__marks_coords[-1]
                    self.__markers[-1].remove()
                    del self.__markers[-1]
                    ax1.set(title=f"Imported Image {self.__curent_image_id}/{len(self.__images)}; OutFileName: {self.__file_name}; DatasetName: {self.__dataset_name} \n Marks Available: {self.__marks_counts - len(self.__marks_coords)}/{self.__marks_counts}")
                    plt.draw()
            return
           
                         
        fig.canvas.mpl_connect('button_press_event', on_click_event)
        fig.canvas.mpl_connect('key_press_event', on_enter_press)
        fig.canvas.mpl_connect('key_press_event', on_z_press)
        plt.show()
        return