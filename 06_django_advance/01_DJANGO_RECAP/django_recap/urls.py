from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 계정 페이지 
    path('home/', include('home.urls')),
    path('board/', include('board.urls')),
    path('poll/', include('poll.urls')),
]
