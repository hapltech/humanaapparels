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
                    },
                    {
                        "title": "Departments",
                        "icon": "apartment",
                        "link": reverse_lazy("admin:users_department_changelist"),
                    },
                    {
                        "title": "Roles",
                        "icon": "badge",
                        "link": reverse_lazy("admin:users_role_changelist"),
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
                    },
                    {
                        "title": "Carousel Slides",
                        "icon": "photo_library",
                        "link": reverse_lazy("admin:hapl_homecarouselslide_changelist"),
                    },
                    {
                        "title": "Introduction Section",
                        "icon": "info",
                        "link": reverse_lazy(
                            "admin:hapl_homeintroductionsection_changelist"
                        ),
                    },
                    {
                        "title": "Introduction Features",
                        "icon": "stars",
                        "link": reverse_lazy(
                            "admin:hapl_homeintroductionfeature_changelist"
                        ),
                    },
                    {
                        "title": "Services Section",
                        "icon": "design_services",
                        "link": reverse_lazy(
                            "admin:hapl_homeservicessection_changelist"
                        ),
                    },
                    {
                        "title": "Services",
                        "icon": "apparel",
                        "link": reverse_lazy("admin:hapl_service_changelist"),
                    },
                    {
                        "title": "Stats Section",
                        "icon": "assessment",
                        "link": reverse_lazy("admin:hapl_homestatssection_changelist"),
                    },
                    {
                        "title": "Company Stats",
                        "icon": "leaderboard",
                        "link": reverse_lazy("admin:hapl_companystats_changelist"),
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
                    },
                    {
                        "title": "Team Section",
                        "icon": "diversity_3",
                        "link": reverse_lazy("admin:hapl_teamsection_changelist"),
                    },
                    {
                        "title": "Team Members",
                        "icon": "groups",
                        "link": reverse_lazy("admin:hapl_teammember_changelist"),
                    },
                    {
                        "title": "FAQ Section",
                        "icon": "quiz",
                        "link": reverse_lazy("admin:hapl_faqsection_changelist"),
                    },
                    {
                        "title": "FAQs",
                        "icon": "help",
                        "link": reverse_lazy("admin:hapl_faq_changelist"),
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
                    },
                    {
                        "title": "Customers",
                        "icon": "store",
                        "link": reverse_lazy("admin:hapl_customer_changelist"),
                    },
                    {
                        "title": "Testimonials Section",
                        "icon": "forum",
                        "link": reverse_lazy(
                            "admin:hapl_testimonialssection_changelist"
                        ),
                    },
                    {
                        "title": "Testimonials",
                        "icon": "comment",
                        "link": reverse_lazy("admin:hapl_testimonial_changelist"),
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
                    },
                    {
                        "title": "Contact Data",
                        "icon": "location_on",
                        "link": reverse_lazy("admin:hapl_contactdata_changelist"),
                    },
                    {
                        "title": "Phone Numbers",
                        "icon": "phone",
                        "link": reverse_lazy("admin:hapl_contactphone_changelist"),
                    },
                    {
                        "title": "Email Addresses",
                        "icon": "email",
                        "link": reverse_lazy("admin:hapl_contactemail_changelist"),
                    },
                    {
                        "title": "Contact Groups",
                        "icon": "group_work",
                        "link": reverse_lazy("admin:hapl_contactgroup_changelist"),
                    },
                    {
                        "title": "Contact Members",
                        "icon": "contacts",
                        "link": reverse_lazy("admin:hapl_contactmember_changelist"),
                    },
                    {
                        "title": "Social Links",
                        "icon": "share",
                        "link": reverse_lazy("admin:hapl_social_changelist"),
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
                    },
                    {
                        "title": "Career Positions",
                        "icon": "work_outline",
                        "link": reverse_lazy("admin:hapl_careerposition_changelist"),
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
                    },
                    {
                        "title": "News Articles",
                        "icon": "feed",
                        "link": reverse_lazy("admin:hapl_newsarticle_changelist"),
                    },
                ],
            },
        ],
    },
}
