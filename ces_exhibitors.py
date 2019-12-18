import os
print("Current File Name : ",os.path.realpath(__file__))

import requests

#ces_url = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha&filter=A&pageNo=1&pageSize=15'
ces_base_url = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha'
param1_base = '&filter='
param2_base = '&pageNo=1'
param3_base = '&pageSize=15'

URL_HEADER = {'ctaapi-version': '1.1'}

EXHIBITOR_SEARCH_FILTER = ['#', 'A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
                           'W','X','Y','Z']


for f1 in EXHIBITOR_SEARCH_FILTER:
    param1_full = param1_base + f1
    ces_url_full = ces_base_url+param1_full+param2_base+param3_base
    print(ces_url_full)
    r = requests.get(ces_url_full, headers = URL_HEADER)
    ces_response_json = r.json()

    for p in ces_response_json['exhibitors']:
        print('Company Name:: ', p['companyName'], ' Description:: ', p['description'])

###
#print out the url
# print('URL Request::', r.url)
#
# print('Request Headers')
# print(r.request.headers)
#
# ces_response_json = r.json()
#
# for p in ces_response_json['exhibitors']:
#     print(p['companyName'])
###




