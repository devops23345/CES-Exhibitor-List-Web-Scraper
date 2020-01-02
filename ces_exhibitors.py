import os
import csv
import requests

print(':::-Program Started-:::')
print("Current File Name : ", os.path.realpath(__file__))

CATEGORIES = ['3D Printing,Accessibility', 'Advertising and Marketing', 'Artificial Intelligence',
              'Audio/High-End/High Performance',
              'Cloud Services', 'Computer Hardware', 'Cyber Security and Privacy', 'Digital Health',
              'Digital Imaging/Photography',
              'Drones', 'Education', 'Entertainment and Content', 'Fitness', 'Gaming',
              'Lifestyle (Family, Beauty, Pet)',
              'Mobile Payments/Digital Finance/E-Commerce/Digital Currency', 'Other Consumer Technology',
              'Public Policy/Government', 'Resilience', 'Robotics', 'Self-driving Vehicles', 'Sensors and Biometrics',
              'Smart Cities', 'Smart Home', 'Software and Apps', 'Sports Technology and Esports', 'Sustainability',
              'Telecommunications', 'Travel and Tourism', 'Vehicle Technology', 'Video',
              'Virtual and Augmented Reality', 'Wearables', 'Wireless Devices', 'Wireless Services']

# EXHIBITOR_SEARCH_FILTER = ['#', 'A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
#                           'W','X','Y','Z']
EXHIBITOR_SEARCH_FILTER = ['A']
HallDecoder = {'U': 'Venetian Palazzo Suite', 'I': 'Renaissance', 'N': 'Westgate Suite', 'AA': 'Aria', 'P': 'Wynn',
               'B': 'Central Hall', 'D': 'South Hall 1/2', 'A': 'North Hall', 'M': 'Sands G', 'C': 'South Hall 3',
               'X': 'Sands A-D', 'F': 'Westgate', 'T': 'Venetian Tower', 'EE': 'South Plaza', 'S': 'Venetian Tower',
               'J': 'Venetian Tower', 'Y': 'Venetian', 'L': 'Central Plaza', 'CC': 'Aria',
               'HH': 'Beach Lot', 'II': 'Aria'}


def get_exhibitor_list(letter, page_num):
    # ces_url_full = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha&filter=A&pageNo=1&pageSize=15'

    ces_base_url = 'https://www.ces.tech/api/Exhibitors?searchTerm=&sortBy=alpha&filter='
    page_num_req = '&pageNo='
    page_size_req = '&pageSize=15'

    URL_HEADER = {'ctaapi-version': '1.1'}

    ces_url_full = ces_base_url + letter + page_num_req + str(page_num) + page_size_req
    print(ces_url_full)
    r = requests.get(ces_url_full, headers=URL_HEADER)

    return r


def parse_exhibitor_data():
    for p in ces_response_json['exhibitors']:
        cat_list = []
        cat_dict = {'categories': ''}

        # print to terminal
        print('Company Name:: ', p['companyName'])
        print('Description:: ', p['description'])
        print('Company Link:: ', p['companyLink'])
        print('Hall::', HallDecoder.get(p['booths'][0]['hall'], 'None'), 'Booth Number:: ',
              p['booths'][0]['boothNumber'])

        for c in p['categories']:
            print('Categories::', c['categoryName'])
            cat_list.append(c['categoryName'])
            cat_dict['categories'] = cat_dict['categories'] + c['categoryName'] + ','
        print('DEBUG:: cat_list::', cat_list)
        print('DEBUG:: cat_dict::', cat_dict)

        # write to file in CSV format
        csvwriter.writerow([p['companyName'], p['description'], HallDecoder.get(p['booths'][0]['hall'], 'None'),
                            p['booths'][0]['boothNumber'], '=HYPERLINK(\"' + p['companyLink'] + '\")',
                            cat_dict['categories']])
        # write to file in CSV format
        # file_object.write(p['companyName'] + ',')
        # file_object.write(p['description'] + ',')
        # file_object.write(HallDecoder.get(p['booths'][0]['hall'], 'None') + ',')
        # file_object.write(p['booths'][0]['boothNumber'] + ',')
        # file_object.write('=HYPERLINK(\"'+p['companyLink']+'\")' + ',')
        # for c in p['categories']:
        #     file_object.write(c['categoryName'] + ',')
        # file_object.write('\n')

    return


with open('ces_exhibitor.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    # write the header row
    csvwriter.writerow(['Company Name', 'Description', 'Hall', 'Booth Number', 'Company Link', 'Categories'])
# with open('ces_exhibitor2.csv', 'w') as file_object:
#     #write the header row
#     file_object.write('Company Name,Description,Hall,Booth Number,Company Link,Categories\n')

    for f1 in EXHIBITOR_SEARCH_FILTER:  # increment through alphabet
        page_req = 1  # for each new letter, start at page 1

        # get first page
        ces_response = get_exhibitor_list(f1, page_req)

        if (ces_response.status_code == 200):  # positive response
            print('Request Response::SUCCESS::', ces_response.status_code)
            info_available = True

        else:  # error response
            info_available = False
            print('Request Response:: ERROR::', ces_response.status_code)
            break

        while info_available:
            # get json format of data
            ces_response_json = ces_response.json()
            # parse and output data
            parse_exhibitor_data()

            if (len(ces_response_json['exhibitors']) == 15):  # go to next page of current letter
                page_req += 1
                ces_response = get_exhibitor_list(f1, page_req)
                info_available = False  ##for debug only


            elif (len(ces_response_json['exhibitors']) < 15):  # no more data is available, goto next letter
                info_available = False

    print(':::-PROGRAM FINISHED-:::')
