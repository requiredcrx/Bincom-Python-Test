# importing beautifulsoup to parse the html content
from bs4 import BeautifulSoup

# reading the html file
with open('Resources.html', 'r') as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, "html.parser")

colors = []
for row in soup.find_all('tr'):
    day_color = row.find_all('td')[1].text.strip().split(', ')
    colors.extend(day_color)


def get_color_frequencies():
    from collections import Counter
    return Counter(colors)


