import flask
from flask import request, jsonify
import pyodbc
import json
import pandas as pd
import itertools


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '(LocalDb)\demo'
database = 'TestDB'
username = 'sa'
password = '0147896325'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=' + server + ';'
                      'DATABASE=' + database + ';'
                      'UID=' + username + ';'
                      'PWD=' + password)

cursor = conn.cursor()


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to API Project</h1><p></p>"


@app.route('/api/v1/resources/info/all', methods=['GET'])
def api_all():
    user_info = cursor.execute('Select * from TestDB.dbo.UserInfo')
    # row_headers = [x[0] for x in user_info.description]  # this will extract row headers
    # print(row_headers)
    # rv = user_info.fetchall()
    # json_data = []
    # for result in rv:
    #     x = {
    #         row_headers[0] : result[0],
    #         row_headers[1] : result[1],
    #         row_headers[2]: str(result[2])
    #     }
    #     json_data.append(x)

    # row_headers = [col[0] for col in user_info.description]  # this will extract row headers
    # rv = user_info.fetchall()
    # json_data = []
    # for result in rv:
    #     json_data.append(dict(zip(row_headers, result)))

    row_headers = [col[0] for col in user_info.description]  # this will extract row headers
    rv = user_info.fetchall()
    data = [dict(zip(row_headers, row)) for row in rv]

    # user_info_dict = []
    # for row in user_info:
    #     print(row)
    #     info = {'name': row[0],
    #             'profession': row[1],
    #             'mobile': str(row[2])}
    #     user_info_dict.append(info)

    # print(dict([json_data]))

    # return jsonify(user_info_dict)
    # return json.dumps(json_data)
    # return json.dumps(user_info.fetchall())
    return jsonify(data)


# name = 'Ahmed'
# profession = 'test'
# mobile = '465465'
# cursor.execute('Insert into UserInfo (Name, Profession, Mobile) '
#                'Values (?,?,?)', name, profession, mobile)

# for row in cursor:
#     print(row)

app.run()
