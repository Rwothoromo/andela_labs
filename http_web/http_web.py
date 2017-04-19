import requests
import pprint

print("Capture User Login Data and Give an output")
sitename = input(r"Enter site (e.g. GitHub): ")

if sitename.lower() == 'github':
    url = "https://api.github.com"

# elif sitename.lower() == 'twitter':
#     url = "https://twitter.com/login"
else:
    print("Not supported")
    exit()

username = input(r"Enter username: ")
password = input(r"Enter password: ")

log_url = url+'/users/'+username+'?'
profile = requests.get(log_url, auth=(username, password))

# print("\nName: ",profile.json()['name'], "\nBio: ", profile.json()['bio'])
results_dict = profile.json()
for key in results_dict:
    print(key, " : ", results_dict[key])

# ba982517f6117112c505c1233781bfc0a2adc6b5

# page_get = requests.get(url, auth=(username, password))
# page_post = requests.post(url, {"username": username, "password": password})
# print(page_get.text)#, page_post.text)

# status = page_post.status_code
# logged_in = "https://api.github.com"
# profile = requests.get(logged_in, auth=(username, password))
# print(profile.json())

# if status != 200:
#     print("Check username and password!")
# else:
#     print(username, page_post.status_code, " logged in successfully")




# results_dict = {}
# results_dict['Content_type'] = page_get.headers['content-type']
# results_dict['Status'] = page_post.status_code
# results_dict['Encoding'] = page_get.encoding
# results_dict['Content'] = page_get.text
# results_dict['Content'] = page_post.json()
# results_dict['Json'] = page_post.json()
# print(page_post.json())
# print("\nConnection details:\n\n")

# for key, value in results_dict:
#     print(key, " : ", value)
