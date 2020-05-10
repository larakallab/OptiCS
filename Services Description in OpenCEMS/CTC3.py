#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

collclimtemp = Blueprint('collclimtemp', __name__,)

@collclimtemp.route('/collClimTemp.md')
def getDescriptorAirTemperature():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/collClimTemp.md",
			"entrypoint": "http://51.77.148.187:5001/resource/collclimtemp",
			"location": "Zone1",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "90"}],
			"Operation": [{
				"method": "GET",
				"expects": ["h2g:startdate", "h2g:enddate"],
				"returns": ["schema:DateTime", "schema:Float"],
				"functionality": "CTC", 
				"Qf": [{"Cost" : "25"},{"Usage": "20"}]
				}],
			"Link": [{
				"@id": "http://51.77.148.187:5001/resource/outvaldetection",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "OVD"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/missvaldetection",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "MVD"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/outvaldet",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "OVD"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/missvaldet",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "MVD"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/outdet",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "OVD"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/missdet",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "MVD"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/getclimtemperature",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "CTC"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/collectclimtemperature",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "CTC"
				}
				]
 		}
 		"""
 	return myjson
	
