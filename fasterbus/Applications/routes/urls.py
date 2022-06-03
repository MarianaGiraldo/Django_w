from django.urls import path
import Applications.routes.views as r

urlpatterns = [
    path('routes', r.all_routes, name="all_routes"),
    path('insert-route', r.insert_route, name="insert_route"),
    path('routes/edit/<int:id>', r.edit_route, name="edit_route"),
    path('routes/delete/<int:id>', r.delete_route, name="edit_route")
]