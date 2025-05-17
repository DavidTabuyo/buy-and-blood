# user_urls.py
from django.urls import path
from app.views.profile_page import holdings, buyandsell_transaction, set_investing_plan, holding
from app.views.auth_views import logout
from app.views.invplan_view import invplan_details

urlpatterns = [
    path('holding/<str:asset_id>/', holding, name='holding'),
    path('holdings/', holdings, name='holdings'),
    path('logout/', logout, name='holdings'),
    path('transaction/', buyandsell_transaction, name='buyandsell_transaction'),
    path('set-investing-plan/<int:id>/', set_investing_plan, name='set_investing_plan'),
    path('investing-plan/', invplan_details, name='set_investing_plan'),
]
