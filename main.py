import secrets,requests,random,json,string
def main_sourse():
    response=requests.get('https://api.mail.tm/domains?page=1')
    id_domain=json.loads(response.text)['hydra:member'][0]['id']
    response=requests.get('https://api.mail.tm/domains/'+str(id_domain))
    domain=str(json.loads(response.text)['domain'])
    mail=str(''.join(secrets.choice(string.ascii_lowercase + string.ascii_lowercase) for i in range(15)))+str(random.randint(100,10000))

    headers = {
        'accept': 'application/ld+json',
        'Content-Type': 'application/ld+json',
    }

    data = '{\n  "address": "'+mail+'@'+domain+'",\n  "password": "lasldjlaskdjkjk"\n}'

    response = requests.post('https://api.mail.tm/accounts', headers=headers, data=data).text
    print (mail+'@'+domain)
    try:
        json_data = {
            'address': str(mail)+'@'+domain+'',
            'password': 'linkmilo',
        }

        response = requests.post('https://api.mail.tm/token', headers=headers, json=json_data).text
        token=json.loads(response)['token']
        headers = {
            'accept': 'application/ld+json',
            'Content-Type': 'application/ld+json',
            'authorization': 'Bearer '+str(token),
        }
        response = requests.get('https://api.mail.tm/messages', headers=headers,json=json_data)
        text=response.text        
    except:
        None
