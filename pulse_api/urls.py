from django.contrib import admin
from django.urls import path

from pulse_api.user import views as user_views
from pulse_api.post import views as post_views
from pulse_api.tag import views as tag_views
from pulse_api.comment import views as comment_views

urlpatterns = [
    # admin site currently disabled
    # path("admin/", admin.site.urls),

    # User views
    path('users/<int:user_id>/', user_views.get_user_by_id, name='get_user_by_id'),
    path('users/', user_views.create_user, name='create_user'),
    path('users/<int:user_id>/update/', user_views.update_user, name='update_user'),
    path('users/<int:user_id>/delete/', user_views.delete_user, name='delete_user'),

    # Post views
    path('posts/user/<int:user_id>/', post_views.get_posts_by_user, name='get_posts_by_user'),
    path('posts/tag/<str:tag_name>/', post_views.get_posts_by_tag, name='get_posts_by_tag'),
    path('posts/<int:post_id>/', post_views.get_post_by_id, name='get_post_by_id'),
    path('posts/', post_views.create_post, name='create_post'),
    path('posts/<int:post_id>/update/', post_views.update_post, name='update_post'),
    path('posts/<int:post_id>/delete/', post_views.delete_post, name='delete_post'),

    # Tag views
    path('tags/post/<int:post_id>/', tag_views.get_tags_by_post_id, name='get_tags_by_post_id'),
    path('tags/<str:tag_name>/', tag_views.get_tag_by_name, name='get_tag_by_name'),
    path('tags/', tag_views.create_tag, name='create_tag'),
    path('tags/<int:tag_id>/update/', tag_views.update_tag, name='update_tag'),
    path('tags/<int:tag_id>/delete/', tag_views.delete_tag, name='delete_tag'),

    # Comment views
    path('comments/post/<int:post_id>/', comment_views.get_comments_by_post_id, name='get_comments_by_post_id'),
    path('comments/<int:comment_id>/', comment_views.get_comments_by_comment_id, name='get_comments_by_comment_id'),
    path('comments/', comment_views.create_comment, name='create_comment'),
    path('comments/<int:comment_id>/update/', comment_views.update_comment, name='update_comment'),
    path('comments/<int:comment_id>/delete/', comment_views.delete_comment, name='delete_comment'),
]
