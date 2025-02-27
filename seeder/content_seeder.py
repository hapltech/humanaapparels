import logging
from django.db import transaction
from hapl.models import ContactGroup
from seeder.content_factories import (
    HomeCarouselSlideFactory,
    HomeIntroductionFactory,
    FeaturedArticleFactory,
    FeaturedClientFactory,
    CompanyStatsFactory,
    ServiceFactory,
    AboutDataFactory,
    TeamMemberFactory,
    FAQFactory,
    CustomerFactory,
    TestimonialFactory,
    ContactDataFactory,
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
        HomeCarouselSlideFactory._meta.model.objects.all().delete()
        HomeIntroductionFactory._meta.model.objects.all().delete()
        FeaturedArticleFactory._meta.model.objects.all().delete()
        FeaturedClientFactory._meta.model.objects.all().delete()
        CompanyStatsFactory._meta.model.objects.all().delete()
        ServiceFactory._meta.model.objects.all().delete()
        logger.info("🧹 Home data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Home data...")
        HomeCarouselSlideFactory.create_batch(3)
        HomeIntroductionFactory.create()
        FeaturedArticleFactory.create_batch(3)
        FeaturedClientFactory.create_batch(10)
        CompanyStatsFactory.create_batch(4)
        ServiceFactory.create_batch(3)
        logger.info("✅ Home data seeded.")


class AboutSeeder(Seeder):
    def clean_data(self):
        AboutDataFactory._meta.model.objects.all().delete()
        TeamMemberFactory._meta.model.objects.all().delete()
        FAQFactory._meta.model.objects.all().delete()
        logger.info("🧹 About data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding About data...")
        AboutDataFactory.create()
        TeamMemberFactory.create_batch(5, is_management=True)
        TeamMemberFactory.create_batch(10, is_management=False)
        FAQFactory.create_batch(5)
        logger.info("✅ About data seeded.")


class CustomerSeeder(Seeder):
    def clean_data(self):
        CustomerFactory._meta.model.objects.all().delete()
        TestimonialFactory._meta.model.objects.all().delete()
        logger.info("🧹 Customer data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Customer data...")
        CustomerFactory.create_batch(10)
        TestimonialFactory.create_batch(4)
        logger.info("✅ Customer data seeded.")


class ContactSeeder(Seeder):
    def clean_data(self):
        ContactDataFactory._meta.model.objects.all().delete()
        ContactGroupFactory._meta.model.objects.all().delete()
        ContactMemberFactory._meta.model.objects.all().delete()
        SocialFactory._meta.model.objects.all().delete()
        logger.info("🧹 Contact data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Contact data...")
        ContactDataFactory.create()
        ContactGroupFactory.create_batch(2)
        for group in ContactGroup.objects.all():
            ContactMemberFactory.create_batch(3, group=group)
        SocialFactory.create_batch(3)
        logger.info("✅ Contact data seeded.")


class CareerSeeder(Seeder):
    def clean_data(self):
        CareerPositionFactory._meta.model.objects.all().delete()
        logger.info("🧹 Career data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Career data...")
        CareerPositionFactory.create_batch(3)
        logger.info("✅ Career data seeded.")


class NewsSeeder(Seeder):
    def clean_data(self):
        NewsArticleFactory._meta.model.objects.all().delete()
        logger.info("🧹 News data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding News data...")
        NewsArticleFactory.create_batch(3)
        logger.info("✅ News data seeded.")
