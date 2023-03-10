from django.urls import path
from . import views

urlpatterns= [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),


    path('', views.home, name="home"),
    path('room/<str:room_id>/', views.room, name="room"),
    path('profile/<str:user_id>/', views.userProfile, name="user-profile"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:room_id>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:room_id>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:message_id>/', views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activities/', views.activitiesPage, name="activities")




]