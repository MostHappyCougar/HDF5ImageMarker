import xml.etree.ElementTree as ET
from os import path
from ErrorHandler import iss_handler

dirname = path.dirname(__file__)
conf_path = path.join(dirname, "config.xml")

conf = ET.parse(conf_path)
root = conf.getroot()

for tags_conf in root.findall("conf"):
    width = int(tags_conf.find("img_w").text) if int(tags_conf.find("img_w").text) > 0 else iss_handler("Config Error", "img_w must be greater than zero!", "conf_err01")
    height = int(tags_conf.find("img_h").text) if int(tags_conf.find("img_h").text) > 0 else iss_handler("Config Error", "img_h must be greater than zero!", "conf_err01")
    window_size_w = int(tags_conf.find("window_size_w").text) if int(tags_conf.find("window_size_w").text) > 0 else iss_handler("Config Error", "window_size_w must be greater than zero!", "conf_err02")
    window_size_h = int(tags_conf.find("window_size_h").text) if int(tags_conf.find("window_size_h").text) > 0 else iss_handler("Config Error", "window_size_h must be greater than zero!", "conf_err02")
    
    src_folder_path = path.join(dirname, tags_conf.find("source_folder").text) #Source Folder abs path
    out_folder_path = path.join(dirname, tags_conf.find("output_folder").text) #Output Folder abs path
    
    if path.exists(src_folder_path) == True:
        source_folder = tags_conf.find("source_folder").text
    elif tags_conf.find("source_folder").text.startswith(" "): iss_handler("Config Error", "Path to source_folder must not begins with space", "conf_err04")
    elif path.exists(src_folder_path) == False: iss_handler("Config Error", "source_folder "+"'"+tags_conf.find("source_folder").text+"'" + " not found!", "conf_err05") 
    
    if path.exists(out_folder_path) == True:
        output_folder = tags_conf.find("output_folder").text
    elif tags_conf.find("output_folder").text.startswith(" "): iss_handler("Config Error", "Path to source_folder must not begins with space", "conf_err06")
    elif path.exists(out_folder_path) == False: iss_handler("Config Error", "output_folder "+"'"+tags_conf.find("output_folder").text+"'" + " not found!", "conf_err07") 
    