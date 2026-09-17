# Extracting exif from photo files
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
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

print(photodata)