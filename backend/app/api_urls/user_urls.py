# user_urls.py
from django.urls import path
from app.views.profile_page import holdings, buyandsell_transaction, set_investing_plan

urlpatterns = [
    path('holdings/', holdings, name='holdings'),
    path('transaction/', buyandsell_transaction, name='buyandsell_transaction'),
    path('set-investing-plan/<int:id>/', set_investing_plan, name='set_investing_plan'),
]
