#   Fun Exercise - Read my horoscope
#   Author: Becca Rohrer
#   Last updated: 7/13/2022

from bs4 import BeautifulSoup
import requests
import textwrap

while True:
    selection = input('What\'s your sign? ')
    selection_lower = selection.lower()
    if selection_lower in ['taurus','gemini','cancer','leo','libra','virgo','libra','scorpio',
                 'sagittarius','capricorn','aquarius','pisces']:
        break

horoscope_ids = {'taurus':"src-hp-taur",
                 'gemini':"src-hp-gem",
                 'cancer':"src-hp-canc",
                 'leo':"src-hp-leo",
                 'libra':"scr-hp-lib",
                 'virgo':"src-hp-virgo",
                 'libra':"src-hp-lib",
                 'scorpio':"src-hp-scpo",
                 'sagittarius':"src-hp-sag",
                 'capricorn':"src-hp-cap",
                 'aquarius':"src-hp-aqua",
                 'pisces':"src-hp-pisc"}

selection_id = horoscope_ids[selection_lower]
print(f'\nFinding your horoscope for today, {selection}...\n')
response = requests.get('https://www.horoscope.com/us/index.aspx')
soup = BeautifulSoup(response.text, 'html.parser')

specific_link_tag = soup.find('a', id=selection_id)
subpage_link = specific_link_tag.attrs['href']
subpage_link_formatted = f'http://horoscope.com{subpage_link}'
sign_specific_response = requests.get(subpage_link_formatted)

sign_soup = BeautifulSoup(sign_specific_response.text, 'html.parser')
horoscope_content_tag = sign_soup.find('p')
formatted_output_text = textwrap.wrap(text=horoscope_content_tag.text, width=70)
for line in formatted_output_text:
    print(line)


