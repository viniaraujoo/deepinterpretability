from flask import Flask, session, redirect, url_for, escape, request
from lime_app.app_back import impl
app = Flask(__name__)

@app.route('/', methods=['GET'])
def method_name():
    return impl.status()