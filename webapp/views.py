from flask import Flask, send_from_directory, render_template, request

from webapp import app

@app.route('/')
def hello_world():
    name = request.args.get('name', None)
    return render_template('hello.html', name=name)

@app.route('/favicon.ico')
def favicon_route():
    return send_from_directory('static', 'favicon.ico')