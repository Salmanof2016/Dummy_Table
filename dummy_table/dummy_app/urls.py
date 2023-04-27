from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.AjaxViewTable.as_view()),
    # path('ajax/data/', views.ajax_data),
    # path('ajax/data/post/', views.ajax_data_post),
]
