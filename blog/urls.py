from django.urls import path
from blog import views
from blog import user_login_view
from django.urls import reverse
from django.contrib.auth.decorators import login_required

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="main"),
    path("create-post/", views.create_post, name="create-post"),
    path("create-place-to-visit/", views.create_place_to_visit, name="create-place-to-visit"),
    path("upload-image/", views.upload_image, name="upload-image"),
    path("edit-post/<int:post_id>", views.edit_post, name="edit"),
    path("post/<int:post_id>", views.load_post, name="post"),   
    path("login/", user_login_view.user_login, name='login'),
    path("logout/", user_login_view.user_logout, name='logout'),
    path("auth/", user_login_view.authentication, name='auth'),

]


