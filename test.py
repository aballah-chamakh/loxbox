import requests ,json 

# AUTHENTICATION 
auth_url = 'http://127.0.0.1:8000/api/token/'
headers = {
'Content-Type': 'application/json'
}
crendentials = {
    'username': 'username',
    'password': 'password'
}
r = requests.post(auth_url,data=json.dumps(crendentials),headers=headers)
token = r.json()['access']
headers['Authorization'] = f"Bearer {token}"

# FOR THE VIEW  : get_transaction_states 

state_url = 'http://127.0.0.1:8000/api/transaction/states'
data = {'transaction_ids':['111111','20100']}
r = requests.get(state_url,data=json.dumps(data),headers=headers)
print(r.json())

#FOR THE VIEW  : cancel_transaction

canceling_url = f'http://127.0.0.1:8000/api/transaction/{20100}/cancel'
r = requests.get(canceling_url,headers=headers)
print(r.json())






