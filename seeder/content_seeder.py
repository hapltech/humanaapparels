import random
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
    ProductsPageFactory,
    ProductCarouselSlideFactory,
    ProductSectionFactory,
    ProductCategoryFactory,
    ProductFactory,
    CompliancePageFactory,
    ComplianceSectionFactory,
    ComplianceCertificateFactory,
    SustainabilityPageFactory,
    SustainabilitySectionFactory,
    SustainabilityCertificateFactory,
    GalleryPageFactory,
    GallerySectionFactory,
    GalleryImageFactory,
    GalleryVideoFactory,
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


class ProductsSeeder(Seeder):
    def clean_data(self):
        # Clean section models first
        ProductsPageFactory._meta.model.objects.all().delete()

        # Then clean content models
        ProductCarouselSlideFactory._meta.model.objects.all().delete()
        ProductSectionFactory._meta.model.objects.all().delete()
        ProductCategoryFactory._meta.model.objects.all().delete()
        ProductFactory._meta.model.objects.all().delete()

        logger.info("🧹 Products data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Products data...")

        # Create main page
        products_page = ProductsPageFactory.create()

        # Create carousel slides
        ProductCarouselSlideFactory.create_batch(3, page=products_page)

        # Create sections (some before, some after products)
        ProductSectionFactory.create_batch(3, page=products_page, after_products=False)
        ProductSectionFactory.create_batch(2, page=products_page, after_products=True)

        # Create product categories and products
        for category_name in ["Jackets", "Pants", "Shirts", "Denim"]:
            category = ProductCategoryFactory.create(
                page=products_page, name=category_name
            )
            # Create 5-10 products for each category
            product_count = random.randint(5, 10)
            ProductFactory.create_batch(product_count, category=category)

        logger.info("✅ Products data seeded.")


class ComplianceSeeder(Seeder):
    def clean_data(self):
        # Clean section models first
        CompliancePageFactory._meta.model.objects.all().delete()

        # Then clean content models
        ComplianceSectionFactory._meta.model.objects.all().delete()
        ComplianceCertificateFactory._meta.model.objects.all().delete()

        logger.info("🧹 Compliance data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Compliance data...")

        # Create main page
        compliance_page = CompliancePageFactory.create()

        # Create content sections
        ComplianceSectionFactory.create_batch(5, page=compliance_page)

        # Create certificates
        ComplianceCertificateFactory.create_batch(7, page=compliance_page)

        logger.info("✅ Compliance data seeded.")


class SustainabilitySeeder(Seeder):
    def clean_data(self):
        # Clean section models first
        SustainabilityPageFactory._meta.model.objects.all().delete()

        # Then clean content models
        SustainabilitySectionFactory._meta.model.objects.all().delete()
        SustainabilityCertificateFactory._meta.model.objects.all().delete()

        logger.info("🧹 Sustainability data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Sustainability data...")

        # Create main page
        sustainability_page = SustainabilityPageFactory.create()

        # Create content sections
        SustainabilitySectionFactory.create_batch(5, page=sustainability_page)

        # Create certificates
        SustainabilityCertificateFactory.create_batch(5, page=sustainability_page)

        logger.info("✅ Sustainability data seeded.")


class GallerySeeder(Seeder):
    def clean_data(self):
        # Clean section models first
        GalleryPageFactory._meta.model.objects.all().delete()

        # Then clean content models
        GallerySectionFactory._meta.model.objects.all().delete()
        GalleryImageFactory._meta.model.objects.all().delete()
        GalleryVideoFactory._meta.model.objects.all().delete()

        logger.info("🧹 Gallery data cleaned.")

    @transaction.atomic
    def run(self):
        if self.clean:
            self.clean_data()
        logger.info("🌱 Seeding Gallery data...")

        # Create main page
        gallery_page = GalleryPageFactory.create()

        # Create gallery sections
        sections = ["Products", "Factory", "Team", "Events"]
        for section_name in sections:
            section = GallerySectionFactory.create(page=gallery_page, name=section_name)

            # Create images for each section
            GalleryImageFactory.create_batch(8, section=section)

            # Create videos for each section (fewer videos than images)
            GalleryVideoFactory.create_batch(2, section=section)

        logger.info("✅ Gallery data seeded.")
