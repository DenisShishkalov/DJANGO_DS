from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('contacts/', views.contact, name='contacts'),
]
