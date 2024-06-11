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
   This will take in a list payload [“duko”, “notcoin”, “gorilla-token”] which are names of the crypto coins and submit a scraping job(celery will be used) to be run for
   these coins parallely and return back a job id.Following image depicts the same.
   
3. **/api/taskmanager/scraping_status/<job_id> [GET]**<br>
   From the job_id received in the previous API, we can query this API and it will return the currently scraped data for that job. Following image depicts the JSON repsonse     we get for the above JOB_ID

