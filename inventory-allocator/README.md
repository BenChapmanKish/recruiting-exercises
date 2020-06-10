## Ben's solution

To solve this problem, I used Python 3. The implementation and tests are fully-documented and well-commented, but I've provided a high-level overview of my approach here.

### Implementation

I implemented the InventoryAllocator class, and the method to solve the problem is `ship(order, warehouse_inventories)`.

The approach I took is to iterate over each item in the order, and search through the list of warehouse inventories in increasing order of cost. Until the requested item quantity is met, I keep track of which warehouses have some amount of the item, and how many of this item needs to be shipped from this warehouse.

If we have enough of every item across our warehouses to fulfill the entire order, then the output of the method is a list of warehouses and the amounts of each item that will be shipped from them.

If we have enough inventory to ship some items in the order but not others, the behaviour of the `ship` method depends on a flag `_SHIP_PARTIAL_ORDERS` which *you* can change if you want to try different functionality.

### Unit tests

I wrote 10 comprehensive unit tests which cover various cases, including:

* The output of `ship` is in the proper format
* An order can be fulfilled if there are exactly enough of any of its items in a warehouse
* If multiple warehouses can completely or partially ship an item, the cheapest ones possible will be used
* An order will be split across warehouses if that is the only way to completely ship an item
* Cheaper warehouses that don't contain any ordered items won't be included in the output
* When there is more than enough of an item to complete the order, only the requested amount will be shipped
* No order will be shipped if there isn't enough inventory for an item to fulfill it, even across every warehouse
* If some items can be shipped in the requested quantity but others cannot, the method will behave depending on the setting for `_SHIP_PARTIAL_ORDERS`

### Documentation and running tests

To read documentation for either the implementation or the tests, run `pydoc ./InventoryAllocator.py` or `pydoc ./test_InventoryAllocator.py`

To run the unit tests, run `python3 test_InventoryAllocator.py`



&nbsp;

Below is the original problem description.

-----

### Problem

The problem is compute the best way an order can be shipped (called shipments) given inventory across a set of warehouses (called inventory distribution). 

Your task is to implement InventoryAllocator class to produce the cheapest shipment.

The first input will be an order: a map of items that are being ordered and how many of them are ordered. For example an order of apples, bananas and oranges of 5 units each will be 

`{ apple: 5, banana: 5, orange: 5 }`

The second input will be a list of object with warehouse name and inventory amounts (inventory distribution) for these items. For example the inventory across two warehouses called owd and dm for apples, bananas and oranges could look like

`[ 
    {
    	name: owd,
    	inventory: { apple: 5, orange: 10 }
    }, 
    {
    	name: dm:,
    	inventory: { banana: 5, orange: 10 } 
    }
]`

You can assume that the list of warehouses is pre-sorted based on cost. The first warehouse will be less expensive to ship from than the second warehouse. 

You can use any language of your choice to write the solution (internally we use Typescript/Javascript, Python, and some Java). Please write unit tests with your code, a few are mentioned below, but these are not comprehensive. Fork the repository and put your solution inside of the src directory and include a way to run your tests!

### Examples

*Happy Case, exact inventory match!**

Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]`  
Output: `[{ owd: { apple: 1 } }]`

*Not enough inventory -> no allocations!*

Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]`  
Output: `[]`

*Should split an item across warehouses if that is the only way to completely ship an item:*

Input: `{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]`  
Output: `[{ dm: { apple: 5 }}, { owd: { apple: 5 } }]`

### What are we looking for

We'll evaluate your code via the following guidelines in no particular order:

1. **Readability**: naming, spacing, consistency
2. **Correctness**: is the solution correct and does it solve the problem
1. **Test Code Quality**: Is the test code comperehensive and covering all cases.
1. **Tool/Language mastery**: is the code using up to date syntax and techniques. 

