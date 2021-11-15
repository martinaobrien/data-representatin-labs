#pip install PyGithub

from github import Github
import requests

#remove the mine sign from the key
g = Github("API Key goes here - cannot be uploaded to Github or else it gets deleted")

#for repo in g.get_user(0.get_repos();
# print(repo.name)
#repo.edit(has_wiki=False)
#to see all the available attributes and methods
#print(dir(repo))

repo = g.get_repo("name of repo is here")
print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)
newContents = contentOfFile + "more stuff \n"

#print (newContents)
gitHubResponse=repo.update_file(fileInfo.path, "updated by prog"), newContents, fileInfo.sha)
print (gitHubResponse)