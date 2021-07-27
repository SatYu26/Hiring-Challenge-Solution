import requests
import base64

file = open('code.py', 'rb')
data = file.read()

URL = "https://prod-24.centralindia.logic.azure.com/workflows/78d6df0ed1384ee0b7d04918f1a32b85/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=i6gXuS7-5_fFVf-0u8M4UfymINDULCMifsscfN5cPKM"


data = {
    "Name": "Ashay Kumar Thakur",
    "Email": "at4206@srmist.edu.in",
    "College": "SRMIST KTR",
    "StudentId": "RA1811005010014",
    "FileName": "code.py",
    "Password": "c3A0OTYxQHNybWlzdC5lZHUuaW4"
}


req = requests.put(url=URL, headers=data, files=file)


print(req.text)
