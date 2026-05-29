import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

# Headers to avoid blocking

headers = {
"User-Agent": (
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, like Gecko) "
"Chrome/124.0.0.0 Safari/537.36"
),
"Accept-Language": "en-US,en;q=0.9"
}

# Amazon search URL

url = "https://www.amazon.in/s?k=laptops"

# Send request

response = requests.get(url, headers=headers)

# Check response

if response.status_code != 200:
print("Failed to fetch webpage")
exit()

# Parse HTML

soup = BeautifulSoup(response.content, "html.parser")

# Find all products

products = soup.find_all(
"div",
{"data-component-type": "s-search-result"}
)

# Store data

data = []

for product in products:

```
# TITLE
title_tag = product.find("h2")
title = (
    title_tag.get_text(strip=True)
    if title_tag else "N/A"
)

# IMAGE
image_tag = product.find("img", class_="s-image")
image = (
    image_tag["src"]
    if image_tag else "N/A"
)

# RATING
rating_tag = product.find(
    "span",
    class_="a-icon-alt"
)

rating = (
    rating_tag.get_text(strip=True)
    if rating_tag else "N/A"
)

# PRICE
price_tag = product.find(
    "span",
    class_="a-price-whole"
)

price = (
    price_tag.get_text(strip=True)
    if price_tag else "N/A"
)

# RESULT TYPE
sponsored = product.find(
    "span",
    string="Sponsored"
)

result_type = (
    "Ad"
    if sponsored else "Organic"
)

# Save data
data.append({
    "Title": title,
    "Image": image,
    "Rating": rating,
    "Price": price,
    "Result Type": result_type
})

# Delay to avoid blocking
time.sleep(1)
```

# Create DataFrame

df = pd.DataFrame(data)

# Show output

print(df.head())

# Create filename with timestamp

timestamp = datetime.now().strftime(
"%Y%m%d_%H%M%S"
)

filename = f"amazon_laptops_{timestamp}.csv"

# Save CSV

df.to_csv(
filename,
index=False,
encoding="utf-8-sig"
)

print(f"\nData saved successfully in {filename}")
