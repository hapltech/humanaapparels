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
                "title": "Content Management",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Home Carousel Slides",
                        "icon": "photo",
                        "link": reverse_lazy("admin:hapl_homecarouselslide_changelist"),
                    },
                    {
                        "title": "Home Introduction",
                        "icon": "home",
                        "link": reverse_lazy("admin:hapl_homeintroduction_changelist"),
                    },
                    {
                        "title": "Home Introduction Features",
                        "icon": "home",
                        "link": reverse_lazy(
                            "admin:hapl_homeintroductionfeature_changelist"
                        ),
                    },
                    {
                        "title": "Featured Articles",
                        "icon": "article",
                        "link": reverse_lazy("admin:hapl_featuredarticle_changelist"),
                    },
                    {
                        "title": "Featured Clients",
                        "icon": "handshake",
                        "link": reverse_lazy("admin:hapl_featuredclient_changelist"),
                    },
                    {
                        "title": "Company Stats",
                        "icon": "leaderboard",
                        "link": reverse_lazy("admin:hapl_companystats_changelist"),
                    },
                    {
                        "title": "Services",
                        "icon": "settings",
                        "link": reverse_lazy("admin:hapl_service_changelist"),
                    },
                    {
                        "title": "About Data",
                        "icon": "info",
                        "link": reverse_lazy("admin:hapl_aboutdata_changelist"),
                    },
                    {
                        "title": "Team Members",
                        "icon": "groups",
                        "link": reverse_lazy("admin:hapl_teammember_changelist"),
                    },
                    {
                        "title": "FAQs",
                        "icon": "help",
                        "link": reverse_lazy("admin:hapl_faq_changelist"),
                    },
                    {
                        "title": "Customers",
                        "icon": "storefront",
                        "link": reverse_lazy("admin:hapl_customer_changelist"),
                    },
                    {
                        "title": "Testimonials",
                        "icon": "comment",
                        "link": reverse_lazy("admin:hapl_testimonial_changelist"),
                    },
                    {
                        "title": "Contact Data",
                        "icon": "email",
                        "link": reverse_lazy("admin:hapl_contactdata_changelist"),
                    },
                    {
                        "title": "Contact Groups",
                        "icon": "contacts",
                        "link": reverse_lazy("admin:hapl_contactgroup_changelist"),
                    },
                    {
                        "title": "Social Links",
                        "icon": "share",
                        "link": reverse_lazy("admin:hapl_social_changelist"),
                    },
                    {
                        "title": "Career Positions",
                        "icon": "work",
                        "link": reverse_lazy("admin:hapl_careerposition_changelist"),
                    },
                    {
                        "title": "News Articles",
                        "icon": "newspaper",
                        "link": reverse_lazy("admin:hapl_newsarticle_changelist"),
                    },
                ],
            },
        ],
    },
}
