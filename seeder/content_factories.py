import factory
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


class BaseFactory(factory.django.DjangoModelFactory):
    """Abstract base factory with common settings."""

    class Meta:
        abstract = True


class HomeCarouselSlideFactory(BaseFactory):
    class Meta:
        model = HomeCarouselSlide

    title = factory.Faker("sentence", nb_words=4)
    subtitle = factory.Faker("sentence", nb_words=10)
    image = factory.LazyAttribute(lambda x: cache_image(1920, 1080))
    cta_text = factory.Faker("word")
    cta_url = factory.Faker("url")
    is_active = True


class HomeIntroductionFactory(BaseFactory):
    class Meta:
        model = HomeIntroduction

    title = factory.Faker("sentence", nb_words=4)
    subtitle = factory.Faker("sentence", nb_words=10)
    content = factory.Faker("paragraph", nb_sentences=5)


class FeaturedArticleFactory(BaseFactory):
    class Meta:
        model = FeaturedArticle

    title = factory.Faker("sentence", nb_words=4)
    excerpt = factory.Faker("sentence", nb_words=10)
    image = factory.LazyAttribute(lambda x: cache_image(560, 315))
    article_url = factory.Faker("url")
    published_at = factory.Faker("date_object")
    category = factory.Faker("word")


class FeaturedClientFactory(BaseFactory):
    class Meta:
        model = FeaturedClient

    name = factory.Faker("company")
    logo = factory.LazyAttribute(lambda x: cache_image(240, 80))
    url = factory.Faker("url")


class CompanyStatsFactory(BaseFactory):
    class Meta:
        model = CompanyStats

    title = factory.Faker("word")
    value = factory.Faker("numerify", text="##+")
    icon = factory.Faker("word")


class ServiceFactory(BaseFactory):
    class Meta:
        model = Service

    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("paragraph", nb_sentences=3)
    icon = factory.Faker("word")
    image = factory.LazyAttribute(lambda x: cache_image(560, 720))


class AboutDataFactory(BaseFactory):
    class Meta:
        model = AboutData

    title = factory.Faker("sentence", nb_words=4)
    subtitle = factory.Faker("sentence", nb_words=10)
    image = factory.LazyAttribute(lambda x: cache_image(1920, 1080))
    content = factory.Faker("paragraph", nb_sentences=5)


class TeamMemberFactory(BaseFactory):
    class Meta:
        model = TeamMember

    name = factory.Faker("name")
    position = factory.Faker("job")
    image = factory.LazyAttribute(lambda x: cache_image(320, 320))
    is_management = factory.Faker("boolean")


class FAQFactory(BaseFactory):
    class Meta:
        model = FAQ

    question = factory.Faker("sentence", nb_words=6)
    answer = factory.Faker("paragraph", nb_sentences=3)


class CustomerFactory(BaseFactory):
    class Meta:
        model = Customer

    name = factory.Faker("company")
    logo = factory.LazyAttribute(lambda x: cache_image(300, 200))
    url = factory.Faker("url")


class TestimonialFactory(BaseFactory):
    class Meta:
        model = Testimonial

    content = factory.Faker("paragraph", nb_sentences=3)
    author = factory.Faker("name")
    position = factory.Faker("job")
    company_logo = factory.LazyAttribute(lambda x: cache_image(200, 200))


class ContactDataFactory(BaseFactory):
    class Meta:
        model = ContactData

    map_title = factory.Faker("sentence", nb_words=4)
    map_subtitle = factory.Faker("sentence", nb_words=10)
    map_image = factory.LazyAttribute(lambda x: cache_image(600, 400, keyword="map"))
    map_url = factory.Faker("url")
    address = factory.Faker("address")
    office_title = factory.Faker("sentence", nb_words=4)
    office_subtitle = factory.Faker("sentence", nb_words=10)
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
    image = factory.LazyAttribute(lambda x: cache_image(320, 320))
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")


class SocialFactory(BaseFactory):
    class Meta:
        model = Social

    name = factory.Faker("word")
    url = factory.Faker("url")
    icon = factory.Faker("word")


class CareerPositionFactory(BaseFactory):
    class Meta:
        model = CareerPosition

    title = factory.Faker("sentence", nb_words=4)
    type = factory.Faker("word")
    location = factory.Faker("city")
    department = factory.Faker("word")
    posted_at = factory.Faker("date_object")
    description = factory.Faker("paragraph", nb_sentences=5)
    status = factory.Faker("random_element", elements=["active", "inactive"])


class NewsArticleFactory(BaseFactory):
    class Meta:
        model = NewsArticle

    title = factory.Faker("sentence", nb_words=4)
    excerpt = factory.Faker("sentence", nb_words=10)
    content = factory.Faker("paragraph", nb_sentences=5)
    image = factory.LazyAttribute(lambda x: cache_image(800, 600))
    published_at = factory.Faker("date_object")
    category = factory.Faker("word")
