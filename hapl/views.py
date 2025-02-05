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
    return render(request, "www/home/index.html", {"hero_slides": hero_slides})
