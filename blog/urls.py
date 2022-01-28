from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEdit.as_view(), name='post_edit'),
    re_path(r'^drafts/$', views.PostDraftList.as_view(), name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.PostPublish.as_view(), name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.PostRemove.as_view(), name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.AddCommentToPost.as_view(), name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.CommentApprove.as_view(), name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.CommentRemove.as_view(), name='comment_remove'),
]
