from django.urls import path
import Applications.buses.views as b

urlpatterns = [
    path('buses', b.all_buses, name="all_buses"),
    path('insert-bus', b.insert_bus, name="insert_bus"),
    path('buses/edit/<int:id>', b.edit_bus, name="edit_bus")
]