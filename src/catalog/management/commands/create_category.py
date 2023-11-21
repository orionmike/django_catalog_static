

from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import *

from faker.providers import *

import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker(['ru_RU'])
        # fake.add_provider(Provider)

        count = 0

        for _ in range(5):

            cat = Category.objects.create(title=fake.sentence(nb_words=2).replace('.', ''))
            cat.parent = None
            cat.save()
            count += 1

        print(f'Category genereited: {count}')
