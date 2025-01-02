import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape quotes
def scrape_quotes():
    base_url = input("Enter the url:")
    quotes = []
    
    # Loop through the first 10 pages
    for page in range(1, 11):
        response = requests.get(f"{base_url}{page}/")
        if response.status_code != 200:
            print("Failed to retrieve the webpage.")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all quote elements on the page
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('small', class_='author').text
            author = quote.find('span', class_='text').text
            quotes.append({'author': author, 'quote': text})
    
    return quotes

# Save scraped data to CSV
def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('quotes.csv', index=False)

# Main execution
if __name__ == "__main__":
    quotes_data = scrape_quotes()
    save_to_csv(quotes_data)
    print("Quotes scraped and saved to quotes.csv.")
