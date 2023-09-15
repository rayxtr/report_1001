from django.shortcuts import render
from django.http import JsonResponse


import requests

from django.conf import settings



def landing_page(request):
    return render(request, 'index.html')

def api_data(request):
    
    api_url = f'{settings.BASE_API_URL}Sales Invoice'
    
    headers = {
        'Authorization': f'token {settings.API_TOKEN}:{settings.SECRET_KEY}'
    }
    
    response = requests.get(api_url,headers=headers)
    data = response.json()
    return render(request,'sale.html',{'data':data})
    


def sales_invoice_report(request):
    base_url = settings.BASE_API_URL
    api_token = settings.API_TOKEN
    sec_key = settings.SECRET_KEY

   
    headers = {
        'Authorization': f'token {api_token}:{sec_key}'
    }
    data_for_chart = {
            'label': [],
           'values': []
        }

    api_url = f'{base_url}Sales Invoice'  
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        invoice_data_list = response.json()
      

      
        for invoice_data in invoice_data_list.get('data'):
          #  print(invoice_data)
            name = invoice_data.get('name', None)

            if name:
               
                invoice_url = f'{base_url}Sales Invoice/{name}'

                try:
                    response = requests.get(invoice_url, headers=headers)
                    response.raise_for_status()
                    invoice_data = response.json()

                  
                    posting_date = invoice_data.get('data').get('posting_date', None)
                    grand_total = invoice_data.get('data').get('grand_total', None)

                   
                    if posting_date is not None and grand_total is not None:
                        data_for_chart['label'].append(posting_date)
                        data_for_chart['values'].append(grand_total)
                       # print(data_for_chart)
                except requests.exceptions.RequestException as e:
                    return JsonResponse({'error': str(e)})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)})

    return render(request, 'salechart.html', {'data': data_for_chart})
