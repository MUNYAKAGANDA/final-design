from django.urls import path
from . import views

app_name='app'
urlpatterns=[

   path('/login',views.login,name='login'),
   path('/register',views.register,name='register'),
   # path('article/create',views.AddArticleView.as_view(),name='addarticleview'),
   # path('article/detail/<int:pk>',views.ArticleDetailView.as_view(),name='article_detail'),
   # path('article/delete/<int:pk>',views.ArticleDeleteView.as_view(),name='article_delete'),







]
