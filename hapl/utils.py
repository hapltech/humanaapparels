from faker import Faker


fake = Faker()


def generate_products_data():
    products_data = {
        "carousel": [
            {
                "image": fake.image_url(width=800, height=400),
                "alt": fake.text(max_nb_chars=20),
            }
            for _ in range(3)
        ],
        "sections": [
            {
                "title": fake.sentence(nb_words=4),
                "description": fake.paragraph(nb_sentences=2),
                "image": fake.image_url(width=600, height=400),
            }
            for _ in range(5)
        ],
        "product_portfolio": [
            {
                "section": fake.word().capitalize() + "s",
                "products": [
                    {
                        "gender": fake.random_element(elements=("Male", "Female")),
                        "name": fake.sentence(nb_words=3),
                        "image": fake.image_url(width=300, height=200),
                        "buyer": fake.company(),
                    }
                    for _ in range(10)
                ],
            }
            for _ in range(2)
        ],
    }
    return products_data


def generate_complience_data():
    complience_data = {
        "sections": [
            {
                "title": fake.sentence(nb_words=4),
                "description": fake.paragraph(nb_sentences=2),
                "image": fake.image_url(width=600, height=400),
            }
            for _ in range(2)
        ],
        "certificates": [
            {"name": fake.company(), "image": fake.image_url(width=200, height=100)}
            for _ in range(2)
        ],
    }
    return complience_data


def generate_sustainability_data():
    sustainability_data = {
        "sections": [
            {
                "title": fake.sentence(nb_words=4),
                "description": fake.paragraph(nb_sentences=2),
                "image": fake.image_url(width=600, height=400),
            }
            for _ in range(2)
        ],
        "certificates": [
            {"name": fake.company(), "image": fake.image_url(width=200, height=100)}
            for _ in range(2)
        ],
    }
    return sustainability_data


def generate_gallery_data():
    gallery_data = {
        "images": [
            {
                "caption": fake.sentence(nb_words=3),
                "url": fake.image_url(width=400, height=300),
                "section": fake.word().capitalize(),
            }
            for _ in range(2)
        ],
        "videos": [
            {
                "caption": fake.sentence(nb_words=3),
                "youtube_url": "https://www.youtube.com/embed/your_youtube_video_id",
                "section": fake.word().capitalize(),
            }
            for _ in range(2)
        ],
    }
    return gallery_data
