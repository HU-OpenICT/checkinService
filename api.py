import flask
from flask import jsonify

import mysql.connector

from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
#connection local database
connection = mysql.connector.connect(
    host='127.0.0.1', port='3307', database='checkin', user='root', password='****')
myCursor = connection.cursor(dictionary=True)

#get all the checkins
@app.route('/api/checkins', methods=['GET'])
def checkins_fetch():
    myCursor.execute("SELECT * FROM checkins")
    myResults = myCursor.fetchall()
    return jsonify(myResults), 200

#only get the students id, the team he is in and his feeling
@app.route('/api/checkins/gevoel', methods=['GET'])
def gevoel_fetch():
    myCursor.execute("SELECT User_ID, Squad, Gevoel FROM checkins")
    myResults = myCursor.fetchall()
    return jsonify(myResults), 200


app.run()

#http://127.0.0.1:5000/api/checkins
#http://127.0.0.1:5000/api/checkins/gevoel

#Columns titels
#ID, Start_time, Completion_time, User_ID, Datum, Squad, Gevoel, Waarom_gevoel, Gedaan, Geleerd, Vandaag_doen, Vraag
