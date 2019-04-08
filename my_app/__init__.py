from flask import Flask, session, redirect, url_for, escape, request
from lime_app.app_back import impl
app = Flask(__name__)

@app.route('/', methods=['POST'])
def method_name():
    url = request.form.get('url')
    return impl.get_image(url)