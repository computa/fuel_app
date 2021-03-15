from feedparser import parse
import  feedparser
import requests
from pprint import pprint
import ssl 
ssl._create_default_https_context=ssl._create_unverified_context

def get_fuel (product_id, region, day):
    #url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb=Cloverdale'
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Region='+str(region)+'&Day='+day
    fuel_data = feedparser.parse(url)

    return fuel_data['entries']
unleaded = 1
premium_unleaded = 2

northRegion = 25
sourthRegion = 26

today = 'Today'
tomorrow = 'Tomorrow'

u_prices = get_fuel(unleaded, northRegion, today)
u_prices_tomorrow = get_fuel(unleaded, northRegion, tomorrow)



fuel_data_main = []
fuel_data_main_tomorrow = []

for fuel_data in u_prices:
    fuel_data_main.append(
        {
            'location': fuel_data['location'],
            'brand': fuel_data['brand'],
            'price': fuel_data['price'],
            'address': fuel_data['address'],
            'day': 'Today'
        }
    )

for fuel_data_tomorrow in u_prices_tomorrow:
    fuel_data_main_tomorrow.append(
        {
            'location': fuel_data_tomorrow['location'],
            'brand': fuel_data_tomorrow['brand'],
            'price': fuel_data_tomorrow['price'],
            'address': fuel_data_tomorrow['address'],
            'day': 'Tomorrow'
        }
    )

fuel_data_combined = fuel_data_main +fuel_data_main_tomorrow

def by_price(item):
    return item['price']
fuel_data_sorted = sorted(fuel_data_combined, key=by_price)



fuel_price_min = float(fuel_data_sorted[0]['price'])

print(fuel_price_min)

fuel_data_used =[]

for fuel_data in fuel_data_sorted:
    #fuel_data_used.append(fuel_price_min + 3)
    if float(fuel_data['price']) <= float(fuel_price_min + 3):
        fuel_data_used.append(fuel_data)
           
     

fuel_watch = ''
for fuel_data in fuel_data_sorted:
    fuel_watch += f'<tr><td> {fuel_data["location"]}</td> <td> {fuel_data["brand"]}</td> <td> {fuel_data["price"]}</td> <td> {fuel_data["address"]}</td> <td> {fuel_data["day"]}</td></tr>'

css_used = '''
        table{
            font-family: arial, sans-serif;
            border: 1px solid #333;
            width: 100%;
        }

        td, th{
            border: 1px solid Tomato;
            text-align: left;
            padding: 8px;
        }
         tr: nth-child(even){
            background-color: #877070;
          
        }
'''

fuel_watch_site = f'''
<!DOCTYPE html>
<html>
    <head>
        <style>{css_used}</style>
    </head>
    <body>
        <h1>Fuel Price Watch WA</h1>
        <ul>
            <li>Search by Suburbs</li>
            <li>Search by Postcode</li>
            <li>Search by Suburbs</li>
        </ul>

    </body>
    <p> Today's best price is  {float(fuel_data_sorted[0]['price'])} at {fuel_data_sorted[0]['address']}, {fuel_data_sorted[0]['location']}</p>
</html>
<table>
    <thead>
        <th colspan = "1">Location</th>
        <th colspan = "1">Brand</th>
        <th colspan = "1">Price</th>
        <th colspan = "1">Address</th>
        <th colspan = "1">Day</th>
    </thead>
    
        {fuel_watch}

</table>

'''
f= open('price_table.html', 'w')
f.write(fuel_watch_site)
f.close()


