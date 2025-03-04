from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline
from unfold.contrib.forms.widgets import WysiwygWidget
from django.db import models
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


class BaseModelAdmin(ModelAdmin):
    """Base admin class that hides tracking fields for all models"""

    exclude = ("created_at", "updated_at", "created_by", "updated_by")


class BaseInline(StackedInline):
    """Base inline class that hides tracking fields"""

    exclude = ("created_at", "updated_at", "created_by", "updated_by")


class BaseSectionAdmin(BaseModelAdmin):
    """Base admin class for section models with title and subtitle"""

    fieldsets = (
        (
            "Section Settings",
            {
                "fields": ("title", "subtitle"),
            },
        ),
    )


# --- Home Page Sections ---


class HomeCarouselSlideInline(BaseInline):
    model = HomeCarouselSlide
    extra = 1


@admin.register(HomeHeroSection)
class HomeHeroSectionAdmin(BaseSectionAdmin):
    inlines = [HomeCarouselSlideInline]


@admin.register(HomeCarouselSlide)
class HomeCarouselSlideAdmin(BaseModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)


class HomeIntroductionFeatureInline(BaseInline):
    model = HomeIntroductionFeature
    extra = 1


@admin.register(HomeIntroductionSection)
class HomeIntroductionSectionAdmin(BaseSectionAdmin):
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}
    inlines = [HomeIntroductionFeatureInline]

    fieldsets = (
        (
            "Section Settings",
            {
                "fields": ("title", "subtitle"),
            },
        ),
        (
            "Content",
            {
                "fields": ("content", "image"),
            },
        ),
    )


@admin.register(HomeIntroductionFeature)
class HomeIntroductionFeatureAdmin(BaseModelAdmin):
    list_display = ("title", "icon")


class ServiceInline(BaseInline):
    model = Service
    extra = 1


@admin.register(HomeServicesSection)
class HomeServicesSectionAdmin(BaseSectionAdmin):
    inlines = [ServiceInline]


@admin.register(Service)
class ServiceAdmin(BaseModelAdmin):
    list_display = ("title", "icon")
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


class CompanyStatsInline(BaseInline):
    model = CompanyStats
    extra = 1


@admin.register(HomeStatsSection)
class HomeStatsSectionAdmin(BaseSectionAdmin):
    inlines = [CompanyStatsInline]


@admin.register(CompanyStats)
class CompanyStatsAdmin(BaseModelAdmin):
    list_display = ("title", "value", "icon")


# --- About Page Sections ---
@admin.register(AboutSection)
class AboutSectionAdmin(BaseSectionAdmin):
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}

    fieldsets = (
        (
            "Section Settings",
            {
                "fields": ("title", "subtitle"),
            },
        ),
        (
            "Content",
            {
                "fields": ("content", "image"),
            },
        ),
    )


class TeamMemberInline(BaseInline):
    model = TeamMember
    extra = 1


@admin.register(TeamSection)
class TeamSectionAdmin(BaseSectionAdmin):
    inlines = [TeamMemberInline]


@admin.register(TeamMember)
class TeamMemberAdmin(BaseModelAdmin):
    list_display = ("name", "position", "is_management")
    list_filter = ("is_management",)


class FAQInline(BaseInline):
    model = FAQ
    extra = 1


@admin.register(FAQSection)
class FAQSectionAdmin(BaseSectionAdmin):
    inlines = [FAQInline]


@admin.register(FAQ)
class FAQAdmin(BaseModelAdmin):
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


# --- Customers Page Sections ---


class CustomerInline(BaseInline):
    model = Customer
    extra = 1


@admin.register(CustomersSection)
class CustomersSectionAdmin(BaseSectionAdmin):
    inlines = [CustomerInline]


@admin.register(Customer)
class CustomerAdmin(BaseModelAdmin):
    list_display = ("name", "is_featured")
    list_filter = ("is_featured",)


class TestimonialInline(BaseInline):
    model = Testimonial
    extra = 1


@admin.register(TestimonialsSection)
class TestimonialsSectionAdmin(BaseSectionAdmin):
    inlines = [TestimonialInline]


@admin.register(Testimonial)
class TestimonialAdmin(BaseModelAdmin):
    list_display = ("author", "position", "is_featured")
    list_filter = ("is_featured",)
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


# --- Contact Page Sections ---
@admin.register(ContactSection)
class ContactSectionAdmin(BaseSectionAdmin):
    pass


class ContactPhoneInline(BaseInline):
    model = ContactPhone
    extra = 1


class ContactEmailInline(BaseInline):
    model = ContactEmail
    extra = 1


@admin.register(ContactData)
class ContactDataAdmin(BaseModelAdmin):
    inlines = [ContactPhoneInline, ContactEmailInline]


@admin.register(ContactPhone)
class ContactPhoneAdmin(BaseModelAdmin):
    list_display = ("number", "type", "is_primary")
    list_filter = ("type", "is_primary")


@admin.register(ContactEmail)
class ContactEmailAdmin(BaseModelAdmin):
    list_display = ("email", "department", "is_primary")
    list_filter = ("is_primary",)


class ContactMemberInline(BaseInline):
    model = ContactMember
    extra = 1


@admin.register(ContactGroup)
class ContactGroupAdmin(BaseModelAdmin):
    inlines = [ContactMemberInline]


@admin.register(ContactMember)
class ContactMemberAdmin(BaseModelAdmin):
    list_display = ("name", "position", "group")
    list_filter = ("group",)


@admin.register(Social)
class SocialAdmin(BaseModelAdmin):
    list_display = ("name", "icon")


# --- Career Page Sections ---


class CareerPositionInline(BaseInline):
    model = CareerPosition
    extra = 1


@admin.register(CareerSection)
class CareerSectionAdmin(BaseSectionAdmin):
    inlines = [CareerPositionInline]


@admin.register(CareerPosition)
class CareerPositionAdmin(BaseModelAdmin):
    list_display = ("title", "location", "department", "status")
    list_filter = ("location", "department", "status")
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


# --- News Page Sections ---


class NewsArticleInline(BaseInline):
    model = NewsArticle
    extra = 1


@admin.register(NewsSection)
class NewsSectionAdmin(BaseSectionAdmin):
    inlines = [NewsArticleInline]


@admin.register(NewsArticle)
class NewsArticleAdmin(BaseModelAdmin):
    list_display = ("title", "published_at", "category", "is_featured")
    list_filter = ("category", "is_featured", "published_at")
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}
