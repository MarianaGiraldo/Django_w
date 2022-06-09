from django.shortcuts import render, redirect
from .models import Passenger
from .forms import PassengerForm
import matplotlib.pyplot as plt
import pandas as pd

def all_users(request):
    users = Passenger.objects.all()
    return render(request, "passengers/all_users.html", {'users': users})

def insert_user(request):
    title = "Registrar Usuario"
    if request.method == 'GET' :
        form = PassengerForm()
    else:
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_users")
    return render(request, "passengers/register_form.html", { 'form': form, 'title': title })

def edit_user(request, id):
    title = "Editar Usuario"
    user = Passenger.objects.get( id = id )
    if request.method == 'GET' :
        form = PassengerForm( instance = user )
    else:
        form = PassengerForm(request.POST,  instance = user )
        if form.is_valid():
            form.save()
            return redirect("all_users")
    return render(request, "passengers/register_form.html", {'form': form, 'title': title })

def delete_user(request, id):
    user = Passenger.objects.get( id = id )
    user.delete()
    return redirect("all_users")


def graph_users(request):
    users = Passenger.objects.values()
    print(users)
    dataframe = pd.DataFrame(users)
    id = dataframe.id
    fullname = dataframe.full_name
    print (id, fullname)
    plt.bar(fullname, id)
    # plt.pie(id)
    plt.show()
    return redirect("all_users")