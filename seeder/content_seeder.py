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


class Seeder:
    """Base seeder class."""

    def run(self):
        raise NotImplementedError


class HomeSeeder(Seeder):
    def run(self):
        HomeCarouselSlideFactory.create_batch(3)
        HomeIntroductionFactory.create()
        FeaturedArticleFactory.create_batch(3)
        FeaturedClientFactory.create_batch(10)
        CompanyStatsFactory.create_batch(4)
        ServiceFactory.create_batch(3)


class AboutSeeder(Seeder):
    def run(self):
        AboutDataFactory.create()
        TeamMemberFactory.create_batch(5, is_management=True)
        TeamMemberFactory.create_batch(10, is_management=False)
        FAQFactory.create_batch(5)


class CustomerSeeder(Seeder):
    def run(self):
        CustomerFactory.create_batch(10)
        TestimonialFactory.create_batch(4)


class ContactSeeder(Seeder):
    def run(self):
        ContactDataFactory.create()
        ContactGroupFactory.create_batch(2)
        for group in ContactGroup.objects.all():
            ContactMemberFactory.create_batch(3, group=group)
        SocialFactory.create_batch(3)


class CareerSeeder(Seeder):
    def run(self):
        CareerPositionFactory.create_batch(3)


class NewsSeeder(Seeder):
    def run(self):
        NewsArticleFactory.create_batch(3)
