from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Comment, Post
from .utils import LoginMixin


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return self.queryset.filter(published_date__lte=timezone.now()).order_by('published_date')

class PostDetail(DetailView):
    model = Post

class PostNew(LoginMixin, CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.id])

class PostEdit(LoginMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.id])

class PostDraftList(LoginMixin, ListView):
    queryset = Post.objects.all()
    template_name = 'blog/post_draft_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return self.queryset.filter(published_date__isnull=True).order_by('created_date')

class PostPublish(LoginMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_object(self):
        post = get_object_or_404(self.model, pk=self.kwargs['pk'])
        post.publish()
        return post

class PostRemove(LoginMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class AddCommentToPost(LoginMixin, CreateView):
    model = Comment
    fields = ['author', 'text']
    template_name = 'blog/add_comment_to_post.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.post.id])

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.get_form()
        return render(request, 'blog/add_comment_to_post.html', {'form': form, 'post': post})

class CommentApprove(LoginMixin, UpdateView):
    model = Comment
    fields = ['approved_comment']
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        form.instance.approved_comment = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.post.id])

class CommentRemove(LoginMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.post.id])
