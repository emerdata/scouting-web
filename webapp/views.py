from flask import Flask, send_from_directory

from webapp import app

@app.route('/')
def hello_world():
    return '<!DOCTYPE HTML><html><head><title>Emerdata, or something</title></head><body><h1>Hello!</h1><p>Hello, World!</p></body></html>'

@app.route('/favicon.ico')
def favicon_route():
    return send_from_directory('static', 'favicon.ico')