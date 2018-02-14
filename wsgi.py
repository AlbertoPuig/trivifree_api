from flask import Flask, request, make_response, abort
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
import json

application = Flask(__name__)

@application.route("/<param>")
def hello(param):
    return "Hello Friend!...." + param

@application.route("/edit/<param3>")
def edit(param3):
	result = ''
	data_string = json.dumps(result)
	#Decoded
	decoded = json.loads(data_string)
	question = 'Q'
	question += param3
	print ("--------------------------------------------")
	print ("question " + question)
	print ("--------------------------------------------")
	try:
		with open('data/data.json', 'r') as f:
			data = json.load(f)
			try:
				question_data = data[question]
				#logging.debug('Response for params: ' + question_id)
				return make_response(jsonify(question_data),200)       
			except Exception as ex:
				print ("Not found. Param error")
				return make_response(jsonify(),500)
	except Exception as e:
		#message to log
		#logging.debug(str(e) + question_id)
		#return error
		return make_response(jsonify(e),500) 


if __name__ == "__main__":
	application.run()