#!/usr/bin/python
import requests
import json
import os
from time import strftime


def getTrafficData():
	cookie=dict(user_session=YOUR_SESSION)
	header = {'accept': 'application/json'}
	s = requests.Session()
	request = s.get("https://github.com/USERNAME/REPO_NAME/graphs/traffic-data",headers=header,cookies=cookie)
	if request.status_code==200:
		return request.content
def getCloneData():
	cookie=dict(user_session=YOUR_SESSION)
	header = {'accept': 'application/json'}
	s = requests.Session()
	request = s.get("https://github.com/USERNAME/REPO_NAME/graphs/clone-activity-data",headers=header,cookies=cookie)
	if request.status_code==200:
		return request.content
def storeJson(data,dataType):
	jsonData = json.loads(data)
	yesterday = jsonData['counts'][1]
	oldJson = open(dataType+".json")
	jsonOld = json.load(oldJson)
	oldJson.close()
	newJson = open(dataType+".json","w")
	insertData = {
			"bucket":yesterday['bucket'],
			"total":yesterday['total'],
			"unique":yesterday["unique"]}
	jsonOld.append(insertData)
	json.dump(jsonOld,newJson,indent=4)

def pushGithub():
	day	= strftime('%Y-%m-%d')
	os.system("git add .")
	os.system("git commit -m \""+day+"\"")
	os.system("git push")
storeJson(getTrafficData(),"traffic")
storeJson(getCloneData(),"clone")
pushGithub()
