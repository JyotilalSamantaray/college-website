from django.contrib import admin
from django.urls import path
from imit import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('notices/',views.notices,name = "notices"),
    path('admission/',views.admission,name = "admission"),
    path('register/',views.register,name = "register"),
    path('certificate/',views.certificate,name = "certificate"),
    path('facilities/',views.facilities,name = "facilities"),
    path('contact/',views.contact,name = "contact"),
    path('login/',views.login,name = "login"),
    path('placement/',views.placement,name = "placement"),
    path('library/',views.library,name = "library"),
    path('computerlab/',views.computerlab,name = "computerlab"),
    path('ladieshostel/',views.ladieshostel,name = "ladieshostel"),
    path('boyshostel/',views.boyshostel,name = "boyshostel"),
]
