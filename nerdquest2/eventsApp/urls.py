from django.urls import path
from . import views

urlpatterns = [
    path('', views.enter),
    path('index', views.index),
    path('register', views.register),

    path('login', views.login),
    path('logout', views.logout),

    path('welcome', views.welcome),
    path('new', views.new_game),
    path('create', views.create_game),
    path('games', views.games),
    path('games/<int:id>', views.one_game),
    path('yours', views.your_games),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
     
    path('join/<int:id>', views.join_game),
    path('leave/<int:id>', views.leave_game),
    path('games/delete/<int:id>', views.delete),
    path('<url>', views.catchall),
]


