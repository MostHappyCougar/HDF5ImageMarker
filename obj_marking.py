import hdf5_exporter
from matplotlib import pyplot as plt
from config_parser import out_folder_path, window_size_w, window_size_h, marks_counts

def marking(data):
    fig, (ax1) = plt.subplots(1, 1, figsize = (window_size_w, window_size_h))
    fig.canvas.manager.set_window_title('HDF5ImageMarker')
    ax1.set(title="Imported Image")
    ax1.imshow(data.permute(1,2,0))
    imp_img=data.permute(1,2,0)
    
    marks_coords=[]
    markers=[]
    def on_click_event(event):
        if len(marks_coords) < marks_counts:
            marks_coords.append([round(event.xdata, 0), round(event.ydata, 0)])
            markers.extend(ax1.plot(round(event.xdata, 0), round(event.ydata, 0), marker='2', markersize=24))
            plt.draw()
        elif len(marks_coords) == marks_counts:
            print("\n###################################################################################")
            print("No available marks for the image! The pair might be saved. Press 'Ender' to save")
            print("###################################################################################\n")
    
    def on_enter_press(event):
        if event.key == 'enter':
            if len(marks_coords) == marks_counts:
                hdf5_exporter.expore_image(out_folder_path, imp_img, marks_coords)
                marks_coords.clear()
                plt.close()
                print("\n###################################################################################")
                print("Pair Image-Marks has been succesfully saved!")
                print("###################################################################################\n")
            else:
                print("Not all marks has been marked up!")
                print("Must be marked up " + str(marks_counts - len(marks_coords)) + " marks")
    def on_z_press(event):
        if event.key == 'z':
            del marks_coords[-1]
            markers[-1].remove()
            del markers[-1]
            plt.draw()
        
    fig.canvas.mpl_connect('button_press_event', on_click_event)
    fig.canvas.mpl_connect('key_press_event', on_enter_press)
    fig.canvas.mpl_connect('key_press_event', on_z_press)
    plt.show()