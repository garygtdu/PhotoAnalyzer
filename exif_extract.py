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

# ISO

def ISO_finder(readable_data: list):

    individual_ISO = []

    for entry in readable_data:
        
        individual_ISO.append(entry['ISOSpeedRatings'])

    return individual_ISO

ISO_data = ISO_finder(readable_data)
print(ISO_data)

