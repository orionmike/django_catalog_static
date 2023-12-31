# Generated by Django 3.2.19 on 2023-10-16 12:43

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='catalog.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-date_update'],
            },
        ),
        migrations.CreateModel(
            name='ProductMetal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('price', models.IntegerField(blank=True)),
                ('preview_text', models.TextField(blank=True)),
                ('full_text', models.TextField(blank=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('property_metal', models.ManyToManyField(blank=True, related_name='product_list', to='catalog.ProductMetal')),
                ('property_shape', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.productshape')),
                ('tag_list', models.ManyToManyField(blank=True, related_name='product_list', to='catalog.Tag')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-date_update'],
            },
        ),
    ]
