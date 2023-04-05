import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from catalog_phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from csv file'
    def add_arguments(self, parser):
        parser.add_argument('phones.csv', type=str, help='CSV file path for import')

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                phone = Phone()
                phone.name = row['name']
                phone.price = float(row['price'])
                phone.image = row['image']
                phone.release_date = datetime.strptime(row['release_date'], '%Y-%m-%d')
                phone.lte_exists = row['lte_exists'].lower() == 'true'
                phone.slug = slugify(phone.name)
                phone.save()
        self.stdout.write(self.style.SUCCESS('Phones were imported successfully'))