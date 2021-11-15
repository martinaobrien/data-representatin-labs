import requests
import json

#html = '<hi>hello world</h1>This is html '

f = open("../Week_02\carviewer02.html", "r")
html = f.read()

apiKey = 'hxBJDP97ooFFAzb8S9Zaq9l7OOj68WCvId7x552umbptbYhir2BApYmKUgPjOINF'
url = 'https://api.html2pdf.app/v1/generate'

#putting the API in as data
data = {'html': html, 'apiKey': apiKey}
response = requests.post(url, json=data)

newFile = open("lab0602.htmlaspdf.pdf", "wb")
newFile.write(response.content)
print(response.status_code)