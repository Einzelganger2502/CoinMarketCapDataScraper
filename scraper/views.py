from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job, Task
from .tasks import scrape_coin_data
import uuid

class StartScrapingView(APIView):
    def post(self, request):
        coins = request.data.get('coins')
        if not all(isinstance(coin, str) for coin in coins):
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)
        
        job = Job.objects.create()
        for coin in coins:
            scrape_coin_data.delay(job.job_id, coin)
        
        return Response({"job_id": job.job_id}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        try:
            # Query the database for the job using UUID
            job = Job.objects.get(job_id=job_id)
            print(f"Retrieved job: {job}")

        except Job.DoesNotExist:
            print("Job not found")
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Exception: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        tasks = job.tasks.all()
        response_data = {
            "job_id": job.job_id,
            "tasks": [
                {
                    "coin": task.coin.upper(),
                    "output": task.output,
                    "status": task.status,
                }
                for task in tasks
            ]
        }
        return Response(response_data)
