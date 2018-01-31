from src import app
from flask import Flask, request,redirect,send_file
from flask import make_response
from flask import render_template, jsonify
import requests
import json

@app.route('/get_country')
def get_country_try():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d7311342c7ecbfaf056c4965205b134a3a5f59814378fa22"
    }

    query = {
        "type": "run_sql",
        "args": {
            "sql": "CREATE VIEW view_country_count AS SELECT country,COUNT(respondent) AS country_count FROM surveyresults GROUP BY country;"
         }
    }
    dataUrl1= "https://data.course77.hasura-app.io/v1/query"
    print(dataUrl1)
    print(json.dumps(query))
    response = requests.post(
        dataUrl1, data=json.dumps(query), headers=headers
    )
    data1 = response.json()
    print(json.dumps(data1))

    headers2 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d7311342c7ecbfaf056c4965205b134a3a5f59814378fa22"
    }

    query2 = {
        "type": "add_existing_table_or_view",
        "args": {
            "name": "view_country_count"
        }
    }
    dataUrl1= "https://data.course77.hasura-app.io/v1/query"
    print(dataUrl1)
    print(json.dumps(query2))
    response = requests.post(
        dataUrl1, data=json.dumps(query2), headers=headers2
    )
    data2 = response.json()
    print(json.dumps(data2))

    headers3 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d7311342c7ecbfaf056c4965205b134a3a5f59814378fa22"
    }

    query3 = {
        "type": "select",
        "args": {
            "table": "view_country_count",
            "columns":[
               "*"
            ],
            "order_by":"country"
        }
    }
    dataUrl1= "https://data.course77.hasura-app.io/v1/query"
    print(dataUrl1)
    print(json.dumps(query3))
    response = requests.post(
        dataUrl1, data=json.dumps(query3), headers=headers3
    )
    data3 = response.json()
    print(json.dumps(data3))
    return jsonify(data=data3)

@app.route('/get_professional')
def get_professional_try():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d7311342c7ecbfaf056c4965205b134a3a5f59814378fa22"
    }

    query = {
        "type": "run_sql",
        "args": {
            "sql": "CREATE VIEW view_professional_count AS SELECT professional,COUNT(respondent) AS professional_count FROM surveyresults GROUP BY professional;"
         }
    }
    dataUrl1= "https://data.course77.hasura-app.io/v1/query"
    print(dataUrl1)
    print(json.dumps(query))
    response = requests.post(
        dataUrl1, data=json.dumps(query), headers=headers
    )
    data1 = response.json()
    print(json.dumps(data1))

    headers2 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d7311342c7ecbfaf056c4965205b134a3a5f59814378fa22"
    }

    query2 = {
        "type": "add_existing_table_or_view",
        "args": {
            "name": "view_professional_count"
        }
    }
    dataUrl1= "https://data.course77.hasura-app.io/v1/query"
    print(dataUrl1)
    print(json.dumps(query2))
    response = requests.post(
        dataUrl1, data=json.dumps(query2), headers=headers2
    )
    data2 = response.json()
    print(json.dumps(data2))

    headers3 = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d7311342c7ecbfaf056c4965205b134a3a5f59814378fa22"
    }

    query3 = {
        "type": "select",
        "args": {
            "table": "view_professional_count",
            "columns":[
               "*"
            ],
            "order_by":"professional"
        }
    }
    dataUrl1= "https://data.course77.hasura-app.io/v1/query"
    print(dataUrl1)
    print(json.dumps(query3))
    response = requests.post(
        dataUrl1, data=json.dumps(query3), headers=headers3
    )
    data3 = response.json()
    print(json.dumps(data3))
    return jsonify(data=data3)

@app.route("/")
def home():
    return "Hasura Hello World nalini Suresh"

