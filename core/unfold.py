from django.templatetags.static import static

UNFOLD_CONFIG = {
    "SITE_TITLE": "Humana Apparels Pvt. Ltd. Admin",
    "SITE_HEADER": "HAPL Admin",
    "SITE_SYMBOL": "public",
    "STYLES": [
        lambda request: static("css/admin.styles.css"),
    ],
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
    },
}
