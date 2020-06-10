#!/usr/bin/env python3
# Ben Chapman-Kish - June 2020
# Deliverr recruiting exercise: inventory allocator
# https://github.com/deliverr/recruiting-exercises/tree/master/inventory-allocator

from collections import defaultdict

"""
Inventory Allocator static class
Contains the class method ship(), which fulfills the requirements of the exercise.

Note: the exercise description does not specify what behaviour to implement if an order
can only be partially fulfilled - that is, if some items can be shipped in the requested
quantity but other items cannot.
I've included a boolean flag `_SHIP_PARTIAL_ORDERS` which you can change to modify this
behaviour if you so desire, and its default is False.
"""
class InventoryAllocator():
    _SHIP_PARTIAL_ORDERS = False

    """
    Returns a boolean indicating if partial orders should be shipped or not.
    """
    @classmethod
    def shouldShipPartialOrders(cls):
        return cls._SHIP_PARTIAL_ORDERS

    """
    Determines the best shipment for the order `order`, given a list of inventories
    `warehouse_inventories` representing various warehouses.
    Item inventory may be spread across any number of warehouses, which are provided in
    increasing order of cost.
    Returns a list of maps with the warehouse name as keys. The values are also maps of
    items to the amount being shipped from this warehouse.    
    """
    @classmethod
    def ship(cls, order, warehouse_inventories):
        # Store a map of warehouses to the map of item-quantities they will ship
        item_distribution = defaultdict( lambda: {} )
        

        # Iterate over every item-quantity pair in the order
        for item, quantity_remaining in order.items():
            # Store a map of warehouses to the quantity of item that they will ship
            warehouses_for_item = {}


            # Iterate over warehouses from cheapest to most expensive
            for warehouse in warehouse_inventories:
                warehouse_name = warehouse["name"]
                warehouse_inv = warehouse["inventory"]

                # Skip this warehouse if it doesn't contain any of `item`
                if item not in warehouse_inv or warehouse_inv[item] < 1:
                    continue


                item_stock = warehouse_inv[item]

                # If there is at least enough stock to finish the order with this
                # warehouse, break out of the loop
                if quantity_remaining <= item_stock:
                    warehouses_for_item[warehouse_name] = quantity_remaining
                    quantity_remaining = 0
                    break

                # If the warehouse has some of `item` but not enough to complete
                # the order, take all of its item inventory and look in more warehouses
                elif quantity_remaining > item_stock:
                    warehouses_for_item[warehouse_name] = item_stock
                    quantity_remaining -= item_stock


            # If we don't have enough of item to fulfill the order, our behaviour
            # depends on the flag `_SHIP_PARTIAL_ORDERS`. If True, we ship none of this
            # item and move on to the next. If False, the entire order is cancelled and
            # we ship no items (even ones that we have enough of!)
            if quantity_remaining > 0:
                if cls.shouldShipPartialOrders():
                    continue
                else:
                    return []

            # Otherwise, add the item quantities per warehouse to our map of warehouses
            for warehouse_name, item_quantity in warehouses_for_item.items():
                item_distribution[warehouse_name][item] = item_quantity


        # Convert our map to a list of one-key maps, as indicated in problem description
        output = [ { name: items } for name, items in item_distribution.items() ]
        return output
