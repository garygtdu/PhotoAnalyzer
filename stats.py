from exif_extractor import readable_data, field_finder, camera_settings, field_list
from collections import Counter
import matplotlib.pyplot as plt


# organizes camera settings to plot on a chart later

def setting_list(field_list: list, camera_settings: list):
        
        setting_storage = {}

        for field_name in field_list: 

            setting_values = []

            for entry in camera_settings: 

                if field_name in entry:
                     
                    setting_values.append(entry[field_name])

            setting_storage[field_name] = setting_values

        return setting_storage            

settings = setting_list(field_list, camera_settings)
# print(settings)
                