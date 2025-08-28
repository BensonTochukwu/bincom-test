from django.urls import path
from . import views

urlpatterns = [
    path('polling-unit/<int:pu_id>/',
         views.polling_unit_result, name='polling_unit_result'),
    path('lga-results/', views.lga_results, name='lga_results'),
    path('add-polling-unit/', views.add_polling_unit_results,
         name='add_polling_unit_results'),

]
