#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify

from random import randint

from itertools import cycle
import requests

getairtemp = Blueprint('getairtemp', __name__,)

@getairtemp.route('/getAirTemperature.md')
def getDescriptorAirTemperature():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/getAirTemperature.md",
			"entrypoint": "http://51.77.148.187:5001/resource/getairtemperature",
			"location": "Zone1",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "70"}],
			"Operation": [{
				"method": "GET",
				"expects": ["h2g:startdate", "h2g:enddate"],
				"returns": ["schema:DateTime", "schema:Float"],
				"functionality": "ATC", 
				"Qf": [{"Cost" : "10"},{"Usage": "15"}]
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
				"@id": "http://51.77.148.187:5001/resource/collectairtemperature",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "ATC"
				}]
 		}
 		"""
 	return myjson
	
