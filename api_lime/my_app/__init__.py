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
    top_labels = int(request.form.get('top_labels'))
    impl.explanation_image(url_model,url_example,top_labels)
    #imgs = os.listdir('./my_app/data')
    return render_template("gallery.html", image_names=['fig0.jpg','fig1.jpg', 'fig2.jpg', 'fig3.jpg', 'fig4.jpg'])


@app.route('/image')
def method_image():
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

