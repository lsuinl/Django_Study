from django.contrib import admin
from django.urls import path, include

from varcode import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('varcode/', include('varcode.urls'))
]
