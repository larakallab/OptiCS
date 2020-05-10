#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

outvaldetection = Blueprint('outvaldetection', __name__,)

@outvaldetection.route('/outvaldetection.md')
def getDescriptorValDetection():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/outvaldetection.md",
			"entrypoint": "http://51.77.148.187:5001/resource/outvaldetection",
			"location": "",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "55"}],
			"Operation": [{
				"method": "GET",
				"expects": ["tabValues"],
				"returns": ["tabTimestamp"],
				"functionality": "OVD", 
				"Qf": [{"Cost" : "0"},{"Usage": "24"}]
				}],
			"Link": [{
				"@id": "http://51.77.148.187:5001/resource/outvalinterpolation",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "OVI"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/outvalint",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "OVI"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/outvaldet",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "OVD"
				}
				]
 		}
 		"""
 	return myjson
	
