from django.shortcuts import render
from django.http import Http404
from hapl.models import (
    HomeCarouselSlide,
    HomeIntroduction,
    FeaturedArticle,
    FeaturedClient,
    CompanyStats,
    Service,
    AboutData,
    TeamMember,
    FAQ,
    Customer,
    Testimonial,
    ContactData,
    ContactGroup,
    CareerPosition,
    NewsArticle,
    Social,
)


def home(request):
    return render(
        request,
        "www/home.html",
        {
            "hero_slides": HomeCarouselSlide.objects.filter(is_active=True),
            "articles": FeaturedArticle.objects.all(),
            "clients": FeaturedClient.objects.all(),
            "intro": HomeIntroduction.objects.first(),
            "stats": CompanyStats.objects.all(),
            "services": Service.objects.all(),
        },
    )


def about(request):
    return render(
        request,
        "www/about.html",
        {
            "about": AboutData.objects.first(),
            "management": TeamMember.objects.filter(is_management=True),
            "team": TeamMember.objects.filter(is_management=False),
            "faq": FAQ.objects.all(),
        },
    )


def customers(request):
    return render(
        request,
        "www/customers.html",
        {
            "clients_data": Customer.objects.all(),
            "testimonials": Testimonial.objects.all(),
        },
    )


def contact(request):
    contact_data = ContactData.objects.first()
    contact_groups = ContactGroup.objects.all()
    socials = Social.objects.all()

    return render(
        request,
        "www/contact.html",
        {
            "contact": contact_data,
            "contact_groups": contact_groups,
            "socials": socials,
        },
    )


def news(request):
    return render(request, "www/news.html", {"news": NewsArticle.objects.all()})


def article(request, article_id):
    try:
        article = NewsArticle.objects.get(pk=article_id)
    except NewsArticle.DoesNotExist:
        raise Http404("Article not found")

    recent_articles = NewsArticle.objects.exclude(pk=article_id).order_by(
        "-published_at"
    )[:3]

    return render(
        request,
        "www/article.html",
        {"article": article, "recent_articles": recent_articles},
    )


def career(request):
    active_positions = CareerPosition.objects.filter(status="active")
    return render(
        request,
        "www/career.html",
        {"positions": active_positions},
    )
