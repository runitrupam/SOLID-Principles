
'''
5. Dependency Injection
Dependency Injection (DI) is a design pattern where an object (or class) 
receives its dependencies from an external source rather than creating them internally.

Benefits of Dependency Injection:
	1.	Flexibility: You can use different Warehouse objects without modifying the Inventory class.
	2.	Testability: You can easily replace the Warehouse instance with a mock or test object.
	3.	Loose Coupling: The Inventory class is not tightly bound to the Warehouse class, 
	    allowing for easier future changes.
When Not to Use Dependency Injection
	•	For small or simple scripts with minimal dependencies.
	•	In performance-critical code where the overhead of DI is not acceptable.
	•	When a project has limited scope and does not require testability or modularity.	
	
'''
print('Dependency Injection -->>')
class Warehouse:
    def __init__(self, warehouse_name : str):
        self._name = warehouse_name

class Inventory:
    def __init__(self, warehouse : Warehouse, inv : int):
        self.__wh = warehouse
        self.__inventory = inv
    
    def get_inventory(self):
        print(f"The Inventory of warehouse : {self.__wh._name} is {self.__inventory}")

# Proper use of dependency injection with real and test warehouses
real_warehouse = Warehouse('Mumbai')
real_inventory = Inventory(real_warehouse, 500)
real_inventory.get_inventory()

test_warehouse = Warehouse('TestWH')
test_inventory = Inventory(test_warehouse, 300)
test_inventory.get_inventory()


'''
Output:-
Dependency Injection -->>
The Inventory of warehouse : Mumbai is 500
The Inventory of warehouse : TestWH is 300

'''
