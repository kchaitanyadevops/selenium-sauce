#!/bin/python

import sys
import json
import requests


if  len(sys.argv) != 2:
    print "Parse IPADDRESS as Input to script"
    sys.exit(1)
IPADDRESS = sys.argv[1]
LIST_URL="http://"+IPADDRESS+"/student/student/list"
POST_URL="http://"+IPADDRESS+"/student/student"

resp = requests.get(LIST_URL)
data = json.loads(resp.text)
if data['httpStatus'] >= 200 and data['httpStatus'] <= 210:
    print "API LIST TEST - SUCCESS"
else:
    print "API LIST TEST - FAILURE"
    sys.exit(1)

payload = "{\r\n\t  \"studentName\": \"Meghan Mahadev\",\r\n      \"studentAddr\": \"Hyderabad\",\r\n      \"studentAge\": \"2\",\r\n      \"studentQulaification\": \"Nursary\",\r\n      \"studentPercent\": \"99%\",\r\n      \"studentYearPassword\": \"2017\"\r\n    }"
headers = {
    'content-type': "application/json"
}
resp = requests.request("POST", POST_URL, data=payload, headers=headers)
data = json.loads(resp.text)
ID = data['data']['object']['student_id']
if data['httpStatus'] >= 200 and data['httpStatus'] <= 210:
    print "API POST TEST - SUCCESS"
else:
    print "API POST TEST - FAILURE"
    sys.exit(1)

DEL_URL = "http://"+IPADDRESS+"/student/student/"+str(ID)
res = requests.request("DELETE", DEL_URL)
if data['httpStatus'] >= 200 and data['httpStatus'] <= 210:
    print "API DELETE TEST - SUCCESS"
else:
    print "API DELETE TEST - FAILURE"
    sys.exit(1)
