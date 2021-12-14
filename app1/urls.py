from django.urls import path
from django.urls.conf import include
from.import views

urlpatterns = [
    path('',views.signupfn,name='sp'),
    path('active',views.afun,name='active'),
    path('f',views.ffun,name='f'),
    path('l',views.lifun,name='l'),
    path('account',views.signup,name='account'),
    path('user',views.usfn,name='user'),
    path('change',views.chfn,name='change'),
    path('',views.signupfn,name='index'),

]