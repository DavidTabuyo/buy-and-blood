# assets_urls.py
from django.urls import path
from app.views.homepage import best_plan
from app.views.invplan_view import invplan_details

urlpatterns = [
    path('best/', best_plan , name='asset-detail'),
    path('details/<int:id>/', invplan_details, name='asset-detail'),
]
