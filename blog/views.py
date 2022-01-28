from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import View

from .forms import CommentForm, PostForm
from .models import Comment, Post


class PostList(ListView):
    def get(self, request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request,'blog/post_list.html', {'posts': posts})

class PostDetail(DetailView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

class PostNew(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = '/'
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request):
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('post_detail', pk=post.pk)

class PostEdit(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = '/'
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request):
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('post_detail', pk=post.pk)

class PostDraftList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/'
    def get(self, request):
        posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
        return render(request, 'blog/post_draft_list.html', {'posts': posts})

class PostPublish(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/'
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.publish()
        return redirect('post_detail', pk=pk)

class PostRemove(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/'
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post_list')

class AddCommentToPost(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = '/'
    form_class = CommentForm
    template_name = 'blog/add_comment_to_post.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.get_form()
        return render(request, 'blog/add_comment_to_post.html', {'form': form, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, post)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, post):
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post_detail', pk=post.pk)

class CommentApprove(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/'
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.approve()
        return redirect('post_detail', pk=comment.post.pk)
    
class CommentRemove(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/'
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return redirect('post_detail', pk=comment.post.pk)
