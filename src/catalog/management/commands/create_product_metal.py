

from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import *

from faker.providers import *

import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker(['ru_RU'])

        count = 0

        for _ in range(5):

            product_metal = ProductMetal.objects.create(title=fake.sentence(nb_words=1).replace('.', ''))
            product_metal.save()

            count += 1

        print(f'Product metal genereited: {count}')
