
from django.contrib import admin
from django.urls import include, path
from report import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.landing_page, name='landing-page'),
    
     path('sales-invoice/', views.sales_invoice_report, name='sales-invoice'),
     path('api_data/', views.api_data,name = 'api_data'),
      path('landing_page/', views.landing_page,name = 'landing_page'),
]
