import os
print("Current File Name : ",os.path.realpath(__file__))


import requests

#ces_url = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha&filter=A&pageNo=1&pageSize=15'
ces_base_url = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha'
param1_base = '&filter=A'
param2_base = '&pageNo=1'
param3_base = '&pageSize=15'



ces_url_full = ces_base_url+param1_base+param2_base+param3_base

ces_url_header = {'ctaapi-version': '1.1'}

r = requests.get(ces_url_full, headers = ces_url_header)
#print out the url
print('URL Request::', r.url)

print('Request Headers')
print(r.request.headers)

ces_response_json = r.json()

for p in ces_response_json['exhibitors']:
    print(p['companyName'])





