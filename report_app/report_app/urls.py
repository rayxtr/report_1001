
from django.contrib import admin
from django.urls import include, path
from report import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.landing_page, name='landing-page'),
    
     path('report/templates/sales_invoice_chart.html', views.sales_invoice_report, name='sales-invoice'),
]
