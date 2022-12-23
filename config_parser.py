import xml.etree.ElementTree as ET
from os import path
from ErrorHandler import iss_handler

dirname = path.dirname(__file__)
conf_path = path.join(dirname, "config.xml")

conf = ET.parse(conf_path)
root = conf.getroot()

for tags_conf in root.findall("conf"):
    width = int(tags_conf.find("img_w").text) if int(tags_conf.find("img_w").text) > 0 else iss_handler("Config Error", "img_w must be greater than zero!", 1)
    height = int(tags_conf.find("img_h").text) if int(tags_conf.find("img_h").text) > 0 else iss_handler("img_h must be greater than zero!")
    window_size_w = int(tags_conf.find("window_size_w").text) if int(tags_conf.find("window_size_w").text) > 0 else iss_handler("Config Error", "window_size_w must be greater than zero!", 1)
    window_size_h = int(tags_conf.find("window_size_h").text) if int(tags_conf.find("window_size_h").text) > 0 else iss_handler("Config Error", "window_size_h must be greater than zero!", 1)
    
    if path.exists(tags_conf.find("source_folder").text) == True:
        source_folder = tags_conf.find("source_folder").text
    elif tags_conf.find("source_folder").text.startswith(" "): iss_handler("Config Error", "Path to source_folder must not begins with space", 1)
    elif path.exists(tags_conf.find("source_folder").text) == False: iss_handler("Config Error", "source_folder "+"'"+tags_conf.find("source_folder").text+"'" + " not found!", 1) 
    
    if path.exists(tags_conf.find("output_folder").text) == True:
        output_folder = tags_conf.find("output_folder").text
    elif tags_conf.find("output_folder").text.startswith(" "): iss_handler("Config Error", "Path to source_folder must not begins with space")
    elif path.exists(tags_conf.find("output_folder").text) == False: iss_handler("Config Error", "output_folder "+"'"+tags_conf.find("output_folder").text+"'" + " not found!", 1) 
    
for tags_logs in root.findall("logs"):
    log_folder = tags_logs.find("log_folder").text
    import_logs = tags_logs.find("import_logs").text
    