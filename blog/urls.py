from django.urls import path

from .views import (AddCommentToPost, CommentApprove, CommentRemove, PostDetail,
                    PostDraftList, PostEdit, PostList, PostNew, PostPublish, PostRemove)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('drafts/', PostDraftList.as_view(), name='post_draft_list'),
    path('post/<int:pk>/publish/', PostPublish.as_view(), name='post_publish'),
    path('post/<int:pk>/remove/', PostRemove.as_view(), name='post_remove'),
    path('post/<int:pk>/comment/', AddCommentToPost.as_view(), name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', CommentApprove.as_view(), name='comment_approve'),
    path('comment/<int:pk>/remove/', CommentRemove.as_view(), name='comment_remove'),
]
