from django.shortcuts import render


def index(request):
    hero_slides = [
        {
            "image": "https://picsum.photos/1920/1080?random=1",
            "title": "Sustainable Fashion",
            "subtitle": "Eco-friendly manufacturing for a better tomorrow",
            "cta": {"text": "Learn More", "url": "#"},
        },
        {
            "image": "https://picsum.photos/1920/1080?random=2",
            "cta": {"text": "View Collection", "url": "#"},
        },
        {
            "image": "https://picsum.photos/1920/1080?random=3",
            "title": "Quality Craftsmanship",
            "subtitle": "Precision in every stitch",
        },
    ]

    articles = [
        {
            "title": "Sustainable Manufacturing Practices",
            "excerpt": "How we're reducing our environmental impact through innovative production methods.",
            "image": "https://picsum.photos/560/315?random=1",
            "url": "#",
            "author": {
                "name": "John Doe",
                "avatar": "https://picsum.photos/32/32?random=1",
            },
        },
        {
            "title": "New Collection Preview",
            "excerpt": "Get a sneak peek at our upcoming seasonal collection featuring eco-friendly materials.",
            "image": "https://picsum.photos/560/315?random=2",
            "url": "#",
            "author": {
                "name": "Alice Johnson",
                "avatar": "https://picsum.photos/32/32?random=2",
            },
        },
        {
            "title": "Industry Recognition",
            "excerpt": "Humana Apparels receives award for excellence in sustainable manufacturing.",
            "image": "https://picsum.photos/560/315?random=3",
            "url": "#",
            "author": {
                "name": "Jane Smith",
                "avatar": "https://picsum.photos/32/32?random=3",
            },
        },
    ]

    clients = [
        {
            "name": "Fashion Brand 1",
            "logo": "https://picsum.photos/240/80?random=1",
            "url": "#",
        },
        {
            "name": "Fashion Brand 2",
            "logo": "https://picsum.photos/240/80?random=2",
            "url": "#",
        },
        {
            "name": "Fashion Brand 3",
            "logo": "https://picsum.photos/240/80?random=3",
            "url": "#",
        },
        {
            "name": "Fashion Brand 4",
            "logo": "https://picsum.photos/240/80?random=4",
            "url": "#",
        },
        {
            "name": "Fashion Brand 5",
            "logo": "https://picsum.photos/240/80?random=5",
            "url": "#",
        },
        {
            "name": "Fashion Brand 6",
            "logo": "https://picsum.photos/240/80?random=6",
            "url": "#",
        },
        {
            "name": "Fashion Brand 6",
            "logo": "https://picsum.photos/240/80?random=6",
            "url": "#",
        },
        {
            "name": "Fashion Brand 6",
            "logo": "https://picsum.photos/240/80?random=6",
            "url": "#",
        },
        {
            "name": "Fashion Brand 6",
            "logo": "https://picsum.photos/240/80?random=6",
            "url": "#",
        },
        {
            "name": "Fashion Brand 6",
            "logo": "https://picsum.photos/240/80?random=6",
            "url": "#",
        },
    ]

    return render(
        request,
        "www/home/index.html",
        {"hero_slides": hero_slides, "articles": articles, "clients": clients},
    )
