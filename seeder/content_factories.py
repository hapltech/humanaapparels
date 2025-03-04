import factory
from faker import Faker
from seeder.utils import cache_image
from hapl.models import (
    HomeHeroSection,
    HomeIntroductionSection,
    HomeServicesSection,
    HomeStatsSection,
    AboutSection,
    TeamSection,
    FAQSection,
    CustomersSection,
    TestimonialsSection,
    ContactSection,
    CareerSection,
    NewsSection,
    HomeCarouselSlide,
    HomeIntroductionFeature,
    Service,
    CompanyStats,
    TeamMember,
    FAQ,
    Customer,
    Testimonial,
    ContactData,
    ContactPhone,
    ContactEmail,
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


# --- Section Factories ---


class BaseSectionFactory(BaseFactory):
    """Base factory for section models"""

    title = factory.Faker("sentence", nb_words=5)
    subtitle = factory.Faker("sentence", nb_words=12)

    class Meta:
        abstract = True


class HomeHeroSectionFactory(BaseSectionFactory):
    class Meta:
        model = HomeHeroSection

    title = "Welcome to Humana Apparels"
    subtitle = "Excellence in Sustainable Apparel Manufacturing"


class HomeIntroductionSectionFactory(BaseSectionFactory):
    class Meta:
        model = HomeIntroductionSection

    title = "Crafting Excellence in Apparel Manufacturing"
    subtitle = "We combine traditional craftsmanship with modern technology that meet global standards."
    content = factory.Faker("paragraph", nb_sentences=5)
    image = factory.LazyAttribute(lambda x: cache_image(1920, 1080, keyword="factory"))


class HomeServicesSectionFactory(BaseSectionFactory):
    class Meta:
        model = HomeServicesSection

    title = "Our Services"
    subtitle = "Comprehensive apparel manufacturing solutions tailored to your needs"


class HomeStatsSectionFactory(BaseSectionFactory):
    class Meta:
        model = HomeStatsSection

    title = "Our Impact in Numbers"
    subtitle = "Key metrics that showcase our growth and success"


class AboutSectionFactory(BaseSectionFactory):
    class Meta:
        model = AboutSection

    title = "Our Story"
    subtitle = "From humble beginnings to a global apparel manufacturing leader."
    content = factory.Faker("paragraph", nb_sentences=8)
    image = factory.LazyAttribute(lambda x: cache_image(1920, 1080, keyword="factory"))


class TeamSectionFactory(BaseSectionFactory):
    class Meta:
        model = TeamSection

    title = "Our Team"
    subtitle = "Meet the experts behind our success"


class FAQSectionFactory(BaseSectionFactory):
    class Meta:
        model = FAQSection

    title = "Frequently Asked Questions"
    subtitle = "Get answers to common questions about our services"


class CustomersSectionFactory(BaseSectionFactory):
    class Meta:
        model = CustomersSection

    title = "Trusted by Global Fashion Brands"
    subtitle = "Partnering with industry leaders in sustainable fashion manufacturing"


class TestimonialsSectionFactory(BaseSectionFactory):
    class Meta:
        model = TestimonialsSection

    title = "What Our Clients Say"
    subtitle = "Read what our clients have to say about us"


class ContactSectionFactory(BaseSectionFactory):
    class Meta:
        model = ContactSection

    title = "Contact Us"
    subtitle = "Get in touch with our team"


class CareerSectionFactory(BaseSectionFactory):
    class Meta:
        model = CareerSection

    title = "Career Opportunities"
    subtitle = "Join our team and grow with us"


class NewsSectionFactory(BaseSectionFactory):
    class Meta:
        model = NewsSection

    title = "Latest News & Updates"
    subtitle = "Stay informed about our latest developments, achievements, and industry insights"


# --- Content Factories ---


class HomeCarouselSlideFactory(BaseFactory):
    class Meta:
        model = HomeCarouselSlide

    section = factory.SubFactory(HomeHeroSectionFactory)
    title = factory.Faker("sentence", nb_words=5)
    subtitle = factory.Faker("sentence", nb_words=12)
    image = factory.LazyAttribute(lambda x: cache_image(1920, 1080, keyword="apparel"))
    cta_text = factory.Faker("word")
    cta_url = factory.Faker("url")
    is_active = True


class HomeIntroductionFeatureFactory(BaseFactory):
    class Meta:
        model = HomeIntroductionFeature

    introduction = factory.SubFactory(HomeIntroductionSectionFactory)
    icon = factory.Faker(
        "random_element",
        elements=[
            "ph-check-circle",
            "ph-rocket",
            "ph-star",
        ],
    )
    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("paragraph", nb_sentences=2)


class ServiceFactory(BaseFactory):
    class Meta:
        model = Service

    section = factory.SubFactory(HomeServicesSectionFactory)
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


class CompanyStatsFactory(BaseFactory):
    class Meta:
        model = CompanyStats

    section = factory.SubFactory(HomeStatsSectionFactory)
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


class TeamMemberFactory(BaseFactory):
    class Meta:
        model = TeamMember

    section = factory.SubFactory(TeamSectionFactory)
    name = factory.Faker("name")
    position = factory.Faker("job")
    image = factory.LazyAttribute(lambda x: cache_image(320, 320, keyword="person"))
    is_management = factory.Faker("boolean")


class FAQFactory(BaseFactory):
    class Meta:
        model = FAQ

    section = factory.SubFactory(FAQSectionFactory)
    question = factory.Faker("sentence", nb_words=8)
    answer = factory.Faker("paragraph", nb_sentences=4)


class CustomerFactory(BaseFactory):
    class Meta:
        model = Customer

    section = factory.SubFactory(CustomersSectionFactory)
    name = factory.Faker("company")
    logo = factory.LazyAttribute(lambda x: cache_image(300, 200, keyword="brand"))
    url = factory.Faker("url")
    is_featured = factory.Faker("boolean", chance_of_getting_true=75)


class TestimonialFactory(BaseFactory):
    class Meta:
        model = Testimonial

    section = factory.SubFactory(TestimonialsSectionFactory)
    content = factory.Faker("paragraph", nb_sentences=4)
    author = factory.Faker("name")
    position = factory.Faker("job")
    company_logo = factory.LazyAttribute(
        lambda x: cache_image(200, 200, keyword="logo")
    )
    is_featured = factory.Faker("boolean", chance_of_getting_true=50)


class ContactDataFactory(BaseFactory):
    class Meta:
        model = ContactData

    section = factory.SubFactory(ContactSectionFactory)
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
    fax = factory.Faker("phone_number")


class ContactPhoneFactory(BaseFactory):
    class Meta:
        model = ContactPhone

    contact = factory.SubFactory(ContactDataFactory)
    number = factory.Faker("phone_number")
    type = factory.Faker("random_element", elements=["phone", "whatsapp"])
    is_primary = factory.Faker("boolean", chance_of_getting_true=25)


class ContactEmailFactory(BaseFactory):
    class Meta:
        model = ContactEmail

    contact = factory.SubFactory(ContactDataFactory)
    email = factory.Faker("email")
    department = factory.Faker("job")
    is_primary = factory.Faker("boolean", chance_of_getting_true=25)


class ContactGroupFactory(BaseFactory):
    class Meta:
        model = ContactGroup

    section = factory.SubFactory(ContactSectionFactory)
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

    section = factory.SubFactory(ContactSectionFactory)
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

    section = factory.SubFactory(CareerSectionFactory)
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

    section = factory.SubFactory(NewsSectionFactory)
    title = factory.Faker("sentence", nb_words=7)
    excerpt = factory.Faker("sentence", nb_words=16)
    content = factory.Faker("paragraph", nb_sentences=7)
    image = factory.LazyAttribute(lambda x: cache_image(800, 600, keyword="news"))
    published_at = factory.Faker("date_object")
    category = factory.Faker("word")
    is_featured = factory.Faker("boolean", chance_of_getting_true=25)
    article_url = factory.LazyFunction(
        lambda: fake.url() if fake.boolean(chance_of_getting_true=30) else None
    )
