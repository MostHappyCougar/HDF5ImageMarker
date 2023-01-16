import xml.etree.ElementTree as ET
from os import path
from ErrorHandler import iss_handler

dirname = path.dirname(__file__)
conf_path = path.join(dirname, "config.xml")

conf = ET.parse(conf_path)
root = conf.getroot()

for tags_conf in root.findall("conf"):
    '''WIDTH OF IMAGES'''
    try:
        width = int(tags_conf.find("img_w").text) if int(tags_conf.find("img_w").text) > 0 else iss_handler("Config Error", "img_w must be greater than zero!", "conf_err01")
    except ValueError:
        iss_handler("Config Error", "img_w must be an integer!", "conf_err011")
    except TypeError:
        iss_handler("Config Error", "img_w must be filled!", "conf_err012")
    
    
    '''HIGHT OF IMAGES'''
    try:
        height = int(tags_conf.find("img_h").text) if int(tags_conf.find("img_h").text) > 0 else iss_handler("Config Error", "img_h must be greater than zero!", "conf_err01")
    except ValueError:
        iss_handler("Config Error", "img_h must be an integer!", "conf_err011")
    except TypeError:
        iss_handler("Config Error", "img_h must be filled!", "conf_err012")
    
    
    window_size_w = int(tags_conf.find("window_size_w").text) if int(tags_conf.find("window_size_w").text) > 0 else iss_handler("Config Error", "window_size_w must be greater than zero!", "conf_err02")
    window_size_h = int(tags_conf.find("window_size_h").text) if int(tags_conf.find("window_size_h").text) > 0 else iss_handler("Config Error", "window_size_h must be greater than zero!", "conf_err02")
    
    try:
        src_folder_path = path.join(dirname, tags_conf.find("source_folder").text) #Source Folder abs path
        out_folder_path = path.join(dirname, tags_conf.find("output_folder").text) #Output Folder abs path
    except TypeError:
        iss_handler("Config Error", "source_folder and output_file must not be empty!", "conf_err14")
    
    
    '''MARKS COUNTS'''
    try:
        marks_counts=int(tags_conf.find("marks_counts").text) if int(tags_conf.find("marks_counts").text) > 0 else iss_handler("Config Error", "marks_counts must be greater than zero!", "conf_err08")
    except TypeError:
        iss_handler("Config Error", "marks_counts must be filled!", "conf_err09")
    except ValueError:
        iss_handler("Config Error", "marks_counts must be an integer!", "conf_err10")
    
    
    '''SOURCE FOLDER'''
    if path.exists(src_folder_path) == True:
        source_folder = tags_conf.find("source_folder").text
    elif tags_conf.find("source_folder").text.startswith(" "): iss_handler("Config Error", "Path to source_folder must not begins with space", "conf_err04")
    elif path.exists(src_folder_path) == False: iss_handler("Config Error", "source_folder "+"'"+tags_conf.find("source_folder").text+"'" + " not found!", "conf_err05") 
    
    
    '''OUTPUT FOLDER'''
    if path.exists(out_folder_path) == True:
        output_folder = tags_conf.find("output_folder").text
    elif tags_conf.find("output_folder").text.startswith(" "): iss_handler("Config Error", "Path to source_folder must not begins with space", "conf_err06")
    elif path.exists(out_folder_path) == False: iss_handler("Config Error", "output_folder "+"'"+tags_conf.find("output_folder").text+"'" + " not found!", "conf_err07") 
    
    
    '''OUTPUT FILE'''
    for file_conf in tags_conf.findall("output_file"):
        try:
            filename = file_conf.find("file_name").text+".h5" if file_conf.find("file_name").text.startswith(" ") == False else iss_handler("Config Error", "file_name must starts with no space!", "conf_err11")
        except AttributeError:
            iss_handler("Config Error", "file_name must be not empty!", "conf_err11")
        try:
            dataset = file_conf.find("dataset_name").text if file_conf.find("dataset_name").text.startswith(" ") == False else iss_handler("Config Error", "dataset_name must starts with no space!", "conf_err12")
        except AttributeError:
            iss_handler("Config Error", "dataset_name must be not empty!", "conf_err12")
        
        try:
            mode = file_conf.find("write_mode").text if file_conf.find("write_mode").text in ('w', 'a') else iss_handler("Config Error", "mode must be 'w' of 'a'!", "conf_err13")
        except AttributeError:
            iss_handler("Config Error", "write_mode must be not empty!", "conf_err13")
            
            
            
            
            