

from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import *

from faker.providers import *

import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        product = Product.objects.all().delete()

        fake = Faker(['ru_RU'])

        tag_list = Tag.objects.all()
        cat_list = Category.objects.all()
        shape_list = ProductShape.objects.all()
        metal_list = ProductMetal.objects.all()
        cat_list_id = []

        for c in list(cat_list):
            cat_list_id.append(c.id)

        shape_list_id = []

        for c in list(shape_list):
            shape_list_id.append(c.id)

        count = 0

        for _ in range(100):

            random_tags = random.sample(list(tag_list), 3)
            random_category = random.sample(cat_list_id, 1)
            random_shape = random.sample(shape_list_id, 1)
            random_metal_list = random.sample(list(metal_list), 2)
            # print(f'random_category: {random_category}')

            price = random.randint(100, 1000)

            product = Product.objects.create(
                # title=fake.sentence(nb_words=3).replace('.', ''),
                title=f'Товар {str(random.randint(0, 999)).zfill(4)}',
                category_id=random_category[0],  # random.randint(40, 50),
                preview_text=fake.paragraph(nb_sentences=2),
                full_text=fake.paragraph(nb_sentences=6),
                price=price,
                product_shape_id=random_shape[0]
            )
            product.tag_list.set(random_tags)
            product.product_metal_list.set(random_metal_list)
            # post.category.set(random_category)

            product.save()
            count += 1

        print(f'Product list genereited: {count}')
