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
print(readable_data)


    
# each item in photodata is a DICT
# TAGS[this is where the values go]; TAGS is a dictionary 