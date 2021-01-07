import flask
from flask import request, jsonify

from flask_cors import CORS

import mysql.connector

import ww

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


connection = mysql.connector.connect(
    host='127.0.0.1', port='3307', database='checkin', user='root', password=ww.password)
myCursor = connection.cursor(dictionary=True)


@app.route('/api/checkins/<int:checkin_id>', methods=['GET'])
def checkin_fetch(checkin_id):
    myCursor.execute('SELECT * FROM checkins WHERE Checkin_ID = {}'.format(checkin_id))
    myResults = myCursor.fetchall()
    return jsonify(myResults), 200, {'ContentType': 'application/json'}

@app.route('/api/checkins/squad/<int:squad_id>', methods=['GET'])
def squad_fetch(squad_id):
    myCursor.execute('SELECT * FROM checkins WHERE Squad = {}'.format(squad_id))
    myResults = myCursor.fetchall()
    return jsonify(myResults), 200, {'ContentType': 'application/json'}

@app.route('/api/checkins/user/<int:user_id>', methods=['GET'])
def user_fetch(user_id):
    if 'feeling' in request.args and 'squad' in request.args:
        feeling = request.args['feeling']
        squad = request.args['squad']
        sql = ("SELECT * FROM checkins WHERE User_ID = {}".format(user_id) + " AND Feeling = {}".format(feeling) + " AND Squad = {}".format(squad) + " ORDER BY Date DESC")
        myCursor.execute(sql)
        myResults = myCursor.fetchall()
    elif 'feeling' in request.args:
        feeling = request.args['feeling']
        sql = ("SELECT * FROM checkins WHERE User_ID = {}".format(user_id) + " AND Feeling = {}".format(feeling) + " ORDER BY Date DESC")
        myCursor.execute(sql)
        myResults = myCursor.fetchall()
    elif 'squad' in request.args:
        squad = request.args['squad']
        sql = ("SELECT * FROM checkins WHERE User_ID = {}".format(user_id) + " AND Squad = {}".format(squad) + " ORDER BY Date DESC")
        myCursor.execute(sql)
        myResults = myCursor.fetchall()
    else:
        myCursor.execute("SELECT * FROM checkins WHERE User_ID = {}".format(user_id) + " ORDER BY Date DESC")
        myResults = myCursor.fetchall()
    return jsonify(myResults), 200, {'ContentType': 'application/json'}

@app.route('/api/checkins', methods=['POST'])
def checkins_post():
    data = request.json
    myCursor.execute("INSERT INTO checkins (Start_time, Completion_time, User_ID, Date, Squad, Feeling, Why_feeling, Did, Learned, Todo, Question) VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}', '{}','{}','{}', '{}')".format(data['start_time'], data['getTime'], data['User_ID'], data['date'], data['team'], data['feeling'], data['why_feeling'], data['did'], data['learned'], data['todo'], data['question']))
    connection.commit()
    return jsonify({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/api/checkins/<int:checkin_id>', methods=['PUT'])
def checkins_update(checkin_id):
    data = request.json
    set_values = []
    for k, v in data.items():
        if isinstance(v, str):
            set_values.append('{} = "{}"'.format(k, v))
        else:
            set_values.append('{} = {}'.format(k, v))
    sql = 'UPDATE checkins SET '
    separator = ', '
    sql = sql + separator.join(set_values)
    sql = sql + ' WHERE Checkin_ID = {}'.format(checkin_id)
    myCursor.execute(sql)
    connection.commit()
    return jsonify({'success': True}), 200, {'ContentType': 'application/json'}

app.run()

# http://127.0.0.1:5000/api/checkins
# http://127.0.0.1:5000/api/checkins/user/1?feeling=1&squad=1



