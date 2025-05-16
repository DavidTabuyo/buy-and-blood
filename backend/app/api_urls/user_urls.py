# user_urls.py
from django.urls import path
from app.views.profile_page import holdings, investing_plan

urlpatterns = [
    path('holdings/', holdings, name='holdings'),
<<<<<<< HEAD
    path('investing-plan/', investing_plan, name='investing_plan'),
=======
    path('transaction/', buyandsell_transaction, name='buyandsell_transaction'),
    path('set-investing-plan/:id/', set_investing_plan, name='set_investing_plan'),
>>>>>>> feature/endpoints
]
