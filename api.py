import flask
from flask import request, jsonify

import mysql.connector

from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

connection = mysql.connector.connect(
    host='127.0.0.1', port='3307', database='checkin', user='root', password='****')
myCursor = connection.cursor(dictionary=True)


@app.route('/api/checkins', methods=['GET'])
def checkins_fetch():
    myCursor.execute("SELECT * FROM checkins")
    myResults = myCursor.fetchall()
    return jsonify(myResults), 200, {'ContentType': 'application/json'}


@app.route('/api/checkins', methods=['POST'])
def checkins_post():
    data = request.json
    myCursor.execute("INSERT INTO checkins (Start_time, Completion_time, Date, Squad, Feeling, Why_feeling, Did, Learned, Todo, Question) VALUES ('{}', '{}', '{}', '{}','{}', '{}','{}','{}','{}','{}')".format(data['start_time'], data['end_time'], data['date'], data['team'], data['feeling'], data['why_feeling'], data['did'], data['learned'], data['todo'], data['question']))
    connection.commit()
    return jsonify({'success': True}), 200, {'ContentType': 'application/json'}


app.run()

# http://127.0.0.1:5000/api/checkins
# http://127.0.0.1:5000/api/checkins/gevoel


