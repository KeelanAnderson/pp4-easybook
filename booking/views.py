from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Service, Booking


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        service_queryset = Service.objects.filter(business_owner_id=post.id)
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
    queryset = Booking.objects.order_by("booking_time")
    template_name = "booking.html"
    paginate_by = 12
