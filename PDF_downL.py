import wget
import requests
url = 'https://stepik.org/certificate/f976f873d5ce3843ec92872700d17d226c0f320d.pdf'
resp = requests.get(url, stream=True)

with open('/home/roman/testDir/Stepik_Inf_sec_Diploma.pdf', 'wb') as f:
    f.write(resp.content)

# link = 'https://stepik.org/certificate/2b03ea3b8e235d0ad83432f9aceddb45915006da.pdf'
# obj = wget.download(link)
# with open('/home/roman/testDir/myfile1.pdf', 'wb') as file:
#    file .write(obj.content)
#