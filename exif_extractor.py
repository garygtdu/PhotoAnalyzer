# Extracting exif from photo files
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS, GPS
from pathlib import Path
import os


photodata = []

for photofile in os.listdir("Photos"):
    with Image.open(Path("Photos") / photofile) as file:
        exif_data = file._getexif()
        if exif_data is None:
            continue
        else: 
            photodata.append(exif_data)


def exif_extractor(data: list):

    datalibrary = []

    for entry in data:

        individual_photo = {}

        for tag, value in entry.items():
            individual_photo[TAGS[tag]] = value
        datalibrary.append(individual_photo)

    return datalibrary

readable_data = exif_extractor(photodata)



# Camera settings finder!!!

def field_finder(readable_data: list, field_list: list):

    setting = []

    for entry in readable_data:

        photo_dict = {}

        for field_name in field_list: 

            if field_name in entry:
                photo_dict[field_name] = entry[field_name]

        setting.append(photo_dict)
    
    return setting


# Test!!
field_list = ['ISOSpeedRatings', 'FNumber', 'ShutterSpeedValue', 'FocalLength']
camera_settings = field_finder(readable_data, field_list)
# print(camera_settings)

