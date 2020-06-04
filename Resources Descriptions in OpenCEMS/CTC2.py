#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

collectclimtemp = Blueprint('collectclimtemp', __name__,)

@collectclimtemp.route('/collectClimTemperature.md')
def getDescriptorAirTemperature():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/collectClimTemperature.md",
			"entrypoint": "http://51.77.148.187:5001/resource/collectclimtemperature",
			"location": "Zone1",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "40"}],
			"Operation": [{
				"method": "GET",
				"expects": ["h2g:startdate", "h2g:enddate"],
				"returns": ["schema:DateTime", "schema:Float"],
				"functionality": "CTC", 
				"image": "ctc.png",
				"Qf": [{"Cost" : "8"},{"Usage": "6"}]
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
				"@id": "http://51.77.148.187:5001/resource/getclimtemperature",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "CTC"
				}
				]
 		}
 		"""
 	return myjson
	
