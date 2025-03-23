from django.shortcuts import render
from django.http import Http404
from hapl.models import (
    HomeHeroSection,
    HomeCarouselSlide,
    HomeIntroductionSection,
    HomeIntroductionFeature,
    HomeServicesSection,
    Service,
    HomeStatsSection,
    CompanyStats,
    AboutSection,
    TeamSection,
    TeamMember,
    FAQSection,
    FAQ,
    CustomersSection,
    Customer,
    TestimonialsSection,
    Testimonial,
    ContactSection,
    ContactData,
    ContactPhone,
    ContactEmail,
    ContactGroup,
    CareerSection,
    CareerPosition,
    NewsSection,
    NewsArticle,
    Social,
)


def home(request):
    hero_section = HomeHeroSection.objects.first()
    intro_section = HomeIntroductionSection.objects.first()
    stats_section = HomeStatsSection.objects.first()
    services_section = HomeServicesSection.objects.first()

    return render(
        request,
        "www/home.html",
        {
            "hero": {
                "title": (
                    hero_section.title if hero_section else "Welcome to Humana Apparels"
                ),
                "subtitle": hero_section.subtitle if hero_section else None,
                "slides": HomeCarouselSlide.objects.filter(is_active=True),
            },
            "articles": NewsArticle.objects.filter(is_featured=True),
            "clients": Customer.objects.filter(is_featured=True),
            "intro": intro_section,
            "intro_features": (
                HomeIntroductionFeature.objects.filter(introduction=intro_section)
                if intro_section
                else []
            ),
            "stats": {
                "title": (
                    stats_section.title if stats_section else "Our Impact in Numbers"
                ),
                "subtitle": stats_section.subtitle if stats_section else None,
                "items": CompanyStats.objects.all(),
            },
            "services": {
                "title": services_section.title if services_section else "Our Services",
                "subtitle": services_section.subtitle if services_section else None,
                "items": Service.objects.all(),
            },
        },
    )


def about(request):
    about_section = AboutSection.objects.first()
    team_section = TeamSection.objects.first()
    faq_section = FAQSection.objects.first()

    return render(
        request,
        "www/about.html",
        {
            "about": about_section,
            "team": {
                "title": team_section.title if team_section else "Our Team",
                "subtitle": team_section.subtitle if team_section else None,
                "management": TeamMember.objects.filter(is_management=True),
                "staff": TeamMember.objects.filter(is_management=False),
            },
            "faq": {
                "title": (
                    faq_section.title if faq_section else "Frequently Asked Questions"
                ),
                "subtitle": (
                    faq_section.subtitle
                    if faq_section
                    else "Get answers to common questions about our services"
                ),
                "faqs": FAQ.objects.all(),
            },
        },
    )


def customers(request):
    customers_section = CustomersSection.objects.first()
    testimonials_section = TestimonialsSection.objects.first()

    featured_testimonial = (
        Testimonial.objects.filter(is_featured=True).first()
        or Testimonial.objects.first()
    )

    return render(
        request,
        "www/customers.html",
        {
            "clients_data": {
                "title": (
                    customers_section.title
                    if customers_section
                    else "Trusted by Global Fashion Brands"
                ),
                "subtitle": (
                    customers_section.subtitle
                    if customers_section
                    else "Partnering with industry leaders in sustainable fashion manufacturing"
                ),
                "clients": Customer.objects.all(),
            },
            "testimonials": {
                "title": (
                    testimonials_section.title
                    if testimonials_section
                    else "What Our Clients Say"
                ),
                "subtitle": (
                    testimonials_section.subtitle
                    if testimonials_section
                    else "Read what our clients have to say about us"
                ),
                "featured": featured_testimonial,
                "testimonials": Testimonial.objects.all(),
            },
        },
    )


def contact(request):
    contact_section = ContactSection.objects.first()
    contact_data = ContactData.objects.first()
    contact_groups = ContactGroup.objects.all()
    socials = Social.objects.all()

    phones = {"phone": [], "whatsapp": []}

    if contact_data:
        for phone in ContactPhone.objects.filter(contact=contact_data):
            phones[phone.type].append(phone.number)

    emails = []
    if contact_data:
        emails = [
            email.email for email in ContactEmail.objects.filter(contact=contact_data)
        ]

    return render(
        request,
        "www/contact.html",
        {
            "contact": {
                "title": contact_section.title if contact_section else "Contact Us",
                "subtitle": (
                    contact_section.subtitle
                    if contact_section
                    else "Get in touch with our team"
                ),
                "office": {
                    "title": (
                        contact_data.office_title if contact_data else "Our Office"
                    ),
                    "subtitle": contact_data.office_subtitle if contact_data else None,
                    "image": contact_data.office_image if contact_data else None,
                    "contacts": {
                        "phones": phones["phone"],
                        "whatsapp": phones["whatsapp"],
                        "emails": emails,
                        "fax": contact_data.fax if contact_data else None,
                    },
                },
                "groups": contact_groups,
                "socials": socials,
                "map": {
                    "title": contact_data.map_title if contact_data else "Find Us",
                    "subtitle": contact_data.map_subtitle if contact_data else None,
                    "image": contact_data.map_image if contact_data else None,
                    "map_url": contact_data.map_url if contact_data else None,
                    "address": contact_data.address if contact_data else None,
                },
            }
        },
    )


def news(request):
    news_section = NewsSection.objects.first()

    return render(
        request,
        "www/news.html",
        {
            "news": {
                "title": (
                    news_section.title if news_section else "Latest News & Updates"
                ),
                "subtitle": (
                    news_section.subtitle
                    if news_section
                    else "Stay informed about our latest developments, achievements, and industry insights"
                ),
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
    career_section = CareerSection.objects.first()
    active_positions = CareerPosition.objects.filter(status="active")

    return render(
        request,
        "www/career.html",
        {
            "career": {
                "title": (
                    career_section.title if career_section else "Career Opportunities"
                ),
                "subtitle": (
                    career_section.subtitle
                    if career_section
                    else "Join our team and grow with us"
                ),
                "positions": active_positions,
            }
        },
    )


# TODO: Use actual data instead of mock data
from hapl.utils import (
    generate_products_data,
    generate_complience_data,
    generate_sustainability_data,
    generate_gallery_data,
)


def products(request):
    products_data = generate_products_data()
    return render(request, "www/products.html", products_data)


def complience(request):
    complience_data = generate_complience_data()
    return render(request, "www/complience.html", complience_data)


def sustainability(request):
    sustainability_data = generate_sustainability_data()
    return render(request, "www/sustainability.html", sustainability_data)


def gallery(request):
    gallery_data = generate_gallery_data()

    images_by_section = {}
    for image in gallery_data["images"]:
        section = image["section"]
        if section not in images_by_section:
            images_by_section[section] = []
        images_by_section[section].append(image)

    videos_by_section = {}
    for video in gallery_data["videos"]:
        section = video["section"]
        if section not in videos_by_section:
            videos_by_section[section] = []
        videos_by_section[section].append(video)

    context = {
        "gallery_data": {
            "images_by_section": images_by_section,
            "videos_by_section": videos_by_section,
        }
    }

    return render(request, "www/gallery.html", context)
