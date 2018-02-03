from src import app
from flask import Flask, request,redirect,send_file
from flask import make_response
from flask import render_template, jsonify
import requests
import json

@app.route('/sendotp')
def sendotp_try():

# This is the url to which the query is made
    url = "https://auth.course77.hasura-app.io/v1/providers/mobile/send-otp"

# This is the json payload for the query
    requestPayload = {
        "mobile": "8095610638",
        "country_code": "91"
    }

# Setting headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 9b216217fd5be3310585e364902f7ad120f5ad7b0137c825"
    }


# Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
    data1=resp.json()
# resp.content contains the json response.
    print(json.dumps(data1))
    return jsonify(data=data1)

@app.route('/signupotp')
def signupotp_try():

# This is the url to which the query is made
    url = "https://auth.course77.hasura-app.io/v1/signup"

# This is the json payload for the query
    requestPayload3 = {
        "provider": "mobile",
        "data": {
            "mobile": "8095610688",
            "country_code": "91",
            "otp": "948589"
        }
    }

# Setting headers
    headers3 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 9b216217fd5be3310585e364902f7ad120f5ad7b0137c825"
    }

# Make the query and store response in resp
    print("request payload")
    print(json.dumps(requestPayload3))
    resp3 = requests.request("POST", url, data=json.dumps(requestPayload3), headers=headers3)
    print("STATUS CODE")
    print(resp3.status_code)
    print(resp3.reason)
    data3=resp3.json()
# resp.content contains the json response.
    print(json.dumps(data3))
    return jsonify(data=data3)

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


@app.route('/login')
def login_try():
 

# This is the url to which the query is made
    url2 = "https://auth.course77.hasura-app.io/v1/login"

# This is the json payload for the query
    requestPayload2 = {
        "provider": "username",
        "data": {
            "username": "Suresh",
            "password": "na@Suresh"
        }
    }

# Setting headers
    headers2 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 9b216217fd5be3310585e364902f7ad120f5ad7b0137c825"
    }

# Make the query and store response in resp
    resp2 = requests.request("POST", url2, data=json.dumps(requestPayload2), headers=headers2)
    data2 = resp2.json()
# resp.content contains the json response.
    
    return jsonify(data=data2)
    
@app.route("/")
def home():
    return "Hasura Hello World nalini Suresh T92"

