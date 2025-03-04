from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from django.db import models
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
    HomeIntroductionFeature,
)


@admin.register(HomeCarouselSlide)
class HomeCarouselSlideAdmin(ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)


@admin.register(HomeIntroduction)
class HomeIntroductionAdmin(ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


@admin.register(HomeIntroductionFeature)
class HomeIntroductionFeatureAdmin(ModelAdmin):
    list_display = ("title", "icon")


@admin.register(FeaturedArticle)
class FeaturedArticleAdmin(ModelAdmin):
    list_display = ("title", "published_at", "category")


@admin.register(FeaturedClient)
class FeaturedClientAdmin(ModelAdmin):
    pass


@admin.register(CompanyStats)
class CompanyStatsAdmin(ModelAdmin):
    list_display = ("title", "value", "icon")


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ("title", "icon")


@admin.register(AboutData)
class AboutDataAdmin(ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


@admin.register(TeamMember)
class TeamMemberAdmin(ModelAdmin):
    list_display = ("name", "position", "is_management")
    list_filter = ("is_management",)


@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    pass


@admin.register(ContactData)
class ContactDataAdmin(ModelAdmin):
    pass


class ContactMemberInline(admin.TabularInline):
    model = ContactMember
    extra = 1


@admin.register(ContactGroup)
class ContactGroupAdmin(ModelAdmin):
    inlines = [ContactMemberInline]


@admin.register(ContactMember)
class ContactMemberAdmin(ModelAdmin):
    pass


@admin.register(Social)
class SocialAdmin(ModelAdmin):
    list_display = ("name", "icon")


@admin.register(CareerPosition)
class CareerPositionAdmin(ModelAdmin):
    list_display = ("title", "location", "status")
    list_filter = ("location", "status")
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


@admin.register(NewsArticle)
class NewsArticleAdmin(ModelAdmin):
    list_display = ("title", "published_at", "category")
    list_filter = ("category",)
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}
