import json

from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import requests
from time import time
from django.http import HttpResponseRedirect
from .models import Form


# url = 'http://192.168.68.114:8000'


# Create your views here.
#
# def ajax_data(request):
#     data = requests.get(url + '/book/').json()
#     return JsonResponse(data, safe=False)
#
#
# def ajax_data_post(request):
#     data = requests.post(url + '/book/')
#     return JsonResponse(data)


# def table(request):
#     # if request.method == 'POST':
#     #     name = request.POST['add_name']
#     #     writer = request.POST['add_writer']
#     #     payload = {'book_name': name, 'writer': writer}
#     #     response = requests.post(url + '/book/', data=payload)
#     #
#     #     if response.status_code == 200:
#     #         return HttpResponseRedirect('/home/')
#     #     else:
#     #         error = response.text
#     #         print(error)
#     #
#     # book_list = requests.get(url + '/book/').json()
#     text = request.GET.get('button_text')
#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         t = time()
#         return JsonResponse({'seconds': t}, status=200)
#
#     th_text = request.POST.get('text')
#     result = f"I have got : {th_text}"
#     return render(request, 'table.html')

# class AjaxViewTable(View):
#     def get(self, request):
#         text = request.GET.get('button_text')
#         if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#             t = time()
#             return JsonResponse({'seconds': t}, status=200)
#         return render(request, 'table.html')
#
#     def post(self, request):
#         th_text = request.POST.get('text')
#         result = f"I have got : {th_text}"
#         return JsonResponse({'data': result}, status=200)

def ajax_table(request):
    return render(request, 'table.html')


def getFormData(request):
    form_data = Form.objects.all()
    data = list(form_data.values())
    return JsonResponse({"FormData": data})
