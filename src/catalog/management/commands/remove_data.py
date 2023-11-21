

from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()
        ProductShape.objects.all().delete()
        ProductMetal.objects.all().delete()
        Tag.objects.all().delete()

        print(f'data remove')
