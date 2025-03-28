from django.urls import path
from . import views


app_name = 'content_api'


urlpatterns = [
    path('blogs/',views.get_blog_list,name='blog_list'),
    # path('blogs/<int:id>/',views.get_blog_by_id,name='blog-detail'),
    path('blogs/create/',views.create_blog,name='blog-create'),
    path('blogs/<int:id>/update/',views.update_blog,name='blog-update'),
    path('blogs/<int:id>/delete/',views.delete_blog,name='blog-delete'),

    path('showrooms/',views.get_showroom_list,name='showroom_list'),
    # path('showrooms/<int:id>/',views.get_showroom_by_id,name='showroom-detail'),
    path('showrooms/create/',views.create_showroom,name='showroom-create'),
    path('showrooms/<int:id>/update/',views.update_showroom,name='showroom-update'),
    path('showrooms/<int:id>/delete/',views.delete_showroom,name='showroom-delete'),

]