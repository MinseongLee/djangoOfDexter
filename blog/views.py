from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Comment, Post


class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return self.queryset.filter(published_date__lte=timezone.now()).order_by('published_date')

class PostDetail(DetailView):
    model = Post

class PostNew(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.id})

class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.id])

class PostDraftList(LoginRequiredMixin, ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'blog/post_draft_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return self.queryset.filter(published_date__isnull=True).order_by('created_date')

class PostPublish(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_object(self):
        post = get_object_or_404(self.model, pk=self.kwargs['pk'])
        post.publish()
        return post

class PostRemove(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class AddCommentToPost(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['author', 'text']
    template_name = 'blog/add_comment_to_post.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.post.id])

class CommentApprove(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['approved_comment']
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        form.instance.approved_comment = True
        form.instance.post.plus_approved_comment_cnt()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.post.id])

class CommentRemove(LoginRequiredMixin, DeleteView):
    model = Comment

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.object.approved_comment:
            self.object.post.minus_approved_comment_cnt()
        self.object.delete()
        return HttpResponseRedirect(success_url)


    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.post.id])
