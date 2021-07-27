import requests
import base64

file = open('code1.py', 'rb')
data = file.read()

name = "SATYAM GOYAL"
email = "sg9528@srmist.edu.in"
college = "SRM Institute of Science and Technology, Kattakulanthur"
student_id = "RA1811005010009"
file_name = "code1.py"

email_byt = email.encode("ascii")
email_base64_byt = base64.b64encode(email_byt)
password = email_base64_byt.decode("ascii")

URL = "https://prod-24.centralindia.logic.azure.com/workflows/78d6df0ed1384ee0b7d04918f1a32b85/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=i6gXuS7-5_fFVf-0u8M4UfymINDULCMifsscfN5cPKM"

headers = {
    "Name": name,
    "Email": email,
    "College": college,
    "StudentId": student_id,
    "FileName": file_name,
    "Password": password,
}


response = requests.put(url=URL, headers=headers, files=file)
print(response.text)
