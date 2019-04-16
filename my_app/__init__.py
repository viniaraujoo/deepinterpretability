from flask import Flask, session, redirect, url_for, escape, request, render_template
from lime_app.app_back import impl
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('templates')
@app.route('/', methods=['POST'])
def method_name():
    url1 = request.form.get('model')
    url2 = request.form.get('example')
    impl.explanation_image(url1,url2)
    return app.send_static_file("index.hml")

@app.route('/tabular', methods=['GET'])
def render_static():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'fig.jpg')

    return render_template("index.html",user_image = full_filename)

