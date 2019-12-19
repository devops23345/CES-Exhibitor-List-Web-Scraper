import os
import csv
import requests
print("Current File Name : ", os.path.realpath(__file__))

#ces_url = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha&filter=A&pageNo=1&pageSize=15'
ces_base_url = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha'
param1_base = '&filter='
param2_base = '&pageNo=1'
param3_base = '&pageSize=15'

URL_HEADER = {'ctaapi-version': '1.1'}
CATEGORIES = ['3D Printing,Accessibility', 'Advertising and Marketing','Artificial Intelligence',
              'Audio/High-End/High Performance',
              'Cloud Services','Computer Hardware','Cyber Security and Privacy','Digital Health',
              'Digital Imaging/Photography',
              'Drones','Education','Entertainment and Content','Fitness','Gaming','Lifestyle (Family, Beauty, Pet)',
              'Mobile Payments/Digital Finance/E-Commerce/Digital Currency','Other Consumer Technology',
              'Public Policy/Government','Resilience','Robotics','Self-driving Vehicles','Sensors and Biometrics',
              'Smart Cities','Smart Home','Software and Apps','Sports Technology and Esports','Sustainability',
              'Telecommunications','Travel and Tourism','Vehicle Technology','Video',
              'Virtual and Augmented Reality','Wearables','Wireless Devices','Wireless Services']

#EXHIBITOR_SEARCH_FILTER = ['#', 'A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
#                           'W','X','Y','Z']
EXHIBITOR_SEARCH_FILTER = ['A']

with open('ces_exhibitor.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    #write the header row
    csvwriter.writerow(['Company Name', 'Description', 'Booth Number', 'Company Link', 'Categories'])

    for f1 in EXHIBITOR_SEARCH_FILTER:
        param1_full = param1_base + f1
        ces_url_full = ces_base_url+param1_full+param2_base+param3_base
        print(ces_url_full)
        r = requests.get(ces_url_full, headers = URL_HEADER)
        ces_response_json = r.json()

        for p in ces_response_json['exhibitors']:
            print('Company Name:: ', p['companyName'])
            print('Description:: ', p['description'])
            print('Company Link:: ', p['companyLink'])
            print('Hall::', p['booths'][0]['hall'], 'Booth Number:: ', p['booths'][0]['boothNumber'])
            for c in p['categories']:
                print('Categories::', c['categoryName'])

            csvwriter.writerow([p['companyName'], p['description'], p['booths'][0]['boothNumber'], p['companyLink']])


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




