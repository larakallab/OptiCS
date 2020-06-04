#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

missvaldetection = Blueprint('missvaldetection', __name__,)

@missvaldetection.route('/missvaldetection.md')
def getDescriptorValDetection():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/missvaldetection.md",
			"entrypoint": "http://51.77.148.187:5001/resource/missvaldetection",
			"location": "",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "50"}],
			"Operation": [{
				"method": "GET",
				"expects": ["tabValues"],
				"returns": ["tabTimestamp"],
				"functionality": "MVD", 
				"image": "mvd.png",
				"Qf": [{"Cost" : "20"},{"Usage": "25"}]
				}],
			"Link": [{
				"@id": "http://51.77.148.187:5001/resource/missvalinterpolation",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "MVI"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/missvalint",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "MVI"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/missvaldet",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "MVD"
				}
				]
 		}
 		"""
 	return myjson
	
