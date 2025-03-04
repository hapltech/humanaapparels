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
    faq = {
        "title": "Frequently Asked Questions",
        "subtitle": "Get answers to common questions about our services",
        "faqs": FAQ.objects.all(),
    }

    return render(
        request,
        "www/about.html",
        {
            "about": AboutData.objects.first(),
            "management": TeamMember.objects.filter(is_management=True),
            "team": TeamMember.objects.filter(is_management=False),
            "faq": faq,
        },
    )


def customers(request):
    clients_data = {
        "title": "Trusted by Global Fashion Brands",
        "subtitle": "Partnering with industry leaders in sustainable fashion manufacturing",
        "clients": Customer.objects.all(),
    }

    testimonials = {
        "title": "What Our Clients Say",
        "subtitle": "Read what our clients have to say about us",
        "featured": Testimonial.objects.first(),
        "testimonials": Testimonial.objects.all(),
    }

    return render(
        request,
        "www/customers.html",
        {
            "clients_data": clients_data,
            "testimonials": testimonials,
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
            "contact": {
                "office": {
                    "title": contact_data.office_title,
                    "subtitle": contact_data.office_subtitle,
                    "image": contact_data.office_image,
                    "contacts": {
                        "phones": list(
                            filter(None, [contact_data.phone1, contact_data.phone2])
                        ),
                        "whatsapp": list(filter(None, [contact_data.whatsapp])),
                        "emails": list(
                            filter(None, [contact_data.email1, contact_data.email2])
                        ),
                    },
                },
                "groups": contact_groups,
                "socials": socials,
                "map": {
                    "title": contact_data.map_title,
                    "subtitle": contact_data.map_subtitle,
                    "image": contact_data.map_image,
                    "map_url": contact_data.map_url,
                    "address": contact_data.address,
                },
            }
        },
    )


def news(request):
    return render(
        request,
        "www/news.html",
        {
            "news": {
                "title": "Latest News & Updates",
                "subtitle": "Stay informed about our latest developments, achievements, and industry insights",
                "articles": NewsArticle.objects.all(),
            }
        },
    )


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
