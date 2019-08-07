from django.urls import path
from . import views

# urlpatterns => fix
urlpatterns = [
    # D/utils/cube/<정수>/ * 슬래쉬 => 앞x 뒤o
    path('cube/<int:num>/', views.cube),
    # utils/check_int/<정수>/
    path('check_int/<int:num>/', views.check_int), 
    # utils/pick_lotto/
    path('pick_lotto/', views.pick_lotto),
]
