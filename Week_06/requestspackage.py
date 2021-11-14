import requests

#url = 'https://www.gmit.ie' #how to get information back
#response = requests.get(url)
#print(response.status_code)
#print (response.text)
#print (response.headers)

url ='http://127.0.0.1:5000/cars' #how to do a post
data = {'reg': '123','make': 'blah','model': 'blah','price': '1234'}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())