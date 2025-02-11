# stock/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_merolagani():
    # Site URL
    url = "https://merolagani.com/LatestMarket.aspx"
    
    # Make a GET request to fetch the raw HTML data
    con = requests.get(url)
    soup = BeautifulSoup(con.text, 'lxml')  # Code of the page
    table = soup.find('table', class_="table table-hover live-trading sortable")  # Table of data

    headers = [i.text for i in table.find_all('th')]  # Extract headers
    data = [j for j in table.find_all('tr', {"class": ["decrease-row", "increase-row", "nochange-row"]})]  # Extract rows

    # Extract the company name (title attribute) from the anchor tags
    fullname = [j.get('title') for j in table.find_all('a', {"target": ["_blank"]})]

    # Format data as a list of dictionaries
    result = [{headers[index]: cell.text for index, cell in enumerate(row.find_all("td"))} for row in data]

    # Combine data and name into one dictionary
    new_data = [
        {
            'Name': fullname[kk],
            'Symbol': result[kk]['Symbol'],
            'LTP': result[kk]['LTP'],
            'Change': result[kk]['% Change'],
            'High': result[kk]['High'],
            'Low': result[kk]['Low'],
            'Open': result[kk]['Open'],
            'Qty.': result[kk]['Qty.']
        }
        for kk in range(len(fullname))
    ]
    
    return new_data
