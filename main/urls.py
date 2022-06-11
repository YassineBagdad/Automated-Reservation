from django.urls import URLPattern, path
from django.urls import re_path as url
#from main import views as core_views
 
from . import views

urlpatterns = [
    path("<int:id>",views.index,name="index"),
    #path("login/",views.login,name="login"),
    path("",views.home,name="home"),
    # path("create/",views.create,name="create"),
    path("index1/",views.index1,name="index1"),
    #path("simple_function/",views.simple_function),
    
    path("register/", views.register_request, name="register"),

    path("signup1/", views.register_request, name="register"),

    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

    path("settings/", views.settings, name= "settings"),


    path("click/", views.request_page, name= "request_page"),

    url(r'^signup/$', views.signup, name='signup'),

    # url(r'^mybtn/$', views.request_page, name='request_page'),
    #path('signup/', views.signup, name='signup'),

]

