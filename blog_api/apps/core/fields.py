from django.db import models
from .utils import generate_slug, generate_unique_slug


class AutoSlugField(models.SlugField):

    def __init__(self, *args, populate_from=None, max_length=100, db_index=True, allow_unicode=False, **kwargs):
        super().__init__(*args, max_length=max_length, db_index=db_index, allow_unicode=allow_unicode, **kwargs)
        self.populate_from = populate_from

    def get_populate_from_value(self, model_instance):
        """Return the values of the populate field's."""
        # print(self.populate_from)
        # assert not self.populate_from, "missing 'populate_from' argument"

        if isinstance(self.populate_from, str):
            return getattr(model_instance, self.populate_from)

        if isinstance(self.populate_from, list) or isinstance(self.populate_from, tuple):
            value = ""
            for populate_from_attr in self.populate_from:
                value += getattr(model_instance, populate_from_attr, "")
            return value

        raise TypeError("'populate_from' must be str or list[str] or tuple[str], found `%s`" % self.populate_from)

    def pre_save(self, model_instance, add):
        """Return field's value just before saving."""

        populate_from_value = self.get_populate_from_value(model_instance)
        slug_value = getattr(model_instance, self.attname, None)
        generated_slug = None

        if populate_from_value:
            generated_slug = generate_slug(populate_from_value, self.max_length, self.allow_unicode)

        if self.unique and slug_value != generated_slug:
            generated_slug = generate_unique_slug(self.model, self.attname, generated_slug)

        return slug_value if slug_value != generated_slug else generated_slug

    def formfield(self, **kwargs):
        return None