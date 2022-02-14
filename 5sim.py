#!/usr/bin python3

import requests
import sys
from operator import itemgetter

def get_size(country_names):
    size = 0

    for i in country_names:
        if (len(i) > size):
            size = len(i)
    return (size)

if len(sys.argv) > 1:
    product = sys.argv[1]
else:
    product = "uber"
countries = requests.get("https://5sim.net/v1/guest/prices?product=" + product).json()

for key, data in countries.items():

    arr = []
    prices = []
    country_names = []

    # countries
    for country_key, country_data in data.items():

        price = []
        # virtual
        for virtual_key, virtual_date in country_data.items():
            price.append(virtual_date['cost'])

        # sort prices to get most expensive
        price.sort(reverse=True)

        # append country names and price
        country_names.append(country_key)
        mytuple = (country_key, price[0])
        arr.append(mytuple)

    arr.sort(key=lambda tup: tup[1])
    size = get_size(country_names)

    for i in arr:
        print(i[0].ljust(size + 1) + ": " + str(i[1]))
    exit(0)