# SOLID Principles in Python

This repository demonstrates examples of the **SOLID** principles using Python. The SOLID principles are a set of design guidelines for creating maintainable, scalable, and robust object-oriented software.

## What are the SOLID Principles?

SOLID is an acronym representing five principles of software design:
1. **S**ingle Responsibility Principle (SRP)
2. **O**pen/Closed Principle (OCP)
3. **L**iskov Substitution Principle (LSP)
4. **I**nterface Segregation Principle (ISP)
5. **D**ependency Inversion Principle (DIP)

---

## Principles Overview

### 1. Single Responsibility Principle (SRP)
**Definition**: A class should have only one reason to change. In other words, a class should only have one responsibility.

#### Pros:
- Improves code readability and maintainability.
- Simplifies debugging by isolating responsibilities.
- Encourages better separation of concerns.

#### Cons:
- May lead to an increase in the number of classes.
- Could require more effort to design upfront.

---

### 2. Open/Closed Principle (OCP)
**Definition**: Software entities (classes, modules, functions) should be open for extension but closed for modification.

#### Pros:
- Reduces the risk of introducing bugs when extending functionality.
- Encourages code reuse and scalability.

#### Cons:
- Can lead to complex hierarchies if overused.
- Requires thoughtful design patterns like inheritance or composition.

---

### 3. Liskov Substitution Principle (LSP)
**Definition**: Subtypes must be substitutable for their base types without altering the correctness of the program.

#### Pros:
- Promotes reliable polymorphism.
- Ensures better compatibility and predictability in OOP design.

#### Cons:
- Violating LSP can cause subtle bugs that are difficult to debug.
- May require additional testing to validate subclass behavior.

---

### 4. Interface Segregation Principle (ISP)
**Definition**: A class should not be forced to implement interfaces it does not use. Instead, create smaller, more specific interfaces.

#### Pros:
- Reduces the burden of implementing unnecessary methods.
- Improves flexibility and clarity in code design.

#### Cons:
- Can lead to an increased number of interfaces.
- Requires more effort in interface design.

---

### 5. Dependency Inversion Principle (DIP)
**Definition**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

#### Pros:
- Decouples high-level and low-level modules for greater flexibility.
- Makes code easier to test by introducing abstractions.

#### Cons:
- Can increase complexity by introducing more abstractions.
- Requires careful planning and design.

---

## Repository Structure

```plaintext
├── README.md          # Overview of SOLID principles
├── SRP                # Examples of Single Responsibility Principle
├── OCP                # Examples of Open/Closed Principle
├── LSP                # Examples of Liskov Substitution Principle
├── ISP                # Examples of Interface Segregation Principle
└── DIP                # Examples of Dependency Inversion Principle
