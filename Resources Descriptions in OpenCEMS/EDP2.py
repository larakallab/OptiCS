#!/usr/bin/env python

from flask import Blueprint
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

predheateng = Blueprint('predheateng', __name__,)

@predheateng.route('/predheateng.md')
def getDescriptorEnergyHeatPrediction():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/predheateng.md",
			"entrypoint": "http://51.77.148.187:5001/resource/predheateng",
			"location": "",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "85"}],
			"Operation": [{
				"method": "GET",
				"expects": ["tabValues", "tabTimestamp"],
				"returns": ["tabValues"],
				"functionality": "EDP",
				"Qf": [{"Cost" : "10"},{"Usage": "15"}]
				}],
			"Link": [{
				"@id": "http://51.77.148.187:5001/resource/predheatengcons",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "EDP"
				}
				]
 		}
 		"""
 	return myjson
