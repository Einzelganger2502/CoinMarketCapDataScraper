from celery import shared_task
from .models import Job, Task
from .coinmarketcap import CoinMarketCap

@shared_task
def scrape_coin_data(job_id, coin):
    job = Job.objects.get(job_id=job_id)
    task = Task.objects.create(job=job, coin=coin)
    
    scraper = CoinMarketCap()
    try:
        
        data = scraper.get_coin_data(coin)
        task.output = data
        task.status = 'COMPLETED'
    except Exception as e:
        task.status = 'FAILED'
        task.output = {'error': str(e)}
    finally:
        scraper.close()
        task.save()
