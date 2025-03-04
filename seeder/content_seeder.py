import logging
from django.db import transaction
from seeder.content_factories import (
    HomeHeroSectionFactory,
    HomeIntroductionSectionFactory,
    HomeServicesSectionFactory,
    HomeStatsSectionFactory,
    AboutSectionFactory,
    TeamSectionFactory,
    FAQSectionFactory,
    CustomersSectionFactory,
    TestimonialsSectionFactory,
    ContactSectionFactory,
    CareerSectionFactory,
    NewsSectionFactory,
    HomeCarouselSlideFactory,
    HomeIntroductionFeatureFactory,
    ServiceFactory,
    CompanyStatsFactory,
    TeamMemberFactory,
    FAQFactory,
    CustomerFactory,
    TestimonialFactory,
    ContactDataFactory,
    ContactPhoneFactory,
    ContactEmailFactory,
    ContactGroupFactory,
    ContactMemberFactory,
    SocialFactory,
    CareerPositionFactory,
    NewsArticleFactory,
)


logger = logging.getLogger(__name__)


class Seeder:
    """Base seeder class."""

    def __init__(self, clean=False):
        self.clean = clean

    def run(self):
        raise NotImplementedError

    def clean_data(self):
        """Delete existing data before seeding."""
        raise NotImplementedError


class HomeSeeder(Seeder):
    def clean_data(self):
        # Clean section models first
        HomeHeroSectionFactory._meta.model.objects.all().delete()
        HomeIntroductionSectionFactory._meta.model.objects.all().delete()
        HomeServicesSectionFactory._meta.model.objects.all().delete()
        HomeStatsSectionFactory._meta.model.objects.all().delete()

        # Then clean content models
        HomeCarouselSlideFactory._meta.model.objects.all().delete()
        HomeIntroductionFeatureFactory._meta.model.objects.all().delete()
        CompanyStatsFactory._meta.model.objects.all().delete()
        ServiceFactory._meta.model.objects.all().delete()

        logger.info("🧹 Home data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Home data...")

        # Create sections first
        hero_section = HomeHeroSectionFactory.create()
        intro_section = HomeIntroductionSectionFactory.create()
        services_section = HomeServicesSectionFactory.create()
        stats_section = HomeStatsSectionFactory.create()

        # Then create content items that reference the sections
        HomeCarouselSlideFactory.create_batch(3, section=hero_section)
        HomeIntroductionFeatureFactory.create_batch(3, introduction=intro_section)
        ServiceFactory.create_batch(3, section=services_section)
        CompanyStatsFactory.create_batch(4, section=stats_section)

        # Create news articles with featured flag for home page
        NewsArticleFactory.create_batch(3, is_featured=True)

        # Create customers with featured flag for home page
        CustomerFactory.create_batch(4, is_featured=True)

        logger.info("✅ Home data seeded.")


class AboutSeeder(Seeder):
    def clean_data(self):
        # Clean section models first
        AboutSectionFactory._meta.model.objects.all().delete()
        TeamSectionFactory._meta.model.objects.all().delete()
        FAQSectionFactory._meta.model.objects.all().delete()

        # Then clean content models
        TeamMemberFactory._meta.model.objects.all().delete()
        FAQFactory._meta.model.objects.all().delete()

        logger.info("🧹 About data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding About data...")

        # Create sections first
        AboutSectionFactory.create()
        team_section = TeamSectionFactory.create()
        faq_section = FAQSectionFactory.create()

        # Then create content items
        TeamMemberFactory.create_batch(5, section=team_section, is_management=True)
        TeamMemberFactory.create_batch(10, section=team_section, is_management=False)
        FAQFactory.create_batch(5, section=faq_section)

        logger.info("✅ About data seeded.")


class CustomerSeeder(Seeder):
    def clean_data(self):
        # Clean section models first
        CustomersSectionFactory._meta.model.objects.all().delete()
        TestimonialsSectionFactory._meta.model.objects.all().delete()

        # Then clean content models
        CustomerFactory._meta.model.objects.all().delete()
        TestimonialFactory._meta.model.objects.all().delete()

        logger.info("🧹 Customer data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Customer data...")

        # Create sections first
        customers_section = CustomersSectionFactory.create()
        testimonials_section = TestimonialsSectionFactory.create()

        # Then create content items
        CustomerFactory.create_batch(10, section=customers_section)
        TestimonialFactory.create_batch(4, section=testimonials_section)
        # Set one testimonial as featured
        TestimonialFactory.create(section=testimonials_section, is_featured=True)

        logger.info("✅ Customer data seeded.")


class ContactSeeder(Seeder):
    def clean_data(self):
        # Clean section model first
        ContactSectionFactory._meta.model.objects.all().delete()

        # Then clean content models
        ContactDataFactory._meta.model.objects.all().delete()
        ContactGroupFactory._meta.model.objects.all().delete()
        ContactMemberFactory._meta.model.objects.all().delete()
        SocialFactory._meta.model.objects.all().delete()
        ContactPhoneFactory._meta.model.objects.all().delete()
        ContactEmailFactory._meta.model.objects.all().delete()

        logger.info("🧹 Contact data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Contact data...")

        # Create section first
        contact_section = ContactSectionFactory.create()

        # Create contact data
        contact_data = ContactDataFactory.create(section=contact_section)

        # Add phone numbers and emails
        ContactPhoneFactory.create(contact=contact_data, type="phone", is_primary=True)
        ContactPhoneFactory.create(contact=contact_data, type="whatsapp")

        ContactEmailFactory.create(
            contact=contact_data, department="Sales", is_primary=True
        )
        ContactEmailFactory.create(contact=contact_data, department="Support")

        # Create groups and members
        for dept in ["Sales", "Production"]:
            group = ContactGroupFactory.create(section=contact_section, name=dept)
            ContactMemberFactory.create_batch(3, group=group)

        # Create social media links
        SocialFactory.create_batch(3, section=contact_section)

        logger.info("✅ Contact data seeded.")


class CareerSeeder(Seeder):
    def clean_data(self):
        # Clean section model first
        CareerSectionFactory._meta.model.objects.all().delete()

        # Then clean content models
        CareerPositionFactory._meta.model.objects.all().delete()

        logger.info("🧹 Career data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Career data...")

        # Create section first
        career_section = CareerSectionFactory.create()

        # Then create positions
        CareerPositionFactory.create_batch(3, section=career_section, status="active")

        logger.info("✅ Career data seeded.")


class NewsSeeder(Seeder):
    def clean_data(self):
        # Clean section model first
        NewsSectionFactory._meta.model.objects.all().delete()

        # Then clean content models
        NewsArticleFactory._meta.model.objects.all().delete()

        logger.info("🧹 News data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding News data...")

        # Create section first
        news_section = NewsSectionFactory.create()

        # Then create articles
        NewsArticleFactory.create_batch(3, section=news_section)
        # Add a few featured articles
        NewsArticleFactory.create_batch(2, section=news_section, is_featured=True)

        logger.info("✅ News data seeded.")
