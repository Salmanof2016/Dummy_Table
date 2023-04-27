from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.AjaxViewTable.as_view()),
    path('', views.ajax_table, name='ajax_table'),
    path('getFormData/', views.getFormData, name='getFormData'),
    # path('ajax/data/', views.ajax_data),
    # path('ajax/data/post/', views.ajax_data_post),
]
