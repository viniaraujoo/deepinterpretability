from flask import Flask, session, redirect, url_for, escape, request, render_template, send_from_directory
from lime_app.app_back import impl
import os

__author__ = 'viniaraujoo'


app = Flask(__name__,static_folder="data")


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


file_caminho = os.path.join('WebService-LIME')


app.config['UPLOAD_FOLDER'] = os.path.join('WebService-LIME')


@app.route('/', methods=['POST'])
def method_name():
    url1 = request.form.get('model')
    url2 = request.form.get('example')
    impl.explanation_image(url1,url2)
    return app.send_static_file("index.hml")





@app.route('/tabular', methods=['GET'])
def render_static():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fig1.jpg')
    
    
    return render_template("index.html",image_name = 'fig1.jpg')


@app.route('/tabular/<filename>')
def send_image(filename):
    return send_from_directory("data", filename)

@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./data')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

