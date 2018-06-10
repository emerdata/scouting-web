from flask import Flask, send_from_directory, render_template, request

from webapp import app

@app.route('/api/login', methods=['POST'])
def login():
    pass

@app.route('/api/logout', method=['POST'])
def logout():
    pass

@app.route('/api/teams', method=['GET'])
def teams():
    pass

@app.route('/api/events', method=['GET'])
def events():
    pass

@app.route('/api/matches', method=['GET'])
def matches():
    pass

@app.route('/api/team/<int:team_number>', method=['GET'])
def team(team_number):
    pass

@app.route('/api/event/<event_id>', method=['GET'])
def event(event_id):
    pass

@app.route('/api/match/<int:match_id>', method=['GET'])
def math(match_id):
    pass