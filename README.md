# Web Scraping Project

A simple Python web scraping project that extracts laptop data from Amazon India.

## Features

* Scrapes product titles
* Scrapes product images
* Scrapes ratings
* Scrapes prices
* Identifies sponsored and organic results
* Saves data into CSV format

---

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

---

## Installation

Clone the repository:

```bash id="7fhon7"
git clone <repo-url>
cd web-scraping-project
```

Install dependencies:

```bash id="j55jyz"
pip install -r requirements.txt
```

---

## Run the Scraper

```bash id="y6j0i5"
python scraper.py
```

---

## Output

The script generates a CSV file:

```text id="eb8lcb"
amazon_laptops_YYYYMMDD_HHMMSS.csv
```

Example columns:

* Title
* Image
* Rating
* Price
* Result Type

---

## Notes

* Uses headers to reduce blocking
* Includes delay between requests
* Intended for educational purposes only

---

## Future Improvements

* Pagination support
* Proxy rotation
* Selenium integration
* Multi-category scraping
* Database storage
* API integration
