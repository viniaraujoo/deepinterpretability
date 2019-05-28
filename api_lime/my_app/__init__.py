from flask import Flask, session, redirect, url_for, escape, request, render_template, send_from_directory, send_file
from flask_pymongo import PyMongo
from lime_app.app_back import impl
import os
import gridfs
import requests
import sklearn
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from keras.applications import inception_v3 as inc_net
from keras.models import load_model
from keras.metrics import top_k_categorical_accuracy
import zipfile
import io
from zipfile import ZipFile 

__author__ = 'viniaraujoo'


app = Flask(__name__,static_folder="data")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))


file_caminho = os.path.join('WebService-LIME')

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

app.config['UPLOAD_FOLDER'] = os.path.join('WebService-LIME')


@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
        online_users=online_users)


# Recebe a url e salva o modelo no banco de dados e retornar o filename do modelo.
@app.route("/uploadmodel", methods=["POST"])
def save_upload():
    url_model = request.form.get('model')
    return save_model(url_model)

@app.route("/explanationlime", methods=["GET"])
def explanation_lime():
    #os.mkdir('./my_app/data')
    url_model = request.form.get('model')
    url_example = request.form.get('example')
    top_labels = int(request.form.get('top_labels'))
    num_samples = int(request.form.get('num_samples'))
    hide_color = int(request.form.get('hide_color'))
    model = load_model_url(url_model)
    example = load_example(url_example)
    impl.expalantion_model_lime_image(model,example,top_labels,hide_color,num_samples)
    imgs = os.listdir('./my_app/data')

    return render_template("gallery.html", image_names=imgs)




@app.route('/gallery/<filename>')
def send_image(filename):
    return send_from_directory("data", filename)

@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./my_app/data')
    
    return render_template("gallery.html", image_names=image_names)



#Responsible function to download and save the template in the mongodb database
def save_model(url):
    model = requests.get(url).content
    with open(os.path.join('model.h5'), 'wb') as handler:
        handler.write(model)
    file = open('./model.h5', 'rb')
    mongo.save_file(filename=url, fileobj=file,base='modelh5')
    file.close()
    return url

#Responsible function to load model in bd
def load_model_url(url):
    file_bd = gridfs.GridFS(mongo.db, collection="modelh5")
    for grid_out in file_bd.find({"filename" : url}):
        data = grid_out.read()
    
    with open('modelbd.h5','wb') as pl:
        pl.write(data)
    pl.close()
    
    model = tf.keras.models.load_model('./modelbd.h5')
    return model
    
def load_example(url):
    exemple = requests.get(url).content
    with open(os.path.join('image.jpg'), 'wb') as handler:
        handler.write(exemple)
    image = transform_img_fn([os.path.join('image.jpg')])
    return image

def transform_img_fn(path_list):
    #Transform image so it can be processed by inception.
    out = []
    for img_path in path_list:
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = inc_net.preprocess_input(x)
        out.append(x)
    return np.vstack(out)


@app.route('/shap')
def explanation_shap():
    model_url = request.form.get('model')
    train_url = request.form.get('train')
    example_url = request.form.get('example')
    model = load_model_url(model_url)
    train  = load_numpy_file(train_url)
    example = load_numpy_file(example_url)
    impl.expalantion_model_shap_image(model,train,example)

    return send_file('result.jpg', mimetype='image')


'''
This function aims to download the training set used to explain SHAP and a numpy file load
'''
def load_numpy_file(url):
    exemple = requests.get(url).content
    with open(os.path.join('numpy.zip'), 'wb') as handler:
        handler.write(exemple)
    with ZipFile('numpy.zip', 'r') as zip:
        file = zip.namelist()
        zip.extractall()
    array = np.load('./' + file[0]) 
    return array


