# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import re

# A function to scrape F1 Calendar
def calendarScrapper(url):

    # Using requests send a get request
    r = requests.get(url).text

    # Store the response as a soup
    soup = BeautifulSoup(r, "html.parser")
    
    # Loop into every item and extract necessary details
    for item in soup.find_all("fieldset", class_="event-item"):
        try:
            round_no = item.find("legend").text

            _info = item.find(class_="event-info").text

            _month = re.sub(r"[\n 0-9\-]", "", _info)
            # Check if event occuring across months and assign start and end months accordingly
            start_month, end_month = _month[:3], _month[3:] if len(_month) > 3 else _month[:3] 

            # Extract start and end date info
            start_date, end_date = re.sub(r"[\n a-zA-Z]", "", _info).split("-")[:2]

            # Initialize country and event_name parameters to empty string as it might be empty for some categories like esports
            country, event_name = "", ""
        
            _detail = item.find(class_="event-details").text
            country, event_name = (_detail.strip().split(" \n"))
        except:
            pass

        print(f"{round_no} | {country} | {start_month}-{start_date} to {end_month}-{end_date}")

url = "https://www.formula1.com/en/racing/2023.html"

calendarScrapper(url)