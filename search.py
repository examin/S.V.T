import pymongo
import sys
import re
import argparse

vSearch = ""
vOutput = ""
vFreeSearch = ""

argParser = argparse.ArgumentParser(description='Search for vulnerabilities in the National Vulnerability DB. Data from http://nvd.nist.org.')
argParser.add_argument('-p', type=str, help='S = search product, e.g. o:microsoft:windows_7 or o:cisco:ios:12.1')
argParser.add_argument('-f', type=str, help='F = free text search in vulnerability summary')
argParser.add_argument('-o', type=str, help='O = output format [csv|html|json|xml]')
args = argParser.parse_args()

vSearch = args.p
vOutput = args.o
vFreeSearch = args.f

if vSearch:
	vSearch = re.sub(r'\(','%28', vSearch)
	vSearch = re.sub(r'\)','%29', vSearch) 

connect = pymongo.Connection()
db = connect.cvedb
collection = db.cves
csvOutput = 0
htmlOutput = 0
xmlOutput = 0
jsonOutput = 0
	
if vOutput == "csv":
	csvOutput = 1
elif vOutput == "html":
	htmlOutput = 1
elif vOutput == "xml":
	xmlOutput = 1
elif vOutput == "json":
	jsonOutput = 1

if htmlOutput:
	print("<html><body><h1>"+sys.argv[1]+"</h1>")

if vFreeSearch:
	for item in collection.find({'summary': {'$regex' : vFreeSearch}}):
		print(item)

if vSearch:
	for item in collection.find({"vulnerable_configuration": {'$regex' : vSearch}}):
		if csvOutput:
			for entry in item['references']:
				if re.search("http://www.cisco.com",entry):
					link = entry
				print(item['id']+"|"+item['Published']+"|"+item['cvss']+"|"+item['summary']+"|"+link)
		elif htmlOutput:
			print("<h2>"+item['id']+"<br></h2>CVSS score: "+item['cvss']+"<br>"+"<b>"+item['Published']+"<b><br>"+item['summary']+"<br>")
			print("References:<br>")
			for entry in item['references']:
				print(entry+"<br>")
			print("<hr><hr>") 		
		elif jsonOutput:
			print(item)
		else:
			print("CVE\t: " + item['id'])
			print("DATE\t: " + item['Published'])
			print("CVSS\t: " + item['cvss'])
			print(item['summary'])
			print("\nReferences:")
			print("-----------")
			for entry in item['references']:
				print(entry)
			print("\nVulnerable Configs:")
			print("-------------------")
			for entry in item['vulnerable_configuration']:
				print(entry)
			print("\n\n")
#print(Moutput)
if htmlOutput:
	print("</body></html>")