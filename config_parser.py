import xml.etree.ElementTree as ET

conf = ET.parse("config.xml")
root = conf.getroot()

for tags_conf in root.findall("conf"):
    height = tags_conf.find("img_h").text
    width = tags_conf.find("img_w").text
    window_size_h = tags_conf.find("window_size_h").text
    window_size_w = tags_conf.find("window_size_w").text
    source_folder = tags_conf.find("source_folder").text
    output_folder = tags_conf.find("output_folder").text
    
for tags_logs in root.findall("logs"):
    log_folder = tags_logs.find("log_folder").text
    import_logs = tags_logs.find("import_logs").text