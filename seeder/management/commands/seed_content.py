import logging
from django.core.management.base import BaseCommand
from seeder.content_seeder import (
    HomeSeeder,
    AboutSeeder,
    CustomerSeeder,
    ContactSeeder,
    CareerSeeder,
    NewsSeeder,
)


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clean",
            action="store_true",
            help="Delete existing data before seeding",
        )

    def handle(self, *args, **options):
        clean = options["clean"]

        logger.info("🚀 Starting data seeding...")

        HomeSeeder(clean=clean).run()
        AboutSeeder(clean=clean).run()
        CustomerSeeder(clean=clean).run()
        ContactSeeder(clean=clean).run()
        CareerSeeder(clean=clean).run()
        NewsSeeder(clean=clean).run()

        logger.info("🎉 Data seeding complete!")
