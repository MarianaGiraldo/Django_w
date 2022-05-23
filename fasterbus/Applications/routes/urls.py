from django.urls import path
import Applications.routes.views as r

urlpatterns = [
    path('routes', r.all_routes, name="all_routes"),
]