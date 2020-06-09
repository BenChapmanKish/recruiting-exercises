#!/usr/bin/env python3
# Ben Chapman-Kish June 2020
# Deliverr recruiting exercise: inventory allocator
# https://github.com/deliverr/recruiting-exercises/tree/master/inventory-allocator

"""
Inventory Allocator static class.
Contains one static method ship(), which fulfills the requirements of the exercise.
"""
class InventoryAllocator():
    """
    Determines the best shipments for the order `order`, given the inventory `inventory`.
    Inventory may be spread across any number of warehouses, which are given in increasing order of cost.
    Returns a list of maps with the warehouse name as keys. The values are also maps of items to the
    amount being shipped from this warehouse.
    """
    def ship(order, inventory):
        item_distribution = {}
        
        # Iterate over every item and its requested quantity
        for item, quantity in order.items():
            remaining = quantity

            tentative_item_distribution = {}

            # Iterate over warehouses from cheapest to most expensive
            for wh in inventory:
                wh_name = wh["name"]
                wh_inv = wh["inventory"]

                if item not in wh_inv:
                    continue

                wh_stock = wh_inv[item]

                if remaining <= wh_stock:
                    tentative_item_distribution[wh_name] = remaining
                    remaining = 0
                    break

                elif remaining > wh_stock:
                    tentative_item_distribution[wh_name] = wh_stock
                    remaining -= wh_stock

            # If we have enough to fulfill order, lower warehouse stock accordingly
            # Otherwise, nothing happens and none of the item is shipped
            if remaining == 0:
                for wh_name, item_quantity in tentative_item_distribution.items():

                    # If the warehouse isn't shipping anything yet, create its order
                    if wh_name not in item_distribution:
                        item_distribution[wh_name] = {}

                    item_distribution[wh_name][item] = item_quantity

        # Convert our map to a list, as specified in problem description
        output = []
        for wh_name, items in item_distribution.items():
            output.append( { wh_name: items } )

        return output

