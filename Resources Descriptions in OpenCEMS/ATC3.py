#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

collairtemp = Blueprint('collairtemp', __name__,)

@collairtemp.route('/collAirTemp.md')
def getDescriptorAirTemp():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/collAirTemp.md",
			"entrypoint": "http://51.77.148.187:5001/resource/collairtemp",
			"location": "Zone1",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "80"}],
			"Operation": [{
				"method": "GET",
				"expects": ["h2g:startdate", "h2g:enddate"],
				"returns": ["schema:DateTime", "schema:Float"],
				"functionality": "ATC", 
				"image": "atc.png",
				"Qf": [{"Cost" : "5"},{"Usage": "8"}]
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
				"@id": "http://51.77.148.187:5001/resource/predheat",
				"method": "GET",
				"relationType": "isComplementary",
				"functionality": "EDP"
				},
				{
				"@id": "http://51.77.148.187:5001/resource/getairtemperature",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "ATC"
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
	
