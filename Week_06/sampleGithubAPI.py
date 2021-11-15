import requests
import json

# not working need API and github account with private repository '

#f = open("../Week_02\carviewer02.html", "r")
#html = f.read()

apiKey = 'sampleAPIkey'
url = 'https://api.github.com/'#sample github repository that is private
filename ="repo.json"

response = requests.get(url,auth=('token', apiKey))

repoJSON = response.json()
#print (response.json())

file = open (filename, 'w')
json.dump(repoJSON, file, indent=4)
