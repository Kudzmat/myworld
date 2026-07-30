# https://youtu.be/0oSsLbh_Kv4?si=hV8dC98-Mt7oZGm7 LINK TO TEMPLATE
from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate,
    Highlight,
    WorkSection,
)

from django.views import generic

from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        #certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        category_order = [category for category, _ in Highlight.CATEGORY_CHOICES]
        highlights = sorted(Highlight.objects.all(), key=lambda h: category_order.index(h.category))

        context["testimonials"] = testimonials
        #context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        context["highlights"] = highlights
        return context


class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio-detail.html"


class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"


class WorkView(generic.TemplateView):
    template_name = "main/work.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sections"] = WorkSection.objects.filter(is_active=True).prefetch_related("talks")
        return context