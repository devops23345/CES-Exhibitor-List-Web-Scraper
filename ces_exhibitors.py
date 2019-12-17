import os
print("Current File Name : ",os.path.realpath(__file__))


import requests

#ces_url = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha&filter=A&pageNo=1&pageSize=15'
ces_base_url = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha'
param1_base = 'filter='
param2_base = 'pageNo='
param3_base = 'pageSize=15'



ces_full_url = ces_base_url+param1+param2+param3

ces_url_header = {'ctaapi-version': '1.1'}

r = requests.get(ces_url, headers = ces_url_header)

print('Request Headers')
print(r.request.headers)

ces_response_json = r.json()

for p in ces_response_json['exhibitors']:
    print(p['companyName'])





