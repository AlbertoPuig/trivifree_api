from flask import Flask, request, make_response, abort
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
import json

application = Flask(__name__)

#to check status of service
@application.route("/<param>")
def hello(param):
	print ("Request to / with param: " + param)
	return "Service Enabled!...."
    
#api entry
@application.route("/api/v1/quest/<qnumber>")
def edit(qnumber):
	result = ''
	if qnumber.isdigit():
		data_string = json.dumps(result)
		#Decoded
		decoded = json.loads(data_string)
		question = 'Q'
		question += qnumber
		print ("--------------------------------------------")
		print ("question " + question)
		print ("--------------------------------------------")
		try:
			with open('data/data.json', 'r') as f:
				data = json.load(f)
				try:
					question_data = data[question]
					print ("Responding json")
					return make_response(jsonify(question_data),200)       
				except Exception as ex:
					print ("Not found. Param error")
					return make_response(jsonify(),500)
		except Exception as e:
			return make_response(jsonify(e),500) 
	else:
		return abort(400)


if __name__ == "__main__":
	application.run()