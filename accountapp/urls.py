from django.urls import path

from accountapp.views import user_login, user_logout, user_signup, user_delete

urlpatterns = [
    path('login/',user_login, name='user_login'),
    path('logout/',user_logout, name='user_logout'),
    path('signup/',user_signup, name='user_signup'),
    path('logout/',user_delete, name='user_delete'),

]