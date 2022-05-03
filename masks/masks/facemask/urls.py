from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
 
urlpatterns = [
  path('', views.home,name="home"),
  path('sucess/',views.success,name="sucess"),
  path('buscar/',views.buscar,name="buscar"),
  path('data/',views.userdata,name="data"),
  path('soporte/',views.support,name="support"),
  path('sent/',views.successcomment,name="sent"),
  path('sports/',views.ViewMasksSport.as_view(),name="sports"),
  path('kids/',views.ViewMasksKids.as_view(),name="kids"),
  path('casual/',views.ViewMasksCasual.as_view(),name="casual"),
  path('different/',views.ViewMasksRar.as_view(),name="different"),
  path('user/',views.UserBoard.as_view(),name='userboard'),
  url('login/', LoginView.as_view(), name= 'login'),
  url('logout/', LogoutView.as_view(), name= 'logout'),
  url('create/', views.CreateMask, name= 'create'),
  url('signup/',views.signup, name='signup'),
]