from flask import Flask, session, redirect, url_for, escape, request, render_template, send_from_directory
from flask_pymongo import PyMongo
from lime_app.app_back import impl
import os
from keras.models import load_model
from keras.metrics import top_k_categorical_accuracy
import gridfs
import requests

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
@app.route("/uploads", methods=["POST"])
def save_upload():
    url_model = request.form.get('model')
    
    return 'ok'

def top_2_accuracy(in_gt, in_pred):
    return top_k_categorical_accuracy(in_gt, in_pred, k=2)

@app.route("/explanation", methods=["GET"])
def explanation():
    return 'ok'

@app.route('/image')
def method_image():
    os.mkdir('./my_app/data')
    url_model = request.form.get('model')
    url_example = request.form.get('example')
    top_labels = int(request.form.get('top_labels'))
    num_samples = int(request.form.get('num_samples'))
    hide_color = int(request.form.get('hide_color'))
    impl.explanation_image(url_model,url_example,top_labels,hide_color,num_samples)
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
def load_model(url):
    file_bd = gridfs.GridFS(mongo.db, collection="modelh5")
    for grid_out in file_bd.find({"filename" : url}):
        data = grid_out.read()
    
    with open('modelbd.h5','wb') as pl:
        pl.write(data)
    model = load_model('./modelbd.h5')
    return model
    

'''
@app.route("/load", methods=["GET"])
def load_model():
    m = mongo.db.fs.files.find()
    b = gridfs.GridFS(mongo.db, collection="modelh5")
    for grid_out in b.find({"filename" : "model"}):
        data = grid_out.read()
    
    with open('teste.h5','wb') as pl:
        pl.write(data)
    #fs = gridfs.GridFS(mongo.db)
    #print(dir(m))
    return 'ok'

'''
