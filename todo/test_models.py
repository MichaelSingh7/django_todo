from django.test import TestCase
from .models import Item


class TestItemModel(TestCase):
    def test_done_defaults_to_False(self):
        item = Item(name="Create A Test")
        item.save()
        self.assertEqual(item.name, "Create A Test")
        self.assertFalse(item.done)

    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name="Create A Test", done=True)
        item.save()
        self.assertEqual(item.name, "Create A Test")
        self.assertTrue(item.done)
