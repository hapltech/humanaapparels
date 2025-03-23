from faker import Faker
import random

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
                "description": fake.paragraph(nb_sentences=10),
                "image": f"https://picsum.photos/seed/{fake.lexify(text='???????????')}/600/400",
            }
            for _ in range(5)
        ],
        "certificates": [
            {
                "name": fake.company(),
                "image": f"https://picsum.photos/seed/{fake.lexify(text='???????????')}/200",
            }
            for _ in range(10)
        ],
    }
    return complience_data


def generate_sustainability_data():
    sustainability_data = {
        "sections": [
            {
                "title": fake.sentence(nb_words=4),
                "description": fake.paragraph(nb_sentences=10),
                "image": f"https://picsum.photos/seed/{fake.lexify(text='???????????')}/600/400",
            }
            for _ in range(5)
        ],
        "certificates": [
            {
                "name": fake.company(),
                "image": f"https://picsum.photos/seed/{fake.lexify(text='???????????')}/200",
            }
            for _ in range(10)
        ],
    }
    return sustainability_data


def generate_gallery_data():
    gallery_data = {
        "images": [
            {
                "caption": fake.sentence(nb_words=3),
                "url": f"https://picsum.photos/seed/{fake.lexify(text='???????????')}/{random.randint(400, 800)}/{random.randint(300, 600)}",
                "section": fake.random_element(
                    elements=("Product", "Culture", "Team", "Events")
                ),
            }
            for _ in range(20)
        ],
        "videos": [
            {
                "caption": fake.sentence(nb_words=3),
                "youtube_url": f"https://www.youtube.com/embed/{fake.lexify(text='???????????')}",
                "section": fake.random_element(
                    elements=("Product", "Culture", "Team", "Events")
                ),
            }
            for _ in range(5)
        ],
    }
    return gallery_data
