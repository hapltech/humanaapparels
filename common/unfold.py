from django.urls import reverse_lazy
from django.templatetags.static import static


UNFOLD_CONFIG = {
    "SITE_TITLE": "Humana Apparels Pvt. Ltd. Admin",
    "SITE_HEADER": "HAPL Admin",
    "SITE_SYMBOL": "public",
    "STYLES": [
        lambda request: static("css/admin.styles.css"),
    ],
    "BORDER_RADIUS": "10px",
    "COLORS": {
        "base": {
            "50": "250 250 250",
            "100": "244 245 246",
            "200": "228 230 232",
            "300": "212 215 218",
            "400": "176 181 186",
            "500": "136 141 147",
            "600": "102 107 114",
            "700": "78 83 90",
            "800": "54 58 65",
            "900": "34 38 45",
            "950": "18 20 26",
        },
        "primary": {
            "50": "226 239 247",
            "100": "192 217 236",
            "200": "148 188 221",
            "300": "104 159 206",
            "400": "61 130 191",
            "500": "5 75 121",
            "600": "4 66 107",
            "700": "3 55 90",
            "800": "3 44 73",
            "900": "2 36 60",
            "950": "1 22 39",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",
            "subtle-dark": "var(--color-base-400)",
            "default-light": "var(--color-base-600)",
            "default-dark": "var(--color-base-300)",
            "important-light": "var(--color-base-900)",
            "important-dark": "var(--color-base-100)",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Authentication & Users",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Users",
                        "icon": "group",
                        "link": reverse_lazy("admin:users_user_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "users.view_user"
                        ),
                    },
                    {
                        "title": "Departments",
                        "icon": "apartment",
                        "link": reverse_lazy("admin:users_department_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "users.view_department"
                        ),
                    },
                    {
                        "title": "Roles",
                        "icon": "badge",
                        "link": reverse_lazy("admin:users_role_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "users.view_role"
                        ),
                    },
                ],
            },
            {
                "title": "Home Page",
                "separator": True,
                "collapsible": True,
                "icon": "home",
                "items": [
                    {
                        "title": "Hero Section",
                        "icon": "featured_video",
                        "link": reverse_lazy("admin:hapl_homeherosection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_homeherosection"
                        ),
                    },
                    {
                        "title": "Introduction Section",
                        "icon": "info",
                        "link": reverse_lazy(
                            "admin:hapl_homeintroductionsection_changelist"
                        ),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_homeintroductionsection"
                        ),
                    },
                    {
                        "title": "Services Section",
                        "icon": "design_services",
                        "link": reverse_lazy(
                            "admin:hapl_homeservicessection_changelist"
                        ),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_homeservicessection"
                        ),
                    },
                    {
                        "title": "Stats Section",
                        "icon": "assessment",
                        "link": reverse_lazy("admin:hapl_homestatssection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_homestatssection"
                        ),
                    },
                ],
            },
            {
                "title": "About Page",
                "separator": True,
                "collapsible": True,
                "icon": "info",
                "items": [
                    {
                        "title": "About Section",
                        "icon": "description",
                        "link": reverse_lazy("admin:hapl_aboutsection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_aboutsection"
                        ),
                    },
                    {
                        "title": "Team Section",
                        "icon": "diversity_3",
                        "link": reverse_lazy("admin:hapl_teamsection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_teamsection"
                        ),
                    },
                    {
                        "title": "FAQ Section",
                        "icon": "quiz",
                        "link": reverse_lazy("admin:hapl_faqsection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_faqsection"
                        ),
                    },
                ],
            },
            {
                "title": "Customers Page",
                "separator": True,
                "collapsible": True,
                "icon": "storefront",
                "items": [
                    {
                        "title": "Customers Section",
                        "icon": "business",
                        "link": reverse_lazy("admin:hapl_customerssection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_customerssection"
                        ),
                    },
                    {
                        "title": "Testimonials Section",
                        "icon": "forum",
                        "link": reverse_lazy(
                            "admin:hapl_testimonialssection_changelist"
                        ),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_testimonialssection"
                        ),
                    },
                ],
            },
            {
                "title": "Contact Page",
                "separator": True,
                "collapsible": True,
                "icon": "contact_page",
                "items": [
                    {
                        "title": "Contact Section",
                        "icon": "contact_mail",
                        "link": reverse_lazy("admin:hapl_contactsection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_contactsection"
                        ),
                    },
                    {
                        "title": "Contact Data",
                        "icon": "location_on",
                        "link": reverse_lazy("admin:hapl_contactdata_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_contactdata"
                        ),
                    },
                    {
                        "title": "Contact Groups",
                        "icon": "group_work",
                        "link": reverse_lazy("admin:hapl_contactgroup_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_contactgroup"
                        ),
                    },
                    {
                        "title": "Social Links",
                        "icon": "share",
                        "link": reverse_lazy("admin:hapl_social_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_social"
                        ),
                    },
                ],
            },
            {
                "title": "Career Page",
                "separator": True,
                "collapsible": True,
                "icon": "work",
                "items": [
                    {
                        "title": "Career Section",
                        "icon": "business_center",
                        "link": reverse_lazy("admin:hapl_careersection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_careersection"
                        ),
                    },
                    {
                        "title": "Career Positions",
                        "icon": "work_outline",
                        "link": reverse_lazy("admin:hapl_careerposition_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_careerposition"
                        ),
                    },
                ],
            },
            {
                "title": "News Page",
                "separator": True,
                "collapsible": True,
                "icon": "article",
                "items": [
                    {
                        "title": "News Section",
                        "icon": "newspaper",
                        "link": reverse_lazy("admin:hapl_newssection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_newssection"
                        ),
                    },
                    {
                        "title": "News Articles",
                        "icon": "feed",
                        "link": reverse_lazy("admin:hapl_newsarticle_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_newsarticle"
                        ),
                    },
                ],
            },
            {
                "title": "Products Page",
                "separator": True,
                "collapsible": True,
                "icon": "inventory_2",
                "items": [
                    {
                        "title": "Products Page",
                        "icon": "checkroom",
                        "link": reverse_lazy("admin:hapl_productspage_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_productspage"
                        ),
                    },
                    {
                        "title": "Product Categories",
                        "icon": "category",
                        "link": reverse_lazy("admin:hapl_productcategory_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_productcategory"
                        ),
                    },
                    {
                        "title": "Products",
                        "icon": "inventory",
                        "link": reverse_lazy("admin:hapl_product_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_product"
                        ),
                    },
                ],
            },
            {
                "title": "Compliance Page",
                "separator": True,
                "collapsible": True,
                "icon": "policy",
                "items": [
                    {
                        "title": "Compliance Page",
                        "icon": "verified",
                        "link": reverse_lazy("admin:hapl_compliancepage_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_compliancepage"
                        ),
                    },
                    {
                        "title": "Compliance Sections",
                        "icon": "rule",
                        "link": reverse_lazy("admin:hapl_compliancesection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_compliancesection"
                        ),
                    },
                    {
                        "title": "Certificates",
                        "icon": "verified_user",
                        "link": reverse_lazy(
                            "admin:hapl_compliancecertificate_changelist"
                        ),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_compliancecertificate"
                        ),
                    },
                ],
            },
            {
                "title": "Sustainability Page",
                "separator": True,
                "collapsible": True,
                "icon": "eco",
                "items": [
                    {
                        "title": "Sustainability Page",
                        "icon": "park",
                        "link": reverse_lazy(
                            "admin:hapl_sustainabilitypage_changelist"
                        ),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_sustainabilitypage"
                        ),
                    },
                    {
                        "title": "Sustainability Sections",
                        "icon": "nature",
                        "link": reverse_lazy(
                            "admin:hapl_sustainabilitysection_changelist"
                        ),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_sustainabilitysection"
                        ),
                    },
                    {
                        "title": "Certificates",
                        "icon": "recycling",
                        "link": reverse_lazy(
                            "admin:hapl_sustainabilitycertificate_changelist"
                        ),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_sustainabilitycertificate"
                        ),
                    },
                ],
            },
            {
                "title": "Gallery Page",
                "separator": True,
                "collapsible": True,
                "icon": "collections",
                "items": [
                    {
                        "title": "Gallery Page",
                        "icon": "photo_library",
                        "link": reverse_lazy("admin:hapl_gallerypage_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_gallerypage"
                        ),
                    },
                    {
                        "title": "Gallery Sections",
                        "icon": "folder",
                        "link": reverse_lazy("admin:hapl_gallerysection_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_gallerysection"
                        ),
                    },
                    {
                        "title": "Images",
                        "icon": "image",
                        "link": reverse_lazy("admin:hapl_galleryimage_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_galleryimage"
                        ),
                    },
                    {
                        "title": "Videos",
                        "icon": "videocam",
                        "link": reverse_lazy("admin:hapl_galleryvideo_changelist"),
                        "permission": lambda request: request.user.has_perm(
                            "hapl.view_galleryvideo"
                        ),
                    },
                ],
            },
        ],
    },
}
