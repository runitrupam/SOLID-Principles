
'''
2. Open Closed Principle
The Open-Closed Principle states that a class 
should be open for extension but closed for modification. 
This means you should add new functionality by extending classes,
not modifying them.


When Modifying Base Class is Acceptable --> 
Modifying the base class is acceptable in limited scenarios:
	1.	Controlled Environment: If the base class is part of a small, tightly controlled codebase where all usage can be tested and updated simultaneously.
	2.	Bug Fixes: If the modification corrects a bug or adds necessary safeguards without altering the intended behavior.
	3.	Refactoring: When the change simplifies or improves the implementation without affecting its external interface (e.g., keeping the return type the same).

'''

class Inventory:
    def __init__(self, inv):
        self.__inventory = inv
        
    def get_inventory(self): # On modifying this some code which depends on this will break.
        return self.__inventory
    
    def update_inventory(self, new_inv):
        self.__inventory = new_inv
    
    def add_stocks(self, stocks):
        self.__inventory += stocks

class InventoryNew(Inventory):
    def __init__(self, inv, warehouse_name):
        # Call the parent constructor to initialize the inventory.
        super().__init__(inv)
        self.__warehouse_name = warehouse_name  
    
    def get_warehouse_name(self):
        return self.__warehouse_name
    
    def add_stocks_to_warehouse(self, stocks):
        print(f"Adding {stocks} stocks to warehouse '{self.__warehouse_name}'")
        self.add_stocks(stocks)  # Use the parent class method for inventory addition.
ob = InventoryNew(1000, 'Mumbai')   
ob.add_stocks_to_warehouse(200)
print(f"Inventory of warehouse = {ob.get_warehouse_name()} is =",ob.get_inventory())

'''
Output :- 
Adding 200 stocks to warehouse 'Mumbai'
Inventory of warehouse = Mumbai is = 1200
'''
