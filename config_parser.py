import xml.etree.ElementTree as ET
from os import path

dirname = path.dirname(__file__)
conf_path = path.join(dirname, "config.xml")

conf = ET.parse(conf_path)
root = conf.getroot()

for tags_conf in root.findall("conf"):
    width = tags_conf.find("img_w").text
    height = tags_conf.find("img_h").text
    window_size_w = tags_conf.find("window_size_w").text
    window_size_h = tags_conf.find("window_size_h").text
    source_folder = tags_conf.find("source_folder").text
    output_folder = tags_conf.find("output_folder").text
    
for tags_logs in root.findall("logs"):
    log_folder = tags_logs.find("log_folder").text
    import_logs = tags_logs.find("import_logs").text