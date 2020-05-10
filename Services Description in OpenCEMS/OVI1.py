#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

outvalinterpolation = Blueprint('outvalinterpolation', __name__,)

@outvalinterpolation.route('/outvalinterpolation.md')
def getDescriptorValInterpolation():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/outvalinterpolation.md",
			"entrypoint": "http://51.77.148.187:5001/resource/outvalinterpolation",
			"location": "",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "75"}],
			"Operation": [{
				"method": "GET",
				"expects": ["tabValues", "tabTimestamp"],
				"returns": ["tabValues"],
				"functionality": "OVI", 
				"Qf": [{"Cost" : "15"},{"Usage": "4"}]
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
				"@id": "http://51.77.148.187:5001/resource/outvalint",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "OVI"
				}
				]
 		}
 		"""
 	return myjson
	
