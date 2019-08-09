# master urls

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls'))  # 앞에는 없고 뒤에만 '/' 가 있다. => django 만 그렇다... 
]
