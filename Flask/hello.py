import json
import pathlib
from pathlib import Path
from flask import Flask, Response, request
from City import City
import requests

def file_put_contents(pathfile, strdata=""):
    try:
        with open(pathfile, 'w') as f:
            f.write(strdata)
    except IOError:
        return f"no file found: {pathfile}"

KEY_GOOGLE = ''
app        = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response

@app.route('/test')
def test():
    city     = request.args.get('city').strip().lower().replace(' ', '+').replace('++', '+')
    newClass = City()
    resultData = newClass.existThisCity(city)
    if resultData == "False":
        return Response(response=resultData, mimetype='text/html')


@app.route("/")
def index():
    pathlib.Path('storage').mkdir(parents=True, exist_ok=True)
    city       = request.args.get('city').strip().lower().replace(' ', '+').replace('++', '+')
    city_url   = 'storage/'+city+'.json'
    city_url   = city_url.replace('+', '')

    my_file = Path(city_url)
    if my_file.exists():
        fileA = open(city_url, "r")
        dataA = fileA.read()
        return Response(response=dataA, mimetype='application/json')

    result     = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=Spain+'+city+'&key='+KEY_GOOGLE)
    parsed     = json.loads(result.content)
    PLACE_ID   = parsed["results"][0]["place_id"]
    res_images = requests.get('https://maps.googleapis.com/maps/api/place/details/json?place_id='+PLACE_ID+'&radius=10000&key='+KEY_GOOGLE)
    parsed_img = json.loads(res_images.content)
    parsed_img = parsed_img["result"]["photos"]

    list_img   = []

    for object_image in parsed_img:
        img_ref  = object_image["photo_reference"]
        list_img.append(img_ref)

    file_put_contents(city_url, json.dumps({"images": list_img}))
    fileA = open(city_url, "r")
    dataA = fileA.read()
    return Response(response=dataA, mimetype='application/json')


@app.route("/show_image/<string:img_ref>/")
def show_image(img_ref):
    img_link = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=99999&photo_reference='+img_ref+'&key='+KEY_GOOGLE
    img_content = requests.get(img_link)
    return Response(img_content.content, mimetype='image/jpeg')



"""
user_: imagedeveloper
email: xboss.developer@gmail.com
pass : svoboda2019A.
"""
