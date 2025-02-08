from django.shortcuts import render
from hapl.data.home import (
    HERO_CAROUSEL_SLIDES,
    INTRODUCTION_DATA,
    FEATURED_ARTICLES,
    FEATURED_CLIENTS,
    COMPANY_STATS,
    SERVICES,
)


def index(request):
    return render(
        request,
        "www/home/index.html",
        {
            "hero_slides": HERO_CAROUSEL_SLIDES,
            "articles": FEATURED_ARTICLES,
            "clients": FEATURED_CLIENTS,
            "intro": INTRODUCTION_DATA,
            "stats": COMPANY_STATS,
            "services": SERVICES,
        },
    )
