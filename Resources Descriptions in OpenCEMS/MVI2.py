#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response
from random import randint

from itertools import cycle
import requests

missvalint = Blueprint('missvalint', __name__,)

@missvalint.route('/missvalint.md')
def getDescriptorValInterpolation():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/missvalint.md",
			"entrypoint": "http://51.77.148.187:5001/resource/missvalint",
			"location": "",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "35"}],
			"Operation": [{
				"method": "GET",
				"expects": ["tabValues", "tabTimestamp"],
				"returns": ["tabValues"],
				"functionality": "MVI", 
				"image": "mvi.png",
				"Qf": [{"Cost" : "5"},{"Usage": "14"}]
				}],
			"Link": [{
				"@id": "http://51.77.148.187:5001/resource/predheatengcons",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "EDP"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/predheateng",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "EDP"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/missvalinterpolation",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "MVI"
				}
				]
 		}
 		"""
 	return myjson
	
