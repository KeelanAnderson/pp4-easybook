from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, DetailView, UpdateView, FormView
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


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
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


class CreatePostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')
    success_message = 'Post created successfully'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


# class BusinessActionMixin:

#     fields = ['title', 'slug', 'profession', 'about', 'display_services', 'city', 'location', 'featured_image', 'carousel_image', 'phone_number', 'email', 'status']

#     @property
#     def success_msg(self):
#         return NotImplemented

#     def form_valid(self, form):
#         messages.info(self.request, self.success_msg)
#         return super().form_valid(form)

    # def form_valid(self, form):
    #     return super().form_valid(form)


# class BusinessFormUpdateView(LoginRequiredMixin, BusinessActionMixin, UpdateView):
#     model = Post
#     form_class = BusinessForUpdate
#     template_name = 'update_post.html'
#     fields = ['title', 'slug', 'profession', 'about', 'display_services', 'city', 'location', 'featured_image', 'carousel_image', 'phone_number', 'email', 'status']
#     success_msg = 'Business page Updated'


# class BusinessFormDetailView(DetailView):
#     model = Post


class BookingList(generic.ListView):
    model = Booking
    template_name = "booking.html"
    paginate_by = 12
    context_object_name = 'booking_list'
