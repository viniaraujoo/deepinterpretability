from flask import Flask, session, redirect, url_for, escape, request
from lime_app.app_back import impl
app = Flask(__name__)

@app.route('/', methods=['POST'])
def method_name():
    url1 = request.form.get('model')
    url2 = request.form.get('example')
    return impl.explanation_image(url1,url2)