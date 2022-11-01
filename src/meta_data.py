#extract metadata from webp images
from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open("ImageGenerations/generation-0HxY8mvKWeH9Pj50P4Rcf2FQ.webp")
exifdata = image.getexif()

for tagid in exifdata:

    tagename = TAGS.get(tagid, tagid)
    value = exifdata.get(tagid)
    print(f"{tagname:25}: {value}")

