
'''
4. Interface Segregation Principle
The Interface Segregation Principle states that a class should not be forced to implement interfaces it does not use. 
Instead, you should break down large, monolithic interfaces into smaller,
more specific ones so that classes only need to implement the methods relevant to them.

Benefits of ISP:
	1.	Improved Maintainability: Smaller interfaces are easier to understand and modify.
	2.	Better Reusability: Classes can pick and choose which interfaces to implement, improving flexibility.
	3.	Reduced Unnecessary Dependencies: Classes are not burdened with methods they don’t need.

Cons:- 
1.	Overhead in Managing Interfaces: Splitting interfaces adds unnecessary complexity in simple systems.
	2.	Lack of Reusability: Strict separation can lead to duplication of shared functionality.
	3.	Difficult to Extend: Adding new vehicle types may require significant refactoring.
	4.	Increased Boilerplate Code: More interfaces and classes lead to a bloated codebase.
	5.	Over-Specialization: Excessive segregation can make the design rigid and less flexible.

'''
print("ISP Violation -->")
class Vehicle:
    def get_petrol_capacity(self):
        pass

class Car(Vehicle):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def get_petrol_capacity(self):
        print(f"Petrol Tank Capacity = {self.capacity} liters")

class EVCar(Vehicle):
    def __init__(self, name):
        self.name = name

    def get_petrol_capacity(self):
        raise NotImplementedError("EVs don't use petrol")

# Violation Example
car = Car("Sedan", 50)
car.get_petrol_capacity()

ev_car = EVCar("Tesla Model 3")
try:
    ev_car.get_petrol_capacity()
except NotImplementedError as e:
    print(e)

print("\nISP Follow -->")
class PetrolVehicle:
    def get_petrol_capacity(self):
        pass

class ElectricVehicle:
    def get_battery_capacity(self):
        pass

class Car(PetrolVehicle):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def get_petrol_capacity(self):
        print(f"Petrol Tank Capacity = {self.capacity} liters")

class EVCar(ElectricVehicle):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get_battery_capacity(self):
        print(f"Battery Capacity = {self.capacity} kWh")

# Following ISP Example
car = Car("Sedan", 50)
car.get_petrol_capacity()

ev_car = EVCar("Tesla Model 3", 75)
ev_car.get_battery_capacity()


'''
Output:--
ISP Violation -->
Petrol Tank Capacity = 50 liters
EVs don't use petrol

ISP Follow -->
Petrol Tank Capacity = 50 liters
Battery Capacity = 75 kWh

'''
