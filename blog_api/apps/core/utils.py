from django.utils.text import slugify

from random import randint


def generate_slug(value, max_length, allow_unicode=False):
    slug = slugify(value, allow_unicode)
    return slug[:max_length]


def generate_unique_slug(model, slug_field_name, slug_field_value):
    while model.objects.filter(**{slug_field_name: slug_field_value}).existe():
        slug_field_value = slug_field_value[:len(slug_field_value) - 4] + randint(1000, 9999)  # add 4 random int

    return slug_field_value