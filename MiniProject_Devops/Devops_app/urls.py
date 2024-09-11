from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("",views.home),
    path("contacts",views.contact),
    path("service",views.getServices),
    path("checkout",views.checkout),
    path("cart/<service>",views.cart),
    
]
