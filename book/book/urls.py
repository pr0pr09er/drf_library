from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # library
    path('api/v1/', include('books.urls')),
    # tasks
    path('api/v2/', include('lessonApp.urls'))
]
