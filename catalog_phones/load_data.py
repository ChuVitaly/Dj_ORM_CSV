import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Apps.settings')
django.setup()
import csv
from datetime import datetime
from django.utils.text import slugify
from catalog_phones.models import Phone

with open('phones.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        phone = Phone()
        phone.name = row['name']
        phone.price = float(row['price'])
        phone.image = row['image']
        phone.release_date = datetime.strptime(row['release_date'], '%Y-%m-%d')
        phone.lte_exists = row['lte_exists'].lower() == 'true'
        phone.slug = slugify(phone.name)
        phone.save()