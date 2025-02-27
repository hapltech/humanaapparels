from django.core.management.base import BaseCommand
from seeder.content_seeder import (
    HomeSeeder,
    AboutSeeder,
    CustomerSeeder,
    ContactSeeder,
    CareerSeeder,
    NewsSeeder,
)


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **options):
        HomeSeeder().run()
        AboutSeeder().run()
        CustomerSeeder().run()
        ContactSeeder().run()
        CareerSeeder().run()
        NewsSeeder().run()
        self.stdout.write(self.style.SUCCESS("Data seeding complete!"))
