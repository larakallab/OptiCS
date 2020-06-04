#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

outdet = Blueprint('outdet', __name__,)

@outdet.route('/outdet.md')
def getDescriptorDetection():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/outdet.md",
			"entrypoint": "http://51.77.148.187:5001/resource/outdet",
			"location": "",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "65"}],
			"Operation": [{
				"method": "GET",
				"expects": ["tabValues"],
				"returns": ["tabTimestamp"],
				"functionality": "OVD", 
				"image": "ovd.png",
				"Qf": [{"Cost" : "10"},{"Usage": "24"}]
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
				"@id": "http://51.77.148.187:5001/resource/outint",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "OVI"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/outvaldetection",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "OVD"
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
	
