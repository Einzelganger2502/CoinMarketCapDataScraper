# Crypto Scraper API

This project is a Django REST Framework API that scrapes cryptocurrency data from CoinMarketCap. It utilizes Celery for task management and returns the scraped data in a JSON response.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
  
## Introduction

The Crypto Scraper API is designed to provide up-to-date cryptocurrency data by scraping CoinMarketCap. It includes features like scheduled tasks to update data periodically using Celery.

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST Framework
- Celery
- Redis (for Celery broker)
- WebDriver Manager
- Requests
- BeautifulSoup4
- Postman App (if you want to locally test the APIs)

## Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/Einzelganger2502/CoinMarketCapDataScraper.git
   cd CoinMarketCapDataScraper

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies**
   ```sh
   pip install -r requirements.txt

4. **Set up Redis**
Ensure that you have Redis installed and running. You can follow instructions from the [ Redis documentation](https://redis.io/docs/latest/) to install it.
   
5. **Run Migrations**
   ```sh
   python3 manage.py migrate

## Running Instructions
1. **Start the Django Development Server**
   ```sh
   python3 manage.py runserver
   
2. **Start the Celery Worker**
   ```sh
   celery -A crypto_scraper worker --loglevel=info

## API Endpoints
1. **/api/taskmanager/start_scraping [POST]**<br>
   This will take in a list payload [“duko”, “notcoin”, “gorilla-token”] which are names of the crypto coins and submit a scraping job(celery will be used) to be run for these coins parallely and return back a job id.Following image depicts the same.
   ![Sending the Post Request](https://github.com/Einzelganger2502/CoinMarketCapDataScraper/blob/main/images/Screenshot%202024-06-11%20145229.png)
   ![Response Payload](https://github.com/Einzelganger2502/CoinMarketCapDataScraper/blob/main/images/Screenshot%202024-06-11%20145252.png)
   
2. **/api/taskmanager/scraping_status/<job_id> [GET]**<br>
   From the job_id received in the previous API, we can query this API and it will return the currently scraped data for that job. Following image depicts the JSON repsonse we get for the above JOB_ID
   ![Sending the Get Request using JOB_ID](https://github.com/Einzelganger2502/CoinMarketCapDataScraper/blob/main/images/Screenshot%202024-06-11%20145312.png)
   ![The Data Scraped](https://github.com/Einzelganger2502/CoinMarketCapDataScraper/blob/main/images/Screenshot%202024-06-11%20145348.png)

3. **Response Payload Structure**<br>
   This is the JSON structure of the scraped data after hitting the above endpoints.
   ```sh
   {
    "job_id": "644f9d8a-09e9-45e3-af54-0d6c03e93731",
    "tasks": [
        {
            "coin": "GORILLA-TOKEN",
            "output": {
                "price": 0.004141,
                "price_change": -9.1,
                "market_cap": 3522052,
                "market_cap_rank": 1494,
                "volume": 640633,
                "volume_rank": 1381,
                "volume_change": 18.19,
                "circulating_supply": 850606814,
                "total_supply": 898930378,
                "diluted_market_cap": 3722142.0,
                "contracts": [
                    {
                        "name": "Ethereum: ",
                        "address": "https://etherscan.io/token/0x33C04Bed4533e31f2Afb8AC4a61A48Eda38C4fA0"
                    }
                ],
                "official_links": [
                    {
                        "name": "Website",
                        "link": "https://gorillatoken.io/"
                    },
                    {
                        "name": "Whitepaper",
                        "link": "https://gorilla.gitbook.io/gorilla-white-paper/"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏Twitter",
                        "url": "https://twitter.com/gorillatokenio"
                    },
                    {
                        "name": "Telegram",
                        "url": "https://t.me/gorillatokenio"
                    }
                ]
            },
            "status": "COMPLETED"
        },
        {
            "coin": "DUKO",
            "output": {
                "price": 0.004153,
                "price_change": -11.01,
                "market_cap": 40138374,
                "market_cap_rank": 688,
                "volume": 6202843,
                "volume_rank": 497,
                "volume_change": 15.45,
                "circulating_supply": 9663955990,
                "total_supply": 9999609598,
                "diluted_market_cap": 41532482.0,
                "contracts": [
                    {
                        "name": "Solana: ",
                        "address": "https://solana.fm/address/HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
                    }
                ],
                "official_links": [
                    {
                        "name": "Website",
                        "link": "https://dukocoin.com/"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏Twitter",
                        "url": "https://twitter.com/dukocoin"
                    },
                    {
                        "name": "Telegram",
                        "url": "https://t.me/+jlScZmFrQ8g2MDg8"
                    }
                ]
            },
            "status": "COMPLETED"
        },
        {
            "coin": "NOTCOIN",
            "output": {
                "price": 0.01623,
                "price_change": -12.94,
                "market_cap": 1662397095,
                "market_cap_rank": 58,
                "volume": 699370998,
                "volume_rank": 15,
                "volume_change": 42.07,
                "circulating_supply": 102701033769,
                "total_supply": 102701033769,
                "diluted_market_cap": 1662397095.0,
                "contracts": [
                    {
                        "name": "TON: ",
                        "address": "https://tonscan.org/address/EQAvlWFDxGF2lXm67y4yzC17wYKD9A0guwPkMs1gOsM__NOT"
                    }
                ],
                "official_links": [
                    {
                        "name": "Website",
                        "link": "https://notco.in/"
                    },
                    {
                        "name": "Whitepaper",
                        "link": "https://cdn.joincommunity.xyz/notcoin/Notcoin_Whitepaper.pdf"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏Twitter",
                        "url": "https://twitter.com/thenotcoin"
                    },
                    {
                        "name": "Telegram",
                        "url": "https://t.me/notcoin"
                    }
                ]
            },
            "status": "COMPLETED"
        }
    ]
}

