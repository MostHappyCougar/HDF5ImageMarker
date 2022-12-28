import hdf5_exporter
from matplotlib import pyplot as plt
from config_parser import out_folder_path, window_size_w, window_size_h, marks_counts

def marking(data):
    fig, (ax1) = plt.subplots(1, 1, figsize = (window_size_w, window_size_h))
    
    ax1.set(title="Imported Image")
    ax1.imshow(data.permute(1,2,0))
    imp_img=data.permute(1,2,0)
    
    tt=[]
    def on_click_event(event):
        tt.append([round(event.xdata, 0), round(event.ydata, 0)])
        if len(tt) == marks_counts:
            hdf5_exporter.expore_image(out_folder_path, imp_img, tt)
            tt.clear()
    
    fig.canvas.mpl_connect('button_press_event', on_click_event)
    plt.show() 