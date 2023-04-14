from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Service, Booking
from .forms import CreatePostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("created_on")
    template_name = "index.html"
    paginate_by = 6
    context_object_name = "post_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=1).order_by("-created_on")
        return queryset


def manage_post(request):
    return render(request, 'manage_post.html')


class CreatePostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')
    success_message = 'Post created successfully'

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


class UpdatePostView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')
    success_message = 'Post updated successfully'

    def form_valid(self, form):
        form.instance.account = self.request.user
        form.save()
        return super().form_valid(form)

    def test_func(self):
        post = Post.objects.filter(slug=self.kwargs['slug']).first()
        return post.account == self.request.user


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy("home")
    template_name = 'create_post.html'


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        if not slug:
            return redirect('home')
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        service_queryset = Service.objects.filter(title_id=post.id)
        services = service_queryset.all()

        return render(
            request,
            "post_detail.html",
            {
                'post': post,
                'services': services,

            },
        )


class BookingList(generic.ListView):
    model = Booking
    template_name = "booking.html"
    paginate_by = 12
    context_object_name = 'booking_list'
