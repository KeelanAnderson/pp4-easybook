from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Service
from .forms import CreatePostForm, CreateServiceForm
from .forms import UpdateServiceForm, DeleteServiceForm


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


class ManagePostView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'manage_post.html')

    def post(self, request):
        return render(request, 'manage_post.html')


class CreatePostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'
    success_url = 'manage_post/'
    success_message = "%(calculated_field)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


class UpdatePostView(
    UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')
    success_message = 'Post updated successfully'

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = Post.objects.filter(slug=self.kwargs['slug']).first()
        return post.account == self.request.user


class DeletePostView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("home")
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = Post.objects.filter(slug=self.kwargs['slug']).first()
        print(post)
        return post.account == self.request.user


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


class CreateServiceView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Service
    form_class = CreateServiceForm
    template_name = 'create_service_form.html'
    success_url = reverse_lazy('manage_post')
    success_message = 'Service created successfully'

    def form_valid(self, form):
        post = form.cleaned_data['title']
        print(self.request.user)
        if self.request.user != post.account:
            raise Http404("You can't create a service for this post.")
        form.instance.post = post
        return super().form_valid(form)


class UpdateServiceView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Service
    form_class = UpdateServiceForm
    template_name = 'create_service_form.html'
    success_url = reverse_lazy('manage_post')
    success_message = 'Service update successfully'


class DeleteServiceView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Service
    form_class = DeleteServiceForm
    template_name = 'create_service_form.html'
    success_url = reverse_lazy('manage_post')
