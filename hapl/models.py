from django.db import models
from common.models import BaseModel
from common.fields import OptimizedImageField


class HomeCarouselSlide(BaseModel):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    image = OptimizedImageField(upload_to="home/carousel/")
    is_active = models.BooleanField(default=True)
    cta_text = models.CharField(max_length=100, blank=True, null=True)
    cta_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class HomeIntroduction(BaseModel):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField(null=True, blank=True)


class FeaturedArticle(BaseModel):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500)
    image = OptimizedImageField(upload_to="home/articles/")
    article_url = models.URLField()
    published_at = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class FeaturedClient(BaseModel):
    name = models.CharField(max_length=100)
    logo = OptimizedImageField(upload_to="home/clients/")
    url = models.URLField()

    def __str__(self):
        return self.name


class CompanyStats(BaseModel):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class Service(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    image = OptimizedImageField(
        upload_to="services/", blank=True, null=True
    )

    def __str__(self):
        return self.title


class AboutData(BaseModel):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    image = OptimizedImageField(upload_to="about/")
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class TeamMember(BaseModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = OptimizedImageField(upload_to="team/")
    is_management = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FAQ(BaseModel):
    question = models.CharField(max_length=200)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question


class Customer(BaseModel):
    name = models.CharField(max_length=100)
    logo = OptimizedImageField(upload_to="customers/")
    url = models.URLField()

    def __str__(self):
        return self.name


class Testimonial(BaseModel):
    content = models.TextField()
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company_logo = OptimizedImageField(upload_to="testimonials/")

    def __str__(self):
        return self.author


class ContactData(BaseModel):
    map_title = models.CharField(max_length=200)
    map_subtitle = models.CharField(max_length=500, blank=True, null=True)
    map_image = OptimizedImageField(upload_to="contact/")
    map_url = models.URLField()
    address = models.CharField(max_length=200)
    office_title = models.CharField(max_length=200)
    office_subtitle = models.CharField(max_length=500, blank=True, null=True)
    office_image = OptimizedImageField(upload_to="contact/")
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    email1 = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.map_title


class ContactGroup(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactMember(BaseModel):
    group = models.ForeignKey(
        ContactGroup, related_name="members", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = OptimizedImageField(upload_to="contact/members/")
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Social(BaseModel):
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text="Phosphor Icon class")

    def __str__(self):
        return self.name


class CareerPosition(BaseModel):
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


class NewsArticle(BaseModel):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)
    image = OptimizedImageField(upload_to="news/")
    published_at = models.DateField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
