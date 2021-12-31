from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

def web_scrape():
	url = "https://www.worldometers.info/coronavirus/#countries"
	req = Request(url, headers={'User-Agent':"Mozilla/5.0"})

	webpage = urlopen(req)
	page_soup = soup(webpage, "html.parser")

	table = page_soup.findAll("table", {'id': 'main_table_countries_yesterday'})

	containers = table[0].findAll('tr', {'style':''})
	title = containers[0]

	del containers[0]

	all_data = []
	clean = True

	for country in containers:
		country_data = []
		country_container = country.findAll('td')
		if country_container[1].text == 'China':
			continue
		for i in range(1, len(country_container)):
			final_feature = country_container[i].text
			if clean:
				if i != 1 and i != len(country_container)-1:
					final_feature = final_feature.replace(',',"")

					if final_feature.find('+') != -1:
						final_feature = final_feature.replace("+", "")
						final_feature = float(final_feature)

					elif final_feature.find("-") != -1:
						final_feature = final_feature.replace("-", "")
						final_feature = float(final_feature)*-1

			if final_feature == 'N/A':
				final_feature = 1
			elif final_feature == "" or final_feature == " ":
				final_feature = -1

			country_data.append(final_feature)
		all_data.append(country_data)
	return all_data