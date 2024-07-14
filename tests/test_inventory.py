# tests/test_inventory.py
import unittest
from inventory import add_inventory_item, get_all_inventory_items, setup_database, engine, Base

class TestInventory(unittest.TestCase):
    def setUp(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def test_add_inventory_item(self):
        item = add_inventory_item("Product A", "Category 1", 100, 50)
        self.assertEqual(item.name, "Product A")
        self.assertEqual(item.category, "Category 1")
        self.assertEqual(item.stock, 100)
        self.assertEqual(item.reorder, 50)

    def test_get_all_inventory_items(self):
        add_inventory_item("Product A", "Category 1", 100, 50)
        items = get_all_inventory_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].name, "Product A")

if __name__ == '__main__':
    unittest.main()

