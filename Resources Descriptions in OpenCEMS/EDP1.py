#!/usr/bin/env python

from flask import Blueprint
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

predheatengcons = Blueprint('predheatengcons', __name__,)

@predheatengcons.route('/predheatengcons.md')
def getDescriptorEnergyHeatPrediction():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/predheatengcons.md",
			"entrypoint": "http://51.77.148.187:5001/resource/predheatengcons",
			"location": "",
			"image": "edp.png",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "60"}],
			"Operation": [{
				"method": "GET",
				"expects": ["tabValues", "tabTimestamp"],
				"returns": ["tabValues"],
				"functionality": "EDP",
				"Qf": [{"Cost" : "0"},{"Usage": "14"}]
				}],
			"Link": [{
				"@id": "http://51.77.148.187:5001/resource/predheateng",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "EDP"
				}
				]
 		}
 		"""
 	return myjson
