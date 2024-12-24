from django.shortcuts import render
from django.http.response import JsonResponse

def home(request):
    if request.method == "GET":
        context = {
            "title": "Growzone/Home"
        }
        return render(request, "app/home.html", context=context)
    return JsonResponse({
        "code": 404,
        "page": "page-not-found"
    })

def authorize(request):
    if request.method == "GET":
        context = {
            "title": "Growzone/Authorize"
        }
        return render(request, "app/authorize.html", context=context)
    elif request.method == "POST":
        return JsonResponse({
            "hub_challenge": 123456789,
            # "page": "create"
        })
    else:
        return JsonResponse({"code": 404, "data": "page-not-found"})

def authorize_message(request):
    if request.method == "GET":
        context = {
            "title": "Growzone/Authorize/Success"
        }
        return render(request, "app/authorize_message.html", context=context)
    
    return JsonResponse({"code": 404, "data": "page-not-found"})

def info(request, user_id):
    if request.method == "GET":
        context = {
            "title": "Growzone/User Info",
            "user_id": user_id,
        }
        return render(request, "app/info.html", context=context)
    # elif request.method == "POST":
    #     return JsonResponse({
    #         "code": 200,
    #         "page": "create"
    #     })
    else:
        return JsonResponse({"code": 404, "data": "page-not-found"})

def update(request, user_id):
    if request.method == "GET":
        context = {
            "title": "Update",
            "user_id": user_id,
        }
        return render(request, "app/update.html", context=context)
    # elif request.method == "POST":
    #     return JsonResponse({
    #         "code": 200,
    #         "page": "create"
    #     })
    else:
        return JsonResponse({"code": 404, "data": "page-not-found"})

def delete(request, user_id):
    if request.method == "GET":
        context = {
            "title": "Delete",
            "user_id": user_id,
        }
        return render(request, "app/delete.html", context=context)
    # elif request.method == "POST":
    #     return JsonResponse({
    #         "code": 200,
    #         "page": "create"
    #     })
    else:
        return JsonResponse({"code": 404, "data": "page-not-found"})