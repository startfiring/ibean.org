from flask import Flask
from flask import render_template
from flask import request

import os
import json
from string import Template 

if ("AZUREFILE" in os.environ and os.environ['AZUREFILE']):
    app = Flask(__name__, static_url_path="/", static_folder="/mnt/azure/static")
    dynamicPath = os.environ['AZUREFILE'] + "/dynamic"
else:
    app = Flask(__name__, static_url_path="/", static_folder="./static")
    dynamicPath = "./dynamic"

@app.route('/')
@app.route('/index')
@app.route('/education')
@app.route('/projects')
@app.route('/blogs')
def index():
    with open(dynamicPath + '/index.json', 'r') as indexJson:
        indexStream = indexJson.read()

    indexConfig = json.loads(indexStream)
    return render_template('index.html', title='kang zian', exams = indexConfig["exams"], projects = indexConfig["projects"][:6], photogroups = indexConfig["photogroups"][:6])

@app.route('/photos')
def photoindex():
    with open(dynamicPath + '/index.json', 'r') as photoJson:
        photoStream = photoJson.read()

    photoConfig = json.loads(photoStream)
    return render_template('photoindex.html', title='kangzian - Footprint', photoGroups = photoConfig["photogroups"])

@app.route('/photos/tags')
def photolist():

    tags = request.full_path.replace("/photos/tags?","")

    with open(dynamicPath + '/photos.json', 'r') as photoJson:
        photoStream = photoJson.read()
    photoTags = json.loads(photoStream)

    filterPhotos = [photo for photo in photoTags if tags in photo["tags"] ]
    return render_template('photolist.html', title='kangzian - Footprint' + tags, photos = filterPhotos)

if __name__ == '__main__':
    app.run()