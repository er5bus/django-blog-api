from rest_framework.reverse import reverse_lazy
from rest_framework import status

from apps.blog.models import Post, Tag
from apps.core.tests import LoggedUserAPITestCase


class TagAPITests(LoggedUserAPITestCase):

    def setUp(self) -> None:
        super(TagAPITests, self).setUp()
        self.tag = Tag(name='new tag')
        self.tag.save()

    def tearDown(self) -> None:
        super(TagAPITests, self).tearDown()
        self.tag.delete()

    def get_tags(self, **kwargs):
        url = reverse_lazy('tag-list')
        return self.client.get(url, kwargs, format='json')

    def get_tag(self, pk, **kwargs):
        url = reverse_lazy('tag-detail', kwargs={'pk': pk})
        return self.client.get(url, kwargs, format='json')

    def post_tag(self, name):
        url = reverse_lazy('tag-list')
        data = {
            "name": name
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_user_with_valid_data(self):
        response = self.post_tag('new tag name')
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_user_with_duplicated_data(self):
        response = self.post_tag('new tag')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_users(self):
        response = self.get_tags()
        assert response.status_code == status.HTTP_200_OK

    def test_get_user_with_valid_pk(self):
        response = self.get_tag(self.tag.pk)
        assert response.status_code == status.HTTP_200_OK

    def test_get_user_with_fake_pk(self):
        response = self.get_tag(111)  # fake pk
        assert response.status_code == status.HTTP_404_NOT_FOUND


class PostAPITests(LoggedUserAPITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.tag = Tag(name='new tag')
        self.tag.save()
        self.post = Post(title='admin', body='admin@gmail.com', author=self.current_user)
        self.post.save()
        self.post.tags.add(self.tag)
        self.post.save()

    def tearDown(self) -> None:
        super().tearDown()
        self.tag.delete()
        self.post.delete()

    def get_posts(self, **kwargs):
        url = reverse_lazy('post-list')
        return self.client.get(url, kwargs, format='json')

    def get_post(self, slug, **kwargs):
        url = reverse_lazy('post-detail', kwargs={'slug': slug})
        return self.client.get(url, kwargs, format='json')

    def post_new_post(self, title, body, tags):
        url = reverse_lazy('post-list')
        data = {
            "title": title,
            "body": body,
            "tags": tags
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_new_post_with_valid_data(self):
        response = self.post_new_post('post title', 'post body', [self.tag.pk])
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_posts(self):
        response = self.get_posts()
        assert response.status_code == status.HTTP_200_OK

    def test_get_post_with_valid_slug(self):
        response = self.get_post(self.post.slug)
        assert response.status_code == status.HTTP_200_OK

    def test_get_post_with_fake_slug(self):
        response = self.get_post('fake-slug')  # fake slug
        assert response.status_code == status.HTTP_404_NOT_FOUND