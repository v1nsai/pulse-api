from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from pulse_api.comment.views import CommentView
from pulse_api.post.views import PostView
from pulse_api.tag.views import TagView
from pulse_api.user.views import UserView


urlpatterns = [
    # admin site currently disabled
    # path("admin/", admin.site.urls),

    # Login/logout
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),

    # User views
    path("users/<int:user_id>/", UserView.get_user_by_id, name="get_user_by_id"),
    path("users/", UserView.create_user, name="create_user"),
    path('users/<int:user_id>/update/', UserView.update_user, name='update_user'),
    path('users/<int:user_id>/delete/', UserView.delete_user, name='delete_user'),

    # Post views
    path('posts/user/<int:user_id>/', PostView.get_posts_by_user, name='get_posts_by_user'),
    path('posts/tag/<str:tag_name>/', PostView.get_posts_by_tag, name='get_posts_by_tag'),
    path('posts/<int:post_id>/', PostView.get_post_by_id, name='get_post_by_id'),
    path('posts/', PostView.create_post, name='create_post'),
    path('posts/<int:post_id>/update/', PostView.update_post, name='update_post'),
    path('posts/<int:post_id>/delete/', PostView.delete_post, name='delete_post'),

    # Tag views
    path('tags/post/<int:post_id>/', TagView.get_tags_by_post_id, name='get_tags_by_post_id'),
    path('tags/<str:tag_name>/', TagView.get_tag_by_name, name='get_tag_by_name'),
    path('tags/', TagView.create_tag, name='create_tag'),
    path('tags/<int:tag_id>/update/', TagView.update_tag, name='update_tag'),
    path('tags/<int:tag_id>/delete/', TagView.delete_tag, name='delete_tag'),

    # Comment views
    path('comments/post/<int:post_id>/', CommentView.get_comments_by_post_id, name='get_comments_by_post_id'),
    path('comments/<int:comment_id>/', CommentView.get_comments_by_comment_id, name='get_comments_by_comment_id'),
    path('comments/', CommentView.create_comment, name='create_comment'),
    path('comments/<int:comment_id>/update/', CommentView.update_comment, name='update_comment'),
    path('comments/<int:comment_id>/delete/', CommentView.delete_comment, name='delete_comment'),
]
