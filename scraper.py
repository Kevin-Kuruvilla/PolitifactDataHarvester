from requests import get
from bs4 import BeautifulSoup
import csv

# converts labels to binary values 
def label_to_numeric(label):
    false_labels = ['false', 'mostly-true', 'pants-fire']
    if label in false_labels:
        return 0
    else:
        return 1

base_url = 'https://www.politifact.com/factchecks/?page='
all_quotes = []
all_labels = []

for page in range(1, 801):
    # parse html for each page
    url = base_url + str(page)
    html = get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    # get quotes from html
    quote_html = soup.find_all('div', class_='m-statement__quote')
    quotes = [quote.find('a').text.strip() for quote in quote_html]

    # get labels from html
    label_html = soup.find_all('div', class_='m-statement__meter')
    labels = [label.find('img')['alt'].strip() for label in label_html]
    labels = [label_to_numeric(label) for label in labels]

    all_quotes.extend(quotes)
    all_labels.extend(labels)

# stores data to csv file
filename = 'politifact_data.csv'
with open(filename, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Label'])
    for quote, label in zip(all_quotes, all_labels):
        writer.writerow([quote, label])