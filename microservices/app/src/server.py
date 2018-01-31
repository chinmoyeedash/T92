from src import app
from flask import Flask, request,redirect,send_file
from flask import make_response
from flask import render_template, jsonify
import requests
import json

@app.route('/signup')
def signup_try():
 
# This is the url to which the query is made
    url1 = "https://auth.course77.hasura-app.io/v1/signup"

# This is the json payload for the query
    requestPayload1 = {
        "provider": "username",
        "data": {
            "username": "nalini",
            "password": "na@Suresh"
        }   
    }

# Setting headers
    headers1 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 9b216217fd5be3310585e364902f7ad120f5ad7b0137c825"
    }

# Make the query and store response in resp
    resp = requests.request("POST", url1, data=json.dumps(requestPayload1), headers=headers1)
    data1 = resp.json()
# resp.content contains the json response.
    print(json.dumps(data1))
    return jsonify(data=data1)

@app.route("/")
def home():
    return "Hasura Hello World nalini Suresh T92"

