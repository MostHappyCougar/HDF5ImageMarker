from config_parser import xml_parser
import image_import
import marking
import dataset_shapes_validation


img_parameters = xml_parser().get_conf_params()

test = dataset_shapes_validation.DatasetValudation(img_parameters)

dataset = image_import.ImageImport(img_parameters["source_folder"], img_parameters["width"], img_parameters["height"])

mrk = marking.ImgMarking(dataset.import_image(), img_parameters["output_folder"], img_parameters["out_file_name"], img_parameters["out_dataset_name"], img_parameters["marks_count"])

mrk.open_first_img()