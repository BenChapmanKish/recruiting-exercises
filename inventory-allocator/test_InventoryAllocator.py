#!/usr/bin/env python3

import unittest
from InventoryAllocator import InventoryAllocator as allocator

"""
Static unit test class to test InventoryAllocator.ship
"""
class test_InventoryAllocator(unittest.TestCase):

    """
    Given the warehouse dictionary of an output `warehouse`, returns its name.
    """
    def _get_warehouse_name(self, warehouse):
        # Assuming well-formed output, the name should be the only key in the dict. 
        # Save on space and use iterator to get this rather than converting to a list.
        name = next( iter( warehouse.keys() ) )
        return name

    """
    Searches for a warehouse in `warehouses` with the name `wh_name`.
    Returns the warehouse object, or None if there is no match.
    """
    def _find_warehouse_in_list_by_name(self, wh_name, warehouses):
        for warehouse in warehouses:
            other_name = self._get_warehouse_name(warehouse)
            if wh_name == other_name:
                return warehouse
            
        return None

    """
    Compares two shipments `expected` and `output`.
    Returns True if the shipments are equivalent, otherwise False.
    """
    def compare_shipments(self, expected, output):
        # Compare lengths of shipments
        if len(expected) != len(output):
            return False

        # Compare the warehouses between the two shipments
        for wh_exp in expected:
            wh_name = self._get_warehouse_name(wh_exp)

            # Check that expected warehouse exists in output
            wh_out = self._find_warehouse_in_list_by_name(wh_name, output)
            if wh_out == None:
                return False

            # Check that the warehouses contain the same items
            exp_items = wh_exp[wh_name]
            out_items = wh_out[wh_name]

            if exp_items.keys() != out_items.keys():
                return False
            
            # Compare item inventories
            for item, exp_inv in exp_items.items():
                out_inv = out_items[item]
                if exp_inv != out_inv:
                    return False

        # All comparisons are done and the shipments should be equivalent.
        return True

    """
    Tests that InventoryAllocator.ship can produce a well-formed output.
    """
    def test_output_should_be_well_formed(self):
        order = { "apple": 1 }
        inventory = [{ "name": "owd", "inventory": { "apple": 1 } }]
        output = allocator.ship(order, inventory)

        self.assertIsInstance(output, list)
        self.assertEqual(len(output), 1)

        self.assertIsInstance(output[0], dict)
        self.assertEqual(len(output[0]), 1)
        self.assertIn("owd", output[0])

        self.assertIsInstance(output[0]["owd"], dict)
        self.assertEqual(len(output[0]["owd"]), 1)
        self.assertIn("apple", output[0]["owd"])

        self.assertIsInstance(output[0]["owd"]["apple"], int)
        self.assertEqual(output[0]["owd"]["apple"], 1)



    def test_exact_match(self):
        order = { "apple": 1 }
        inventory = [{ "name": "owd", "inventory": { "apple": 1 } }]
        expected = [{ "owd": { "apple": 1 } }]

        output = allocator.ship(order, inventory)
        self.assertTrue(self.compare_shipments(expected, output))

    def test_insufficient_inventory(self):
        order = { "apple": 1 }
        inventory = [{ "name": "owd", "inventory": { "apple": 0 } }]
        expected = []

        output = allocator.ship(order, inventory)
        self.assertTrue(self.compare_shipments(expected, output))

    def test_split_across_warehouses(self):
        order = {"apple": 10}
        inventory = [
            { "name": "owd", "inventory": { "apple": 5 } },
            { "name": "dm",  "inventory": { "apple": 5 } }
        ]
        expected = [{ "dm": { "apple": 5 } }, { "owd": { "apple": 5 } }]

        output = allocator.ship(order, inventory)
        self.assertTrue(self.compare_shipments(expected, output))


if __name__ == '__main__':
    unittest.main()

