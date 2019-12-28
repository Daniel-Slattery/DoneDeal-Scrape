#!/usr/bin/python3

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.donedeal.ie/cars?fuelType=Diesel&make=BMW;model:4%20Series,4-Series&year_from=2016&year_to=2016&engine_to=2.1&source=private&country=Ireland'

# opening up connection, grabbing the page
uClient = uReq(my_url)

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

# grab each car on page
containers = page_soup.findAll("div",{"class":"card__body"})

filename = "cars.csv"
f = open(filename, "w")

headers = "Description, Milage, Location, Price\n"

f.write(headers)

for container in containers:

# If ul class="card__body-keyinfo" inside card then execute
# (avoid scanning through empty ads on page)
	description_container = container.findAll("p", {"class":"card__body-title"})
	description = description_container[0].text

	info_container = container.findAll("ul", {"class":"card__body-keyinfo"})
	info = info_container[0].text

	miles = info.split('Diesel',1)
	milage = miles[1]
	miles2 = milage.split(' ',1)

	type_, *vals = info.split('days')
	location = vals[0]

	price_container = container.findAll("p", {"class":"card__price"})
	price = price_container[0].text

	print("Description: " + description)
	print("Milage: " + miles2[0])
	print("Location: " + location)
	print("Price: " + price)
	print(" ")
	# print("info: " + info)

	f.write(description + "," +miles2[0] + "," +location + "," +price +"\n")
