import os
from dotenv import load_dotenv
import requests

#loads varialbes that were defined in the .env environment
load_dotenv()

client_id = os.getenv("CLIENT_ID")
tenant_id = os.getenv("TENANT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#Check if we are getting the correct credentials
# print(f"Clinet ID : {client_id}\nTenant ID : {tenant_id}\nClient Secret : {client_secret}")

# Now we will ahve to generate an access token 

def generate_access_token():
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    data = {
        "grant_type" : "client_credentials",
        "client_id" : client_id,
        "client_secret" : client_secret,
        "scope" : "https://analysis.windows.net/powerbi/api/.default"
    }
    resp = requests.post(url, data = data)
    # resp.raise_for_status()
    return resp.json()["access_token"]

# Once token is generated, we will need to get all the workspace

def get_workspace(access_token):
    # workspace_id = 'c2303663-f7bc-485c-a6e2-0483ccd04048'
    url =  f"https://api.powerbi.com/v1.0/myorg/groups" #/{workspace_id}/reports"
    headers = {
        "Authorization" : f"Bearer {access_token}"
    }
    resp = requests.get(url,headers=headers)
    # resp.raise_for_status()
    # return resp.json()
    # print(resp)
    return resp.json()["value"][0]


token = generate_access_token()
details = get_workspace(token)

# print(type(details))

print(f"Workspce_Id : {details["id"]}\nWorkspace Name : {details["name"]}")