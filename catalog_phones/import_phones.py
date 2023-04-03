import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from catalog_phones.models import Phone


class ImportPhoneCommand(BaseCommand):
    help = 'Import phones from csv file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
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