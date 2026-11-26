# Extracting exif from photo files
from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS, GPSTAGS, GPS, IFD
from pathlib import Path


photodata = []

for photofile in Path("Photos").iterdir():
    try:
        with Image.open(photofile) as img:

            exif = img.getexif()
            exif_data = dict(exif)
            exif_data.update(exif.get_ifd(IFD.Exif))

    except (UnidentifiedImageError, IsADirectoryError):
        continue
    if exif_data:
        photodata.append(exif_data)


def exif_extractor(data: list):

    datalibrary = []

    for entry in data:

        individual_photo = {}

        for tag, value in entry.items():
            individual_photo[TAGS.get(tag, tag)] = value
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
field_list = ['ISOSpeedRatings', 'FNumber', 'ExposureTime', 'FocalLength']
camera_settings = field_finder(readable_data, field_list)
# print(camera_settings)

