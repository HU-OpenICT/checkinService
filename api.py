import flask
from flask import request, jsonify

import mysql.connector

from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

connection = mysql.connector.connect(
    host='127.0.0.1', port='3307', database='checkin', user='root', password='123flappie')
myCursor = connection.cursor(dictionary=True)


@app.route('/api/checkins', methods=['GET'])
def checkins_fetch():
    myCursor.execute("SELECT * FROM checkins")
    myResults = myCursor.fetchall()
    return jsonify(myResults), 200


@app.route('/api/checkins/gevoel', methods=['GET'])
def gevoel_fetch():
    myCursor.execute("SELECT User_ID, Squad, Gevoel FROM checkins")
    myResults = myCursor.fetchall()
    return jsonify(myResults), 200


@app.route('/api/checkins', methods=['POST'])
def checkins_post():
    data = request.json
    myCursor.execute("INSERT INTO checkins (Datum, Squad, Gevoel, Waarom_gevoel, Gedaan, Geleerd, Vandaag_doen, Vraag) VALUES ('{}','{}','{}', '{}','{}','{}','{}','{}')".format(data['datum'], data['team'], data['gevoel'], data['reden_gevoel'], data['gister_gedaan'], data['gister_geleerd'], data['vandaag_doen'], data['hulpvragen']))
    connection.commit()
    return jsonify({'success': True}), 200, {'ContentType': 'application/json'}


app.run()

# http://127.0.0.1:5000/api/checkins
# http://127.0.0.1:5000/api/checkins/gevoel


# Columns titels
# ID, Start_time, Completion_time, User_ID, Datum, Squad, Gevoel, Waarom_gevoel, Gedaan, Geleerd, Vandaag_doen, Vraag
