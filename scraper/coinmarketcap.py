import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


class CoinMarketCap:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    
    def get_coin_data(self, coin):
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        

        
        price=soup.find('span',class_='sc-d1ede7e3-0 fsQm base-text').text
        price_change=soup.find('p',class_='sc-71024e3e-0 sc-58c82cf9-1 ihXFUo iPawMI').text
        market_cap=soup.find('dd',class_='sc-d1ede7e3-0 hPHvUM base-text').text
        market_cap_rank=soup.find('span',class_='text slider-value rank-value').text
        volume=soup.find('dd',class_='sc-d1ede7e3-0 hPHvUM base-text').text
        volume_rank=soup.find('span',class_='text slider-value rank-value').text
        volume_change=soup.find('p',class_='sc-71024e3e-0 sc-58c82cf9-1 ihXFUo iPawMI').text

        #Handling elements with same class name
        articles = soup.find_all('dd', class_='sc-d1ede7e3-0 hPHvUM base-text')
        text_values = [dd.get_text(strip=True) for dd in articles]
        circulating_supply = text_values[3]
        total_supply=text_values[4]
        diluted_market_cap = text_values[6]

        contracts = []
        contract_elements = soup.find_all('div', class_='sc-d1ede7e3-0 sc-7f0f401-0 sc-96368265-0 bwRagp gQoblf eBvtSa flexStart')
        for element in contract_elements:
            href_tag=soup.find('a',class_='chain-name')
            href_value=href_tag.get('href')
            contract = {
                'name': self._get_text(element.find('span', class_='sc-71024e3e-0 dEZnuB')),
                'address': href_value
            }
            contracts.append(contract)

        # Return a structured data dictionary
        return {
            "price": price,
            "price_change": price_change,
            "market_cap": market_cap,
            "market_cap_rank": market_cap_rank,
            "volume": volume,
            "volume_rank":volume_rank,
            "volume_change": volume_change,
            "circulating_supply": circulating_supply,
            "total_supply": total_supply,
            "diluted_market_cap": diluted_market_cap,
            "contracts": contracts,
            # "official_links": official_links,
            # "socials": socials,
        }

    def close(self):
        self.driver.quit()

    
