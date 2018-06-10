from flask import Flask, send_from_directory, render_template, request

from webapp import app

@app.route('/api/login', methods=['POST'])
def login():
    pass

@app.route('/api/logout', methods=['POST'])
def logout():
    pass

@app.route('/api/teams', methods=['GET'])
def teams():
    pass

@app.route('/api/events', methods=['GET'])
def events():
    pass

@app.route('/api/matches', methods=['GET'])
def matches():
    pass

@app.route('/api/team/<int:team_number>', methods=['GET'])
def team(team_number):
    pass

@app.route('/api/event/<event_id>', methods=['GET'])
def event(event_id):
    pass

@app.route('/api/match/<int:match_id>', methods=['GET'])
def math(match_id):
    pass