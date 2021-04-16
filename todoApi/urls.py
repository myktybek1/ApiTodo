from django.urls import path, include
from todoApi.views import *

urlpatterns =  [
    path('', postview, name='postview'),
    path('post-list/', PostsListView.as_view()),
    path('post-detail/<int:pk>', PostsDetailView.as_view()),
    path('post-create/', PostsCreateView.as_view()),
    path('post-update/<int:pk>', PostsUpdateView.as_view()),
    path('post-delete/<int:pk>', PostsDeleteView.as_view()),

]
