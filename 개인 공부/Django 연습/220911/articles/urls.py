from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('<int:pk>/detail/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/update/',views.update,name='update'),
]
