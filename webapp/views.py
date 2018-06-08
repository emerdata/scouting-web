from flask import Flask

from webapp import app

@app.route('/')
def hello_world():
    return '<!DOCTYPE HTML><html><head></head><body><h1>Hello!</h1><p>Hello, World!</p></body></html>'