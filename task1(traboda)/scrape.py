import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.worldometers.info/coronavirus/"

# Fetching the webpage
page = requests.get(url)

# Parsing the webpage
soup = BeautifulSoup(page.content, "html.parser")

# Finding the table containing the data
table = soup.find("table", id="main_table_countries_today")

# Creating an empty list to store the data
data = []

# Iterating through the table rows
for row in table.find_all("tr")[9:19]:


    # Skipping the first row (headers)
    if "Country" in row.text:
        continue

    # Extracting the data from the row
    cols = row.find_all("td")

    country = cols[1].text.strip()
    total_cases = cols[2].text.strip()
    total_recovered = cols[4].text.strip()
    total_deaths = cols[6].text.strip()

    # Appending the data to the list
    data.append([country, total_cases, total_deaths, total_recovered])
    print(data)

# Writing the data to a CSV file
with open("Exctrated_data(covid cases).csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Country", "Total Cases", "Total recovered", "Total deaths"])
    writer.writerows(data)
