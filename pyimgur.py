#!/usr/bin/env python3

import urllib.request
import urllib.parse
import base64
import json

class pyImgurError(Exception):
	pass

def doB64Conv(openedFile):
	try:	
		if openedFile.mode == "rb":
			pass
		else:
			raise pyImgurError("argument was not opened with 'rb' mode")
	except AttributeError:
		raise pyImgurError("argument is not a file object")
		return

	b64img = base64.b64encode(openedFile.read())
	return b64img.decode('utf-8')

def craftAuthURL(clientID):
	authURL = "https://api.imgur.com/oauth2/authorize?"
	values = { "client_id": clientID, "response_type": "pin", "state": "imgurAuth" }
	data = urllib.parse.urlencode(values)
	return authURL+data


def imgurAuth(clientID, clientSecret, PIN):
	pinURL = "https://api.imgur.com/oauth2/token"
	pinValues = { "client_id": clientID, "client_secret": clientSecret, "grant_type": "pin", "pin": PIN }
	dataPIN  = urllib.parse.urlencode(pinValues)
	dataPIN = dataPIN.encode('utf-8')
	reqPIN = urllib.request.Request(pinURL, dataPIN)
	responsePIN = urllib.request.urlopen(reqPIN)
	the_pagePIN = responsePIN.read()
	realData = json.loads(the_pagePIN.decode('utf-8'))

	accessToken = realData["access_token"]
	refreshToken = realData["refresh_token"]

	return (accessToken, refreshToken)
