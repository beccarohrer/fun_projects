#   Fun Exercise - Get Brooklyn Weather
#   Author: Becca Rohrer
#   Last updated: 7/27/2022

from bs4 import BeautifulSoup
import requests

print(f'\nFinding Brooklyn weather for today...\n')
response = requests.get('https://weather.com/weather/hourbyhour/l/01d4306a0f4d8d9ca283fce0bcfb508b7cee58c6a1cf8a84e36fd5e43ae58c87')
soup = BeautifulSoup(response.text, 'html.parser')

datetime_tags = soup.find_all('h3', attrs={"data-testid":"daypartName"})
temp_tags = soup.find_all('span', attrs={"data-testid":"TemperatureValue", "class":"DetailsSummary--tempValue--1K4ka"})
precip_tags = soup.find_all('span', attrs={"data-testid":"PercentageValue"})

precip_tags_filtered = [] #there are "data-testid" : "percentagevalue" tags with more attrs corresponding to humidity and cloudcover that we want to filter out
for tag in precip_tags:
    if len(tag.attrs) == 1:
        precip_tags_filtered.append(tag)

weather_dict = {}

for i in range(12):
    inner_list = []
    inner_list.append(datetime_tags[i].text)
    inner_list.append(temp_tags[i].text)
    inner_list.append(precip_tags_filtered[i].text)
    weather_dict[i] = inner_list

for i in range(12):
    print(f'{weather_dict[i][0]}, {weather_dict[i][1]}, {weather_dict[i][2]} chance of rain')


