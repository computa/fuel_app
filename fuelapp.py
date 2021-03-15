
from feedparser import parse
import feedparser
import requests
from pprint import pprint
import ssl
ssl._create_default_https_context=ssl._create_unverified_context


# response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')

# feed1 = feedparser.parse(response.content)
# pprint(feed1)

#feed1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')

#pprint.pprint(feed1)

#feed1 = parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')

#pprint(feed1)

no_number = []
number = ['one','two','three']
number.append('four')
number.append(18)
#print(number[4])

'''
print('There are ', number[4], 'number of things')
print('There are ', len(number), 'number of things')
print('These are inside number', number)
'''

member = {'Name': 'Ambrose', 'Age': 19, 'Address': '14  Road Street, Perth'}

#print('A member lives at:', member['Address'])

member_list = [
    ['Ross', 19, 20023],
    ['Jim', 21, 20021],
]
#print(member_list[1][2])

l = [2,3,4]
l2 = []
for i in l:
    j = i+1
    l2.append(j)
#print(l2)

l = ['first', 'second']
l2 = []
for s in l:
    l2.append(s+'_word')
#print(l2)

l1 = [1, 2, 3]
l2 = [10, 11, 12]
l3 = l1 + l2

#print(l3)

empty_dic = {}

person = {
    'name': 'Robin',
    'age': 44,
}

#print(person['name'])

#person as a list?

plist = ['Robin', 44]

#print(plist[1])

network = {
    'people': [
        {'name': 'Mary', 'age': 54},
        person, 
        {'name': 'James', 'age': 45},
    ],
    'verson': 1
}

people_list = network['people']
third_person = people_list[2]
#print(third_person['age'])

person = {
    'name': 'RObin', 
    'age': 45, 
    'friends': [
        {'name': 'John', 'age': 44}, 
        {'name': 'Mary', 'age': 23}
    ]
}
friends = person['friends']
#print(friends)

#sorting
l1  = [{'name': 'Robin', 'age': 44}, {'name': 'John', 'age': 22}, {'name': 'Mary', 'age': 33}]
def by_age(item):
    return item['age']
sorted_l1 = sorted(l1, key= by_age)
#print(sorted_l1)

#Functions
def get_fuel (product_id):
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb=Cloverdale'
    data = feedparser.parse(url)
    return data['entries']
unleaded = 1
premium_unleaded = 2

u_prices = get_fuel(unleaded)
pu_prices = get_fuel(premium_unleaded)

#print(u_prices)
#print('-----------------')
#print('-----------------')
#print(pu_prices)

people = [{'name': 'Robin', 'age': 99}, {'name': 'Kevin', 'age': 1}, {'name': 'Jane', 'age': 50}]


def get_people(older_than):
    new_people = []
    for person in people:
        if person['age'] > older_than:
            new_people.append(person)
    return new_people
print(get_people(0))
print(get_people(5))
print(get_people(50))