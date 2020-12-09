from django.urls import path
from blog import views

urlpatterns=[
    path('about/',views.about,name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('addpost/',views.Addpost,name='add'),
    path('updatepost/<int:id>/',views.updatepost,name='update'),
    path('delete/<int:id>/',views.delete_post,name='delete'),
    path('logout/',views.user_logout,name='logout'),
]
