from django.db import models
from common.models import BaseModel
from common.fields import OptimizedImageField


class BaseSection(BaseModel):
    """Abstract base model for content sections with title and subtitle"""

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# --- --- Home Page Models --- ---
class HomeHeroSection(BaseSection):
    """Section model for home page hero/carousel"""

    pass


class HomeCarouselSlide(BaseModel):
    section = models.ForeignKey(
        HomeHeroSection, related_name="slides", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    image = OptimizedImageField(upload_to="home/carousel/")
    is_active = models.BooleanField(default=True)
    cta_text = models.CharField(max_length=100, blank=True, null=True)
    cta_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class HomeIntroductionSection(BaseSection):
    """Section model for home page introduction"""

    content = models.TextField(null=True, blank=True)
    image = OptimizedImageField(upload_to="home/", blank=True, null=True)


class HomeIntroductionFeature(BaseModel):
    introduction = models.ForeignKey(
        HomeIntroductionSection, related_name="features", on_delete=models.CASCADE
    )
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class HomeServicesSection(BaseSection):
    """Section model for services showcase on home page"""

    pass


class Service(BaseModel):
    section = models.ForeignKey(
        HomeServicesSection,
        related_name="services",
        on_delete=models.CASCADE,
        null=True,
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Phosphor icon class")
    image = OptimizedImageField(
        upload_to="services/", max_dimensions=((800, 800)), blank=True, null=True
    )

    def __str__(self):
        return self.title


class HomeStatsSection(BaseSection):
    """Section model for company stats on home page"""

    pass


class CompanyStats(BaseModel):
    section = models.ForeignKey(
        HomeStatsSection, related_name="stats", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


# --- About Page Models ---
class AboutSection(BaseSection):
    """Main about section model"""

    content = models.TextField(null=True, blank=True)
    image = OptimizedImageField(upload_to="about/", max_dimensions=(800, 800))


class TeamSection(BaseSection):
    """Section model for team members"""

    pass


class TeamMember(BaseModel):
    section = models.ForeignKey(
        TeamSection, related_name="members", on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = OptimizedImageField(upload_to="team/", max_dimensions=(400, 400))
    is_management = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FAQSection(BaseSection):
    """Section model for frequently asked questions"""

    pass


class FAQ(BaseModel):
    section = models.ForeignKey(
        FAQSection, related_name="faqs", on_delete=models.CASCADE, null=True
    )
    question = models.CharField(max_length=200)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question


# --- Customers Page Models ---
class CustomersSection(BaseSection):
    """Section model for customer showcase"""

    pass


class Customer(BaseModel):
    section = models.ForeignKey(
        CustomersSection, related_name="customers", on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=100)
    logo = OptimizedImageField(upload_to="customers/", max_dimensions=(200, 200))
    url = models.URLField()
    is_featured = models.BooleanField(default=False, help_text="Display on home page")

    def __str__(self):
        return self.name


class TestimonialsSection(BaseSection):
    """Section model for client testimonials"""

    pass


class Testimonial(BaseModel):
    section = models.ForeignKey(
        TestimonialsSection,
        related_name="testimonials",
        on_delete=models.CASCADE,
        null=True,
    )
    content = models.TextField()
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company_logo = OptimizedImageField(
        upload_to="testimonials/", max_dimensions=(100, 100)
    )
    is_featured = models.BooleanField(default=False, help_text="Featured testimonial")

    def __str__(self):
        return self.author


# --- Contact Page Models ---
class ContactSection(BaseSection):
    """Main contact section model"""

    pass


class ContactData(BaseModel):
    section = models.OneToOneField(
        ContactSection, related_name="data", on_delete=models.CASCADE, null=True
    )
    map_title = models.CharField(max_length=200)
    map_subtitle = models.CharField(max_length=500, blank=True, null=True)
    map_image = OptimizedImageField(upload_to="contact/")
    map_url = models.URLField()
    address = models.CharField(max_length=200)
    office_title = models.CharField(max_length=200)
    office_subtitle = models.CharField(max_length=500, blank=True, null=True)
    office_image = OptimizedImageField(upload_to="contact/")
    fax = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.office_title


class ContactMethod(BaseModel):
    """Base model for contact methods (phone, email, etc.)"""

    contact = models.ForeignKey(
        ContactData, related_name="%(class)ss", on_delete=models.CASCADE
    )
    is_primary = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ContactPhone(ContactMethod):
    number = models.CharField(max_length=20)
    type = models.CharField(
        max_length=20,
        choices=(
            ("phone", "Phone"),
            ("whatsapp", "WhatsApp"),
        ),
        default="phone",
    )

    def __str__(self):
        return f"{self.type}: {self.number}"


class ContactEmail(ContactMethod):
    email = models.EmailField()
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email


class ContactGroup(BaseModel):
    section = models.ForeignKey(
        ContactSection, related_name="groups", on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactMember(BaseModel):
    group = models.ForeignKey(
        ContactGroup, related_name="members", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = OptimizedImageField(upload_to="contact/members/", max_dimensions=(400, 400))
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Social(BaseModel):
    section = models.ForeignKey(
        ContactSection, related_name="socials", on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text="Phosphor Icon class")

    def __str__(self):
        return self.name


# --- Career Page Models ---
class CareerSection(BaseSection):
    """Section model for career listings"""

    pass


class CareerPosition(BaseModel):
    section = models.ForeignKey(
        CareerSection, related_name="positions", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    posted_at = models.DateField()
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=(("active", "Active"), ("inactive", "Inactive")),
        default="active",
    )

    def __str__(self):
        return self.title


# --- News Page Models ---
class NewsSection(BaseSection):
    """Section model for news articles"""

    pass


class NewsArticle(BaseModel):
    section = models.ForeignKey(
        NewsSection, related_name="articles", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)
    image = OptimizedImageField(upload_to="news/", max_dimensions=(1000, 1000))
    published_at = models.DateField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False, help_text="Feature on home page")
    article_url = models.URLField(
        blank=True, null=True, help_text="Optional external URL"
    )

    def __str__(self):
        return self.title
