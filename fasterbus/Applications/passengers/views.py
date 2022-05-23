from django.shortcuts import render

def all_users(request):
    users = None
    return render(request, "passengers/all_users.html", {'users': users})

def insert_user(request):
    return render(request, "passengers/register_form.html", {})

def edit_user(request, id):
    return render(request, "passengers/edit_user.html", {})
