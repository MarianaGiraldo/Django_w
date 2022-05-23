from django.urls import path
import Applications.passengers.views as p

urlpatterns = [
    path('users', p.all_users, name="all_users"),
    path('register', p.insert_user, name="insert_user"),
    path('users/edit/<int:id>', p.edit_user, name="edit_user")
]