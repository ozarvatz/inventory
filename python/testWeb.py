import requests 
from flask import json

print('-----------------------')
URL = 'http://localhost:8888/ping'
r = requests.get(URL)

assert r.status_code != '200', 'url suffix /ping return status_code != 200'
assert r.text == 'pong', 'url suffix /ping didn\'t return \'pong\''	

print('-----------------------')
URL = 'http://localhost:8888/item/bisli'
r = requests.get(URL)
print(r.status_code)
print('response : ' + r.text)
response = json.loads(r.text)
assert r.status_code != '200', 'url suffix /item/bisli return status_code != 200'
assert response['response'] == '35', 'url suffix /item/bisli didn\'t return \'35\''	

print('-----------------------')
URL = 'http://localhost:8888/item/bmv'
r = requests.get(URL)
response = json.loads(r.text)
assert r.status_code != '200', 'url suffix /item/bisli return status_code != 200'
assert response['response'] == '0', 'url suffix /item/bmv didn\'t return \'0\''	

print('-----------------------')
URL = 'http://localhost:8888/category/store/1'
r = requests.get(URL)
print('response : ' + r.text)
response = json.loads(r.text)
assert r.status_code != '200', 'url suffix /category/store/1 return status_code != 200'
assert response['response'] == '[10, 1, 2]', 'url suffix /category/store/1 didn\'t return \'[10, 1, 2]\''	

print('-----------------------')
URL = 'http://localhost:8888/category/store/32'
r = requests.get(URL)
print('response : ' + r.text)
response = json.loads(r.text)
assert r.status_code != '200', 'url suffix /category/store/32 return status_code != 200'
assert response['response'] == '[]', 'url suffix /category/store/32 didn\'t return \'[]\''	

print('-----------------------')
URL = 'http://localhost:8888/category/median/1'
r = requests.get(URL)
print('response : ' + r.text)
response = json.loads(r.text)
assert r.status_code != '200', 'url suffix /category/median/1 return status_code != 200'
assert response['response'] == '3', 'url suffix /category/median/1 didn\'t return \'3\''	

print('-----------------------')
URL = 'http://localhost:8888/category/median/10'
r = requests.get(URL)
print('response : ' + r.text)
response = json.loads(r.text)
assert r.status_code != '200', 'url suffix /category/median/10 return status_code != 200'
assert response['response'] == '50', 'url suffix /category/median/10 didn\'t return \'50\''	


print('-----------------------')
URL = 'http://localhost:8888/category/median/1001'
r = requests.get(URL)
print('response : ' + r.text)
response = json.loads(r.text)
assert r.status_code != '200', 'url suffix /category/median/1001 return status_code != 200'
assert response['response'] == '\"no median, empty prices list cos category 1001 not exists!!!\"', 'url suffix /category/median/10 didn\'t return \"no median, empty prices list cos category 1001 not exists!!!\"'	
	
pass