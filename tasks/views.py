from django.shortcuts import render,HttpResponse

# Create your views here.

def task_list(request):
    return HttpResponse("Task Manager Home")