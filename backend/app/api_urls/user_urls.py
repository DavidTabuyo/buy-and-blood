# user_urls.py
from django.urls import path
from app.views.profile_page import holdings, buyandsell_transaction

urlpatterns = [
    path('holdings/', holdings, name='holdings'),
    path('transaction/', buyandsell_transaction, name='buyandsell_transaction')
]
