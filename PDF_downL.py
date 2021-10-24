import wget
import requests
url = 'https://stepik.org/certificate/cdb9b191e6ac2fd45966961498a21064070ef4b7.pdf'
resp = requests.get(url, stream=True)

with open('/home/roman/testDir/myfile.pdf', 'wb') as f:
    f.write(resp.content)

# link = 'https://stepik.org/certificate/2b03ea3b8e235d0ad83432f9aceddb45915006da.pdf'
# obj = wget.download(link)
# with open('/home/roman/testDir/myfile1.pdf', 'wb') as f:
#     f.write(obj)

