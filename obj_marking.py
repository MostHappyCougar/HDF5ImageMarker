import hdf5_exporter
from matplotlib import pyplot as plt
import config_parser

def marking(data):
    fig, (ax1) = plt.subplots(1, 1, figsize = (int(config_parser.window_size_w), int(config_parser.window_size_h)))
    ax1.set(title="Imported Image")
    ax1.imshow(data.permute(1,2,0))
    plt.show()
     