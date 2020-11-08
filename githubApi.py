import requests

"""fueron eliminadas las credenciales"""

client_id='bcc69c232219a24165db'
client_secret='cf3babfb19141f962117f964cf265f58d3df6c22'
code='d43cd48f8eb717ab4bf8'
access_token='62576340236a5d78e96fcf3ceb423ea3338b4384' #no tiene tiempo limite

def meetOauth():
    url='https://github.com/login/oauth/access_token'
    payload={'client_id':client_id,'client_secret':client_secret,'code':code}
    headers={'Accept':'application/json'}
    response=requests.post(url,json=payload,headers=headers)

    if response.status_code==200:
        print(response.json()['access_token'])

def getRepo():
    url = 'https://api.github.com/user/repos'
    headers={'Authorization': 'token 62576340236a5d78e96fcf3ceb423ea3338b4384'}
    response= requests.get(url,headers=headers)

    if response.status_code==200:
        payload= response.json()

        for projects in payload:
            name = projects['name']
            print (name)
    else:
        print (response.content)
def createRepo():
    url = 'https://api.github.com/user/repos'
    headers={'Accept' : 'application/json','Authorization': 'token' + access_token}
    payload = {'name':'createdFromApi'} 

    response=requests.post(url, json=payload, headers=headers)

    if response.status_code==200:
        print (response.json())

    else:
        print (response.content)
