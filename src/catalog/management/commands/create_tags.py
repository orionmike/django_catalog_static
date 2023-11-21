

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

            tag = Tag.objects.create(title=fake.sentence(nb_words=1).replace('.', ''))
            tag.save()

            count += 1

        print(f'Tags genereited: {count}')
