from django.shortcuts import render
from hapl.data.about import ABOUT_DATA, TEAM_DATA, FAQ_DATA
from hapl.data.customers import ALL_CLIENTS, TESTIMONIALS
from hapl.data.contact import CONTACT_DATA
from hapl.data.career import CAREER_DATA
from hapl.data.news import NEWS_DATA
from django.http import Http404
from hapl.data.home import (
    HERO_CAROUSEL_SLIDES,
    INTRODUCTION_DATA,
    FEATURED_ARTICLES,
    FEATURED_CLIENTS,
    COMPANY_STATS,
    SERVICES,
)


def home(request):
    return render(
        request,
        "www/home.html",
        {
            "hero_slides": HERO_CAROUSEL_SLIDES,
            "articles": FEATURED_ARTICLES,
            "clients": FEATURED_CLIENTS,
            "intro": INTRODUCTION_DATA,
            "stats": COMPANY_STATS,
            "services": SERVICES,
        },
    )


def about(request):
    return render(
        request,
        "www/about.html",
        {
            "about": ABOUT_DATA,
            "management": TEAM_DATA["management"],
            "team": TEAM_DATA["team"],
            "faq": FAQ_DATA,
        },
    )


def customers(request):
    return render(
        request,
        "www/customers.html",
        {
            "clients_data": ALL_CLIENTS,
            "testimonials": TESTIMONIALS,
        },
    )


def contact(request):
    return render(
        request,
        "www/contact.html",
        {
            "contact": CONTACT_DATA,
        },
    )


def news(request):
    return render(request, "www/news.html", {"news": NEWS_DATA})


def article(request, article_id):
    article = next(
        (article for article in NEWS_DATA["articles"] if article["id"] == article_id),
        None,
    )
    if not article:
        raise Http404("Article not found")

    # Get recent articles excluding current one
    recent_articles = [a for a in NEWS_DATA["articles"] if a["id"] != article_id][:3]

    return render(
        request,
        "www/article.html",
        {"article": article, "recent_articles": recent_articles},
    )


def career(request):
    active_positions = [p for p in CAREER_DATA["positions"] if p["status"] == "active"]
    return render(
        request,
        "www/career.html",
        {"career": CAREER_DATA, "positions": active_positions},
    )
