#!/usr/bin/env python

from flask import Blueprint 
from flask import Flask, json
from flask import Response
from flask import request
from flask import jsonify, make_response

from random import randint

from itertools import cycle
import requests

collectairtemp = Blueprint('collectairtemp', __name__,)

@collectairtemp.route('/collectAirTemperature.md')
def getDescriptorAirTemperature():
	myjson = """
 		{
 			"@context": "http://51.77.148.187:5001/resourceDescription/context.jsonld",
			"@id": "http://51.77.148.187:5001/resourceDescription/collectAirTemperature.md",
			"entrypoint": "http://51.77.148.187:5001/resource/collectairtemperature",
			"location": "Zone1",
			"Qres": [{"Dynamicity" : "0"},{"Availability" : "50"}],
			"Operation": [{
				"method": "GET",
				"expects": ["h2g:startdate", "h2g:enddate"],
				"returns": ["schema:DateTime", "schema:Float"],
				"functionality": "ATC",
				"image": "atc.png",
				"Qf": [{"Cost" : "0"},{"Usage": "12"}]
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
				"@id": "http://51.77.148.187:5001/resource/getairtemperature",
				"method": "GET",
				"relationType": "isSimilar",
				"functionality": "ATC"
				}]
 		}
 		"""
 	return myjson
	
