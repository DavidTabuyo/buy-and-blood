# assets_urls.py
from django.urls import path
from app.views.invplan_view import invplan_details, invplan_list, best_plan

urlpatterns = [
    path('best/', best_plan , name='asset-detail'),
    path('details/<int:id>/', invplan_details, name='asset-detail'),
    path('list/', invplan_list, name='asset-detail'),
]
