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
    dados = os.listdir('/home/vinicius/WebService/WebService-LIME/api_lime/my_app/data')
    return render_template("gallery.html", image_names=dados)


@app.route('/tabular/<filename>')
def send_image(filename):
    return send_from_directory("data", filename)

@app.route('/gallery')
def get_gallery():
    #image_names = os.listdir('./data')
    #print(image_names)
    return render_template("gallery.html", image_names=['fig1.jpg', 'fig2.jpg', 'fig3.jpg', 'fig4.jpg'])

