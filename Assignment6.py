import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read the JSON file
with open('employees.json', 'r') as f:
    data = json.load(f)

# Create a list of Employee objects
employees = []
for emp in data['employees']:
    employees.append(Employee(emp['Name'], emp['DOB'], emp['Height'], emp['City'], emp['State']))

# Print the list of Employee objects
for emp in employees:
    print(f"Name: {emp.name}, DOB: {emp.dob}, Height: {emp.height}, City: {emp.city}, State: {emp.state}")

