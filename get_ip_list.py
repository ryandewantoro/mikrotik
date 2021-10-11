import routeros_api
#https://github.com/socialwifi/RouterOS-api

import json

host = '192.168.1.1'
username = ''
password = ''

connection = routeros_api.RouterOsApiPool(host, username=username, password=password, plaintext_login=True)

api = connection.get_api()

list_ipadd = api.get_resource('ip/address/').get()

print(json.dumps(show_ipadd, indent=3))

connection.disconnect()
