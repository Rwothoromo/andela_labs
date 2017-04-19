import requests
print("Capture User Login Data and Give an output")
sitename = input("Enter username (Facebook): ")
username = input("Enter username: ")
password = input("Enter password: ")

if sitename.lower() == 'facebook':
    url = "https://www.facebook.com/login"

page_get = requests.get(url, auth=(username, password))
page_post = requests.post(url, {"username": username, "password": password})
# print(page_get.text)#, page_post.text)

results_dict = {}
results_dict['Content_type'] = page_get.headers['content-type']
results_dict['Status'] = page_post.status_code
results_dict['Encoding'] = page_get.encoding
# results_dict['Content'] = page_get.text
# results_dict['Json'] = page_post.json()

print("\nConnection details:\n\n")

for item in results_dict:
    print(item, " : ", results_dict[item])
