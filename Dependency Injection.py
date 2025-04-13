
'''
5. Dependency Injection
Dependency Injection (DI) is a design pattern where an object (or class) 
receives its dependencies from an external source rather than creating them internally.

Benefits of Dependency Injection:
	1.	Flexibility: You can use different Warehouse objects without modifying the Inventory class.
	2.	Testability: You can easily replace the Warehouse instance with a mock or test object.
	3.	Loose Coupling: The Inventory class is not tightly bound to the Warehouse class, 
	    allowing for easier future changes.
     4. It allows to test your code easily, as you are passing an object.
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


# Example 2:- 
# ✅ Without Dependency Injection (Tightly Coupled):
# In this version, NotificationManager is tightly coupled with EmailService. 
# If we want to switch to SMSService, we need to change the code.
class EmailService:
    def send(self, message):
        print(f"Sending Email with message: {message}")

class NotificationManager:
    def __init__(self):
        self.email_service = EmailService()  # tightly coupled

    def notify(self, message):
        self.email_service.send(message)

notifier = NotificationManager()
notifier.notify("Hello, User!")


# ✅ With Dependency Injection (Loosely Coupled):

from abc import ABC, abstractmethod

# Step 1: Define an abstraction
class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Step 2: Implement different services
class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

# Step 3: Inject dependency
class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        self.service.send(message)

# Injecting EmailService
email_notifier = NotificationManager(EmailService()) # Object is passed . 
email_notifier.notify("Welcome via Email!")

# Injecting SMSService
sms_notifier = NotificationManager(SMSService())
sms_notifier.notify("Welcome via SMS!")
