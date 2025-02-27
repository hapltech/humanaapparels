import factory
from faker import Faker
from seeder.utils import cache_image
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
    ContactMember,
    Social,
    CareerPosition,
    NewsArticle,
)


fake = Faker()


class BaseFactory(factory.django.DjangoModelFactory):
    """Abstract base factory with common settings."""

    class Meta:
        abstract = True


class HomeCarouselSlideFactory(BaseFactory):
    class Meta:
        model = HomeCarouselSlide

    title = factory.Faker("sentence", nb_words=5)
    subtitle = factory.Faker("sentence", nb_words=12)
    image = factory.LazyAttribute(lambda x: cache_image(1920, 1080, keyword="apparel"))
    cta_text = factory.Faker("word")
    cta_url = factory.Faker("url")
    is_active = True


class HomeIntroductionFactory(BaseFactory):
    class Meta:
        model = HomeIntroduction

    title = "Crafting Excellence in Apparel Manufacturing"
    subtitle = "We combine traditional craftsmanship with modern technology that meet global standards."
    content = factory.Faker("paragraph", nb_sentences=5)


class FeaturedArticleFactory(BaseFactory):
    class Meta:
        model = FeaturedArticle

    title = factory.Faker("sentence", nb_words=6)
    excerpt = factory.Faker("sentence", nb_words=15)
    image = factory.LazyAttribute(lambda x: cache_image(560, 315, keyword="rmg"))
    article_url = factory.Faker("url")
    published_at = factory.Faker("date_object")
    category = factory.Faker("word")


class FeaturedClientFactory(BaseFactory):
    class Meta:
        model = FeaturedClient

    name = factory.Faker("company")
    logo = factory.LazyAttribute(lambda x: cache_image(240, 80, keyword="logo"))
    url = factory.Faker("url")


class CompanyStatsFactory(BaseFactory):
    class Meta:
        model = CompanyStats

    title = factory.Faker("word")
    value = factory.Faker("numerify", text="##+")
    icon = factory.Faker(
        "random_element",
        elements=[
            "ph-calendar",
            "ph-users",
            "ph-t-shirt",
            "ph-globe",
            "ph-factory",
        ],
    )


class ServiceFactory(BaseFactory):
    class Meta:
        model = Service

    title = factory.Faker("sentence", nb_words=5)
    description = factory.Faker("paragraph", nb_sentences=4)
    icon = factory.Faker(
        "random_element",
        elements=[
            "ph-pen-nib",
            "ph-factory",
            "ph-leaf",
            "ph-truck",
            "ph-gear",
        ],
    )
    image = factory.LazyAttribute(lambda x: cache_image(560, 720, keyword="factory"))


class AboutDataFactory(BaseFactory):
    class Meta:
        model = AboutData

    title = "Our Story"
    subtitle = "From humble beginnings to a global apparel manufacturing leader."
    image = factory.LazyAttribute(lambda x: cache_image(1920, 1080, keyword="factory"))
    content = factory.Faker("paragraph", nb_sentences=8)


class TeamMemberFactory(BaseFactory):
    class Meta:
        model = TeamMember

    name = factory.Faker("name")
    position = factory.Faker("job")
    image = factory.LazyAttribute(lambda x: cache_image(320, 320, keyword="person"))
    is_management = factory.Faker("boolean")


class FAQFactory(BaseFactory):
    class Meta:
        model = FAQ

    question = factory.Faker("sentence", nb_words=8)
    answer = factory.Faker("paragraph", nb_sentences=4)


class CustomerFactory(BaseFactory):
    class Meta:
        model = Customer

    name = factory.Faker("company")
    logo = factory.LazyAttribute(lambda x: cache_image(300, 200, keyword="brand"))
    url = factory.Faker("url")


class TestimonialFactory(BaseFactory):
    class Meta:
        model = Testimonial

    content = factory.Faker("paragraph", nb_sentences=4)
    author = factory.Faker("name")
    position = factory.Faker("job")
    company_logo = factory.LazyAttribute(
        lambda x: cache_image(200, 200, keyword="logo")
    )


class ContactDataFactory(BaseFactory):
    class Meta:
        model = ContactData

    map_title = "Visit Our Headquarters"
    map_subtitle = "Get directions to our main office and manufacturing facility."
    map_image = factory.LazyAttribute(lambda x: cache_image(600, 400, keyword="map"))
    map_url = "https://www.google.com/maps"
    address = factory.Faker("address")
    office_title = "Contact Us"
    office_subtitle = "Reach out to our team for inquiries and support."
    office_image = factory.LazyAttribute(
        lambda x: cache_image(600, 400, keyword="office")
    )
    phone1 = factory.Faker("phone_number")
    email1 = factory.Faker("email")


class ContactGroupFactory(BaseFactory):
    class Meta:
        model = ContactGroup

    name = factory.Faker("word")


class ContactMemberFactory(BaseFactory):
    class Meta:
        model = ContactMember

    group = factory.SubFactory(ContactGroupFactory)
    name = factory.Faker("name")
    position = factory.Faker("job")
    image = factory.LazyAttribute(lambda x: cache_image(320, 320, keyword="person"))
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")


class SocialFactory(BaseFactory):
    class Meta:
        model = Social

    name = factory.Faker("word")
    url = factory.Faker("url")
    icon = factory.Faker(
        "random_element",
        elements=[
            "ph-facebook-logo",
            "ph-instagram-logo",
            "ph-linkedin-logo",
            "ph-twitter-logo",
        ],
    )


class CareerPositionFactory(BaseFactory):
    class Meta:
        model = CareerPosition

    title = factory.Faker("sentence", nb_words=6)
    type = factory.Faker(
        "random_element", elements=["Full-time", "Part-time", "Contract"]
    )
    location = factory.Faker("city")
    department = factory.Faker("word")
    posted_at = factory.Faker("date_object")
    description = factory.Faker("paragraph", nb_sentences=6)
    status = factory.Faker("random_element", elements=["active", "inactive"])


class NewsArticleFactory(BaseFactory):
    class Meta:
        model = NewsArticle

    title = factory.Faker("sentence", nb_words=7)
    excerpt = factory.Faker("sentence", nb_words=16)
    content = factory.Faker("paragraph", nb_sentences=7)
    image = factory.LazyAttribute(lambda x: cache_image(800, 600, keyword="news"))
    published_at = factory.Faker("date_object")
    category = factory.Faker("word")
