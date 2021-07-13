from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trails/', views.TrailList.as_view(), name='index'),
    path('trails/<int:trail_id>/', views.trails_detail, name='detail'),
    path('trails/create/', views.TrailCreate.as_view(), name='trails_create'),
    path('trails/<int:pk>/update/', views.TrailUpdate.as_view(), name='trails_update'),
    path('trails/<int:pk>/delete/', views.TrailDelete.as_view(), name='trails_delete'),
    path('trails/<int:trail_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    path('trails/<int:trail_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='comments_delete'),
    # path('trails/<int:trail_id>/add_amenity/', views.add_amenity, name='add_amenity'),

    path('accounts/signup/', views.signup, name='signup'),

]