class InvalidHeight(Exception):
    def __init__(self, actual):
        self.message = f"Value of '<img_h>' in config must be filled and be greater than zero! (Actually: {actual})"
    def __str__(self):
        return self.message

class InvalidWidth(Exception):
    def __init__(self, actual):
        self.message = f"Value of '<img_w>' in config must be filled and be greater than zero! (Actually: {actual})"
    def __str__(self):
        return self.message


class InvalidMarksCount(Exception):
    def __init__(self, actual):
        self.message = f"Value of '<marks_count>' tag must be filled and be greater than zero! (Actually: {actual})"
    def __str__(self):
        return self.message
    
class InvalidSourceFolderName(Exception):
    def __init__(self, actual):
        self.message = f"Value of '<source_folder>' tag must be filled and starts with no space! (Actually: '{actual}')"
    def __str__(self):
        return self.message

class InvalidOutputFolderName(Exception):
    def __init__(self, actual):
        self.message = f"Value of '<output_folder>' tag must be filled and starts with no space! (Actually: '{actual}')"
    def __str__(self):
        return self.message
    
class InvalidOutputFileName(Exception):
    def __init__(self, actual):
        self.message = f"Value of '<file_name>' tag must be filled and starts with no space! (Actually: '{actual}')"
    def __str__(self):
        return self.message
    
class InvalidDatasetName(Exception):
    def __init__(self, actual):
        self.message = f"Value of '<dataset_name>' tag must be filled and starts with no space! (Actually: '{actual}')"
    def __str__(self):
        return self.message

class InvalidSourceStructure(Exception):
    def __init__(self):
        self.message = "In the source folder must be at least one subdirectory with content there. Content directly in source folder is not valid"
    def __str__(self):
        return self.message


            