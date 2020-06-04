#!/usr/bin/env python

from flask import Blueprint
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

predheat = Blueprint('predheat', __name__,)

@predheat.route('/predheat.md')
def getDescriptorHeatPrediction():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/predheat.md",
			"entrypoint": "http://51.77.148.187:5001/resource/predheat",
			"location": "",
			"image": "edp.png",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "55"}],
			"Operation": [{
				"method": "GET",
				"expects": ["tabValues", "tabTimestamp"],
				"returns": ["tabValues"],
				"functionality": "EDP",
				"Qf": [{"Cost" : "0"},{"Usage": "19"}]
				}],
			"Link": [{
				"@id": "http://51.77.148.187:5001/resource/predheatengcons",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "EDP"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/predheateng",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "EDP"
				}
				]
 		}
 		"""
 	return myjson
