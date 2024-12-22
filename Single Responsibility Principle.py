'''

SOLID Principles:- 

1. Single Responsibility Principle
-- A class should have only 1 reason for change


Pros of the Single Responsibility Principle (SRP):
	1.	Improved Maintainability: Changes in one functionality of the system do not impact other functionalities since they are encapsulated in different classes or modules.
	2.	Easier Debugging: Since each class handles only one responsibility, it is simpler to identify and fix bugs.
	3.	Reusability: Small, focused classes are easier to reuse in other projects or contexts.
	4.	Better Scalability: Each responsibility can evolve independently, allowing the codebase to scale without creating dependencies.

Cons of the Single Responsibility Principle (SRP):
	1.	Increased Complexity in Small Projects: Dividing responsibilities might lead to many classes, which could be overkill for simple applications.
	2.	Potential Over-Engineering: If SRP is applied too rigidly, it might lead to unnecessary complications with too many small classes or files.

'''

# Violates Single Responsibility Principle
class Restaurant:
    
    def serve_customer():
        print("serving")
        
    def wash_dishes():
        print('Dishes being washed')

# Note if there is a change in the customer's serving 


class Waiter:
    
    def serve_customer():
        print("Waiter serving")
        
    def customer_checkout():
        print('customer are given the Bill to pay.')

class Chef:
    
    def wash_dishes():
        print('Dishes being washed')
        
    def cook_food():
        print('Chef making food.')


