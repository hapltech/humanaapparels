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
    ProductsPage,
    ProductCarouselSlide,
    ProductSection,
    ProductCategory,
    Product,
    CompliancePage,
    ComplianceSection,
    ComplianceCertificate,
    SustainabilityPage,
    SustainabilitySection,
    SustainabilityCertificate,
    GalleryPage,
    GallerySection,
    GalleryImage,
    GalleryVideo,
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
    extra = 0


@admin.register(HomeHeroSection)
class HomeHeroSectionAdmin(BaseModelAdmin):
    inlines = [HomeCarouselSlideInline]

    def has_add_permission(self, request):
        # Restrict adding new instances
        return False

    def has_delete_permission(self, request, obj=None):
        # Restrict deleting the instance
        return False


@admin.register(HomeCarouselSlide)
class HomeCarouselSlideAdmin(BaseModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)


class HomeIntroductionFeatureInline(BaseInline):
    model = HomeIntroductionFeature
    extra = 0


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

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HomeIntroductionFeature)
class HomeIntroductionFeatureAdmin(BaseModelAdmin):
    list_display = ("title", "icon")


class ServiceInline(BaseInline):
    model = Service
    extra = 0


@admin.register(HomeServicesSection)
class HomeServicesSectionAdmin(BaseSectionAdmin):
    inlines = [ServiceInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(BaseModelAdmin):
    list_display = ("title", "icon")
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


class CompanyStatsInline(BaseInline):
    model = CompanyStats
    extra = 0


@admin.register(HomeStatsSection)
class HomeStatsSectionAdmin(BaseSectionAdmin):
    inlines = [CompanyStatsInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


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

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TeamMemberInline(BaseInline):
    model = TeamMember
    extra = 0


@admin.register(TeamSection)
class TeamSectionAdmin(BaseSectionAdmin):
    inlines = [TeamMemberInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TeamMember)
class TeamMemberAdmin(BaseModelAdmin):
    list_display = ("name", "position", "is_management")
    list_filter = ("is_management",)


class FAQInline(BaseInline):
    model = FAQ
    extra = 0


@admin.register(FAQSection)
class FAQSectionAdmin(BaseSectionAdmin):
    inlines = [FAQInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FAQ)
class FAQAdmin(BaseModelAdmin):
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


# --- Customers Page Sections ---


class CustomerInline(BaseInline):
    model = Customer
    extra = 0


@admin.register(CustomersSection)
class CustomersSectionAdmin(BaseSectionAdmin):
    inlines = [CustomerInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Customer)
class CustomerAdmin(BaseModelAdmin):
    list_display = ("name", "is_featured")
    list_filter = ("is_featured",)


class TestimonialInline(BaseInline):
    model = Testimonial
    extra = 0


@admin.register(TestimonialsSection)
class TestimonialsSectionAdmin(BaseSectionAdmin):
    inlines = [TestimonialInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Testimonial)
class TestimonialAdmin(BaseModelAdmin):
    list_display = ("author", "position", "is_featured")
    list_filter = ("is_featured",)
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


# --- Contact Page Sections ---
@admin.register(ContactSection)
class ContactSectionAdmin(BaseSectionAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ContactPhoneInline(BaseInline):
    model = ContactPhone
    extra = 0


class ContactEmailInline(BaseInline):
    model = ContactEmail
    extra = 0


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
    extra = 0


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
    extra = 0


@admin.register(CareerSection)
class CareerSectionAdmin(BaseSectionAdmin):
    inlines = [CareerPositionInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CareerPosition)
class CareerPositionAdmin(BaseModelAdmin):
    list_display = ("title", "location", "department", "status")
    list_filter = ("location", "department", "status")
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


# --- News Page Sections ---


class NewsArticleInline(BaseInline):
    model = NewsArticle
    extra = 0


@admin.register(NewsSection)
class NewsSectionAdmin(BaseSectionAdmin):
    inlines = [NewsArticleInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(NewsArticle)
class NewsArticleAdmin(BaseModelAdmin):
    list_display = ("title", "published_at", "category", "is_featured")
    list_filter = ("category", "is_featured", "published_at")
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


class ProductCarouselSlideInline(BaseInline):
    model = ProductCarouselSlide
    extra = 1


class ProductSectionInline(BaseInline):
    model = ProductSection
    extra = 1
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


class ProductCategoryInline(BaseInline):
    model = ProductCategory
    extra = 1


@admin.register(ProductsPage)
class ProductsPageAdmin(BaseSectionAdmin):
    inlines = [ProductCarouselSlideInline, ProductSectionInline, ProductCategoryInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ProductCarouselSlide)
class ProductCarouselSlideAdmin(BaseModelAdmin):
    list_display = ("alt", "page")
    list_filter = ("page",)


@admin.register(ProductSection)
class ProductSectionAdmin(BaseModelAdmin):
    list_display = ("title", "page", "after_products")
    list_filter = ("page", "after_products")
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


class ProductInline(BaseInline):
    model = Product
    extra = 1


@admin.register(ProductCategory)
class ProductCategoryAdmin(BaseModelAdmin):
    list_display = ("name", "page")
    list_filter = ("page",)
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    list_display = ("name", "category", "gender", "buyer")
    list_filter = ("category", "gender")


# --- Compliance Page Sections ---
class ComplianceSectionInline(BaseInline):
    model = ComplianceSection
    extra = 1
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


class ComplianceCertificateInline(BaseInline):
    model = ComplianceCertificate
    extra = 1


@admin.register(CompliancePage)
class CompliancePageAdmin(BaseSectionAdmin):
    inlines = [ComplianceSectionInline, ComplianceCertificateInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ComplianceSection)
class ComplianceSectionAdmin(BaseModelAdmin):
    list_display = ("title", "page")
    list_filter = ("page",)
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


@admin.register(ComplianceCertificate)
class ComplianceCertificateAdmin(BaseModelAdmin):
    list_display = ("name", "page")
    list_filter = ("page",)


# --- Sustainability Page Sections ---
class SustainabilitySectionInline(BaseInline):
    model = SustainabilitySection
    extra = 1
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


class SustainabilityCertificateInline(BaseInline):
    model = SustainabilityCertificate
    extra = 1


@admin.register(SustainabilityPage)
class SustainabilityPageAdmin(BaseSectionAdmin):
    inlines = [SustainabilitySectionInline, SustainabilityCertificateInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SustainabilitySection)
class SustainabilitySectionAdmin(BaseModelAdmin):
    list_display = ("title", "page")
    list_filter = ("page",)
    formfield_overrides = {models.TextField: {"widget": WysiwygWidget}}


@admin.register(SustainabilityCertificate)
class SustainabilityCertificateAdmin(BaseModelAdmin):
    list_display = ("name", "page")
    list_filter = ("page",)


# --- Gallery Page Sections ---
class GallerySectionInline(BaseInline):
    model = GallerySection
    extra = 1


@admin.register(GalleryPage)
class GalleryPageAdmin(BaseSectionAdmin):
    inlines = [GallerySectionInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GalleryImageInline(BaseInline):
    model = GalleryImage
    extra = 1


class GalleryVideoInline(BaseInline):
    model = GalleryVideo
    extra = 1


@admin.register(GallerySection)
class GallerySectionAdmin(BaseModelAdmin):
    list_display = ("name", "page")
    list_filter = ("page",)
    inlines = [GalleryImageInline, GalleryVideoInline]


@admin.register(GalleryImage)
class GalleryImageAdmin(BaseModelAdmin):
    list_display = ("caption", "section")
    list_filter = ("section",)


@admin.register(GalleryVideo)
class GalleryVideoAdmin(BaseModelAdmin):
    list_display = ("caption", "section")
    list_filter = ("section",)


def has_add_permission(self, request):
    return False


def has_delete_permission(self, request, obj=None):
    return False
