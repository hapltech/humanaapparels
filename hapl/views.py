from django.shortcuts import render
from django.http import Http404
from hapl.models import (
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
    ProductsPage,
    ProductCarouselSlide,
    ProductSection,
    ProductCategory,
    Product,
    CompliancePage,
    ComplianceSection,
    ComplianceCertificate,
    SustainabilityPage,
    SustainabilitySection,
    SustainabilityCertificate,
    GalleryPage,
    GallerySection,
    GalleryImage,
    GalleryVideo,
)


def home(request):
    intro_section = HomeIntroductionSection.objects.first()
    stats_section = HomeStatsSection.objects.first()
    services_section = HomeServicesSection.objects.first()

    return render(
        request,
        "www/home.html",
        {
            "hero": {
                "title": "Welcome to Humana Apparels",
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


def products(request):
    products_page = ProductsPage.objects.first()

    context = {
        "carousel": ProductCarouselSlide.objects.filter(page=products_page),
        "sections": ProductSection.objects.filter(page=products_page),
        "product_portfolio": [],
    }

    # Build the product portfolio structure with pre-processed gender data
    for category in ProductCategory.objects.filter(page=products_page):
        portfolio_item = {
            "section": category.name,
            "has_male": False,
            "has_female": False,
            "has_other": False,
            "male_products": [],
            "female_products": [],
            "other_products": [],
        }

        # Categorize products by gender
        for product in Product.objects.filter(category=category):
            product_data = {
                "name": product.name,
                "image": product.image.url,
                "buyer": product.buyer,
            }

            if product.gender == "Male":
                portfolio_item["has_male"] = True
                portfolio_item["male_products"].append(product_data)
            elif product.gender == "Female":
                portfolio_item["has_female"] = True
                portfolio_item["female_products"].append(product_data)
            else:
                portfolio_item["has_other"] = True
                portfolio_item["other_products"].append(product_data)

        context["product_portfolio"].append(portfolio_item)

    return render(request, "www/products.html", context)


def complience(request):
    compliance_page = CompliancePage.objects.first()

    complience_data = {"sections": [], "certificates": []}

    # Add sections
    for section in ComplianceSection.objects.filter(page=compliance_page):
        complience_data["sections"].append(
            {
                "title": section.title,
                "description": section.description,
                "image": section.image.url,
            }
        )

    # Add certificates
    for certificate in ComplianceCertificate.objects.filter(page=compliance_page):
        complience_data["certificates"].append(
            {"name": certificate.name, "image": certificate.image.url}
        )

    return render(request, "www/complience.html", {"complience_data": complience_data})


def sustainability(request):
    sustainability_page = SustainabilityPage.objects.first()

    sustainability_data = {"sections": [], "certificates": []}

    # Add sections
    for section in SustainabilitySection.objects.filter(page=sustainability_page):
        sustainability_data["sections"].append(
            {
                "title": section.title,
                "description": section.description,
                "image": section.image.url,
            }
        )

    # Add certificates
    for certificate in SustainabilityCertificate.objects.filter(
        page=sustainability_page
    ):
        sustainability_data["certificates"].append(
            {"name": certificate.name, "image": certificate.image.url}
        )

    return render(
        request, "www/sustainability.html", {"sustainability_data": sustainability_data}
    )


def gallery(request):
    gallery_page = GalleryPage.objects.first()

    # Initialize dictionaries to store images and videos by section
    images_by_section = {}
    videos_by_section = {}

    # Organize images by section
    for section in GallerySection.objects.filter(page=gallery_page):
        section_name = section.name

        # Get images for this section
        if section_name not in images_by_section:
            images_by_section[section_name] = []

        for image in GalleryImage.objects.filter(section=section):
            images_by_section[section_name].append(
                {
                    "caption": image.caption,
                    "url": image.image.url,
                    "section": section_name,
                }
            )

        # Get videos for this section
        if section_name not in videos_by_section:
            videos_by_section[section_name] = []

        for video in GalleryVideo.objects.filter(section=section):
            videos_by_section[section_name].append(
                {
                    "caption": video.caption,
                    "youtube_url": video.youtube_url,
                    "section": section_name,
                }
            )

    context = {
        "gallery_data": {
            "images_by_section": images_by_section,
            "videos_by_section": videos_by_section,
        }
    }

    return render(request, "www/gallery.html", context)
