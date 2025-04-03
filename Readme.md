# Books to Scrape Web Scraper

## Overview
This Python script scrapes book data from the website (http://books.toscrape.com/) and saves the extracted details into a CSV file. The script collects book titles, prices, stock availability, and ratings from the first five pages of the website.

## Features
- Scrapes book data from the first five pages of the catalog.
- Extracts the following details:
  - **Title**: Name of the book.
  - **Price**: Cost of the book.
  - **Stock Availability**: Indicates whether the book is in stock.
  - **Rating**: Book rating (e.g., One, Two, Three, etc.).
- Saves the extracted data into a CSV file (`books_data.csv`).

## Requirements
Make sure you have the following dependencies installed before running the script:

```bash
pip install requests beautifulsoup4 pandas
```

## How to Run
1. Clone or repository from https://github.com/Yuvijadeja/web_scrapper.
2. Install the required dependencies using the command above.
3. Run the script:
   
   ```bash
   python script_name.py
   ```

4. The script will scrape data and save it to `books_data.csv` in the same directory.

## Code Explanation
- The script iterates through five pages of the Books to Scrape website.
- It sends an HTTP request to each page and parses the HTML using BeautifulSoup.
- Extracted book details are stored in a list and then converted into a Pandas DataFrame.
- Finally, the data is saved to a CSV file.

## Output
After running the script, a CSV file (`books_data.csv`) is generated with the following structure:

| Title | Price | Stock | Rating |
|-------|-------|-------|--------|
| Book1 | £20.99 | In stock | Three |
| Book2 | £15.99 | Out of stock | Five |

## Notes
- The script uses a `User-Agent` header to mimic a real browser request.
- The `Rating` is extracted as a word (e.g., "One", "Two", etc.), representing a numerical rating.

## License
This project is for educational purposes and should be used responsibly for ethical web scraping practices.
