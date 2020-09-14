import json

with open('./dynamic/photos.json', 'r') as photoJson:
        photoStream = photoJson.read()

photoTags = json.loads(photoStream)

filterPhotos = [photo for photo in photoTags if "us" in photo["tags"] ]

print(filterPhotos)