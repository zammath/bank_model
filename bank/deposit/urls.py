from django.urls import path
from . import views

app_name = "deposit"

urlpatterns = [
    path('', views.deposit, name='deposit_page'),
    path('deposit/', views.predict_chances, name='submit_deposit'),
    path('results/', views.view_results, name='results')
    
]

