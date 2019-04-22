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
    url_model = request.form.get('model')
    url_example = request.form.get('example')
    top_labels = request.form.get('top_labels')
    num_samples = request.form.get('num_samples')
    hide_color = request.form.get('hide_color')
    impl.explanation_image(url_model,url_example,top_labels,hide_color,num_samples)
    imgs = [top_labels]
    for i in range(top_labels):
        imgs[i] = 'fig%d.jpg' % n

    return render_template("gallery.html", image_names=imgs)





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

