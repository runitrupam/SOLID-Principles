
'''
3. Liskov Substitution Principle
Two classes follows LSP , if on the changing the object of class1 with the object of another class
the functionality doesn't break 
Pros of Liskov Substitution Principle (LSP):
	Improved Code Reusability:- Subclasses can be swapped
	Code Maintainability :- Changes to a superclass or one subclass don’t break other subclasses or the overall application logic.
    Clear/Fix Design :-  Enforces a consistent interface for all subclasses
    
Cons of Liskov Substitution Principle (LSP):
    Rigid Structure: Fixed Interface Str.
    Potential Overhead:
	    •	Forcing behaviors like “start_engine” in a Bicycle (which doesn’t have an engine) might introduce unnecessary methods, 
	    even if they are no-ops or return a default message.

When Not to Prioritize LSP:
	•	In small-scale, less complex systems where rigid adherence might introduce unnecessary abstraction.
	•	For classes with very distinct behaviors that don’t share common functionality,
	    where composition or other patterns might be better suited.

'''
# Violates the LSP
class Car:
    def start_engine(self):
        return 'Enigne Started of Car'

class Bicycle:
    def get_no_of_gear(self):
        return 5

ob = Car()
print(ob.start_engine())

# Now if you replace the object initialization of Car to use Bicycle 
ob = Bicycle()
#print(ob.start_engine()) # Run Time Error : AttributeError: 'Bicycle' object has no attribute 'start_engine'
print()
## LSP code
print('LSP code --> ')

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def get_no_of_wheels(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Engine Started"

    def get_no_of_wheels(self):
        return 4


class Bicycle(Vehicle):
    def start_engine(self):
        # Bicycles don't have an engine
        return "Bicycles don't have engines."

    def get_no_of_wheels(self):
        return 2


# Using the Vehicle type with different subclasses
vehicles = [Car(), Bicycle()]
# # Now if you replace the object initialization of Car to use Bicycle 
for vehicle in vehicles:
    print(f"Vehicle Type: {vehicle.__class__.__name__}")
    print(f"Engine Status: {vehicle.start_engine()}")
    print(f"No. of Wheels: {vehicle.get_no_of_wheels()}")
    print()
