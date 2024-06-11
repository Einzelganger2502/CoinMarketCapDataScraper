import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from .utils import Utils



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
        
        price=Utils.clean_number(soup.find('span',class_='sc-d1ede7e3-0 fsQm base-text').text)
        price_change=Utils.clean_number(soup.find('p',class_='sc-71024e3e-0 sc-58c82cf9-1 ihXFUo iPawMI').text)
        sign_check= soup.find('p',class_='sc-71024e3e-0 sc-58c82cf9-1 ihXFUo iPawMI')['color']
        #Checking whether there is an increase or decrease in price
        if(sign_check=='red'):
            price_change*=-1

        #Handling elements with same class name
        articles = soup.find_all('dd', class_='sc-d1ede7e3-0 hPHvUM base-text')
        ranks = soup.find_all('span',class_='text slider-value rank-value')
        text_values = [dd.get_text(strip=True) for dd in articles]
        rank_values = [dt.get_text(strip=True) for dt in ranks]
        market_cap=Utils.extract_number(text_values[0])
        market_cap_rank=(int)(rank_values[0].replace('#',' '))
        volume=Utils.extract_number(text_values[1])
        volume_rank=(int)(rank_values[1].replace('#',' '))
        volume_change=Utils.clean_number(text_values[2])
        circulating_supply = Utils.clean_integer(text_values[3])
        total_supply=Utils.clean_integer(text_values[4])
        diluted_market_cap = Utils.clean_number(text_values[6])

        contracts = []
        contract_elements = soup.find_all('div', class_='sc-d1ede7e3-0 sc-7f0f401-0 sc-96368265-0 bwRagp gQoblf eBvtSa flexStart')
        for element in contract_elements:
            href_tag=soup.find('a',class_='chain-name')
            href_value=href_tag.get('href')
            contract = {
                'name': element.find('span', class_='sc-71024e3e-0 dEZnuB').text,
                'address': href_value
            }
            contracts.append(contract)
    
        official_links = []
        socials=[]
        link_elements = soup.find_all('div', class_="sc-d1ede7e3-0 sc-7f0f401-0 gRSwoF gQoblf")
        # Extract the name and href for each link
        for element in link_elements:
            link_href = element.find('a',href=True)['href']
            link_name = element.find('a').text.strip()
            title=element.parent.parent.previous_sibling.text
            if(title=='Socials'):
                Social={
                    'name':link_name,
                    'url':link_href
                }
                socials.append(Social)
            elif(title=='Official links'):    
                official_link = {
                    'name': link_name,
                    'link': link_href
                }
                official_links.append(official_link)

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
            "official_links": official_links,
            "socials": socials,
        }

    def close(self):
        self.driver.quit()

    
