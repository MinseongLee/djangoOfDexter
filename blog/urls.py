from django.urls import include, path, re_path

from .views import (AddCommentToPost, CommentApprove, CommentRemove, PostDetail,
                    PostDraftList, PostEdit, PostList, PostNew, PostPublish, PostRemove)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    re_path(r'^drafts/$', PostDraftList.as_view(), name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', PostPublish.as_view(), name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', PostRemove.as_view(), name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', AddCommentToPost.as_view(), name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', CommentApprove.as_view(), name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', CommentRemove.as_view(), name='comment_remove'),
]
