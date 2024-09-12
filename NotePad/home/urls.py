from django.urls import path


from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutinInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]

    #path('home', views.casa),
    # path('home', views.HomeView.as_view()),

    #path('autorizado', views.autorize)
    # path('autorizado', views.AuthorizedView.as_view()),