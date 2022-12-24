import hdf5_exporter
from matplotlib import pyplot as plt
import config_parser

def marking(data):
    fig, (ax1) = plt.subplots(1, 1, figsize = (config_parser.window_size_w, config_parser.window_size_h))
    
    ax1.set(title="Imported Image")
    ax1.imshow(data.permute(1,2,0))
    imp_img=data.permute(1,2,0)
    
    def on_click_event(event):
        hdf5_exporter.expore_image(config_parser.out_folder_path, imp_img, round(event.xdata, 0), round(event.ydata, 0))
    
    fig.canvas.mpl_connect('button_press_event', on_click_event)
    plt.show() 