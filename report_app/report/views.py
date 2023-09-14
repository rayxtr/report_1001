from django.shortcuts import render
from django.http import JsonResponse


import requests

from django.conf import settings

def landing_page(request):
    return render(request, 'index.html')


def sales_invoice_report(request):
    base_url = settings.BASE_API_URL
    api_token = settings.API_TOKEN
    sec_key = settings.SECRET_KEY
    api_url = f'{base_url}Sales Invoice'
    
    headers = {
        'Authorization': 'Bearer {api_token}:{sec_key}'
    }
    
    try:
        response = requests.get(api_url,headers=headers)
        response.raise_for_status()
        data = response.json()
        
        data_for_chart = {
            'label':[entry['date'] for entry in data],
            'values':[entry['amount'] for entry in data]
        }
        return JsonResponse(data_for_chart)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error':str(e)})