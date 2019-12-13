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

# grab each product
containers = page_soup.findAll("div",{"class":"card__body"})

filename = "cars.csv"
f = open(filename, "w")

headers = "Description, Milage, Location, Price\n"

f.write(headers)

for container in containers:

	description_container = container.findAll("p", {"class":"card__body-title"})
	description = description_container[0].text

	# THE NEXT 3 CONTAINERS ARE TO BE PULLED FROM THESE <li>'s (example HTML from webpage shown below). 
	# I CAN'T USE THE REACT ID AS THIS IS DIFFERENT FOR EACH CAR ON THE WEBPAGE
		# <ul class="card__body-keyinfo" data-reactid="18">
	 #   <li data-reactid="19">2016</li>
	 #   <li data-reactid="20">2.0 Diesel</li>
	 #   <li data-reactid="21">115,000 mi</li>
	 #   <li data-reactid="22">1 day</li>
	 #   <li data-reactid="23">Donegal</li>
		# </ul>

	milage_container = container.findAll("ul", {"class":"card__body-keyinfo"})
	milage = milage_container[0].text

	location_container = container.findAll("ul", {"class":"card__body-keyinfo"})
	location = location_container[0].text

	price_container = container.findAll("ul", {"class":"card__body-keyinfo"})
	price = price_container[0].text

	print("description: " + description)
	print("milage: " + milage)
	print("location: " + location)
	print("price: " + price)

	f.write(description + "," +milage + "," +location + "," +price +"\n")