import requests
import pprint

print("Capture User Login Data and Give an output")
sitename = input(r"Enter site (e.g. GitHub): ")

if sitename.lower() == 'github':
    url = "https://api.github.com"

else:
    print("Not supported")
    exit()

username = input(r"Enter username: ")
password = input(r"Enter password: ")

log_url = url+'/users/'+username+'?'
profile = requests.get(log_url, auth=(username, password))

results_dict = profile.json()
for key in results_dict:
    print(key, " : ", results_dict[key])
