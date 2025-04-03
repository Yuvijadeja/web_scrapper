import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
URL = "http://books.toscrape.com/catalogue/page-1.html"

# Headers to mimic a real browser
HEADERS = {"User-Agent": "Mozilla/5.0"}

# List to store book details
books = []

# Loop through multiple pages
for page in range(1, 6):  # Scraping first 5 pages
    response = requests.get(f"http://books.toscrape.com/catalogue/page-{page}.html", headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        stock = "In stock" if "In stock" in book.find("p", class_="instock").text else "Out of stock"
        rating = book.p["class"][1]  # Rating class e.g., "One", "Two", "Three"

        books.append({"Title": title, "Price": price, "Stock": stock, "Rating": rating})

# Save data to CSV
df = pd.DataFrame(books)
df.to_csv("books_data.csv", index=False)

print("Scraping Completed! Data saved to books_data.csv")
