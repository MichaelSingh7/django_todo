from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item


class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")

    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_item_page(self):
        item = Item(name='Create A Test')
        item.save()

        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_test_edit_page_for_item_that_doesnt_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)

    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create A Test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
