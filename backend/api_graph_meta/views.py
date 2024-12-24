from django.shortcuts import render, redirect
from django.http.response import JsonResponse

def authorize(request):
    if request.method == "POST":
        form = request.POST
        print(form)
        return redirect('app_user_account_authorize_message')
    else:
        return JsonResponse({"code": 404, "data": "page-not-found"})

def info(request, user_id):
    if request.method == "POST":
        return JsonResponse({
            "code": 200,
            "user_id": user_id,
            "page": "info"
        })
    else:
        return JsonResponse({"code": 404, "data": "page-not-found"})

def update(request, user_id):
    if request.method == "POST":
        return JsonResponse({
            "code": 200,
            "user_id": user_id,
            "page": "update"
        })
    else:
        return JsonResponse({"code": 404, "data": "page-not-found"})

def delete(request, user_id):
    if request.method == "POST":
        return JsonResponse({
            "code": 200,
            "user_id": user_id,
            "page": "delete"
        })
    else:
        return JsonResponse({"code": 404, "data": "page-not-found"})
