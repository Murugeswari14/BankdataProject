from flask import Flask, json
#from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os
import urllib.request
#from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import csv
from flask_cors import cross_origin,CORS

app = Flask(__name__)
CORS(app)
#api = Api(app)


ALLOWED_EXTENSIONS = set(['csv', 'pdf', ])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)

		res=extract(filename)

		# resp = jsonify(res)
		# res.status_code = 201
		return res
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp


def extract(filename):
   
    df = pd.read_csv(filename)

    dfnew = df.dropna(axis=0, how="all", thresh=None, subset=None, inplace=False)
    dfnew = dfnew.fillna(0)

    dfnew.rename(columns = {'Closing Balance':'ClosingBalance'}, inplace = True)
    dfnew.rename(columns = {'Withdrawal Amt.':'Withdrawal'}, inplace = True)
    dfnew.rename(columns = {'Deposit Amt.':'Deposit'}, inplace = True)
    
    res = dfnew.to_json(orient='records')

    return res

if __name__ == "__main__":
    app.run()