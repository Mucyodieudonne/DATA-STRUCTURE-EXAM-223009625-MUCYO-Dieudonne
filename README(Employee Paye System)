EMPLOYEE PAYE SYSTEM
This C++ program is a simple payroll system that lets a user enter different pay components (like salary, transport, etc.) for an employee, choose a calculation method (with or without bonus), and then calculates the total pay. Here's a clear explanation of how the system works step by step:

1. Data Structure – PayComponent
Represents one part of the pay (e.g., "Basic Pay", "Allowance").

Contains:

desc[30]: A short name or description of the component.

amount: How much this component is worth in money.

2. Polymorphism – Pay Calculation (OOP concept)
Uses inheritance and virtual functions to allow flexible pay calculations.

Base class: PayCalculator

Has a pure virtual function compute() to force child classes to implement it.

RegularPayCalculator:

Adds all component amounts.

Used for normal pay without extras.

BonusPayCalculator:

Adds all component amounts + 500 bonus.

3. Employee Class – Manages Pay Components
This class keeps a dynamic list of pay components for one employee.

addComponent: Adds a new pay part.

removeComponent: Deletes a component by index.

getComponents: Returns the pointer to the list of components.

getCount: Returns how many components are saved.

Uses new and delete[] to manage memory when components are added/removed.

4. Main Function – Program Flow
Here’s what happens when you run the program:

a. User Inputs
User is asked how many components they want to add.

For each, they type a description and an amount.

These are stored inside the Employee object using addComponent().

b. Choose Calculation Method
The user selects:

1 for Regular pay

2 for Bonus pay

Based on choice, either RegularPayCalculator or BonusPayCalculator is created.

c. Compute and Display
The program calls compute() on the calculator object.

It calculates total pay using the chosen logic.

Final pay is shown on screen.

d. Memory Cleanup
calculator and comps (inside Employee) are cleaned up using delete to avoid memory leaks.

Example
Let’s say you enter:

2 components: "Basic" with 1000, "Transport" with 300

Choose Bonus Pay

Then it will:

Add 1000 + 300 = 1300

Add bonus: 1300 + 500 = 1800

Output: Total Pay: 1800

By Conclusion,
Uses object-oriented programming (inheritance, polymorphism, dynamic memory).

Supports modular, flexible calculation.

Cleanly separates employee data from calculation logic.
