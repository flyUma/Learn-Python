# In this code, we have three classes: Customer, Order, and Product. 
# Customer has an add_order method which adds an Order object to its orders list. 
# Order has a get_total method which calculates the total price of the products in the order. 
# Product has a name and price attribute.
# This code could be used in a production-level e-commerce application to manage customers, orders, and products. 
# By using classes, the code is organized, reusable, and easy to maintain.

# 이 코드에는 Customer, Order 및 Product의 세 가지 클래스가 있습니다. 
# Customer에는 orders 목록에 Order 개체를 추가하는 add_order 메서드가 있습니다. 
# Order에는 주문한 제품의 총 가격을 계산하는 get_total 메소드가 있습니다. 
# 제품에는 이름 및 가격 속성이 있습니다.
# 이 코드는 생산 수준의 전자 상거래 애플리케이션에서 고객, 주문 및 제품을 관리하는 데 사용할 수 있습니다. 
# 클래스를 사용하면 코드가 체계화되고 재사용 가능하며 유지 관리가 쉽습니다.

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

class Order:
    def __init__(self, order_number, products):
        self.order_number = order_number
        self.products = products

    def get_total(self):
        return sum([product.price for product in self.products])

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# In this code, we have three classes: Employee, Manager, and Developer. 
# Manager and Developer inherit from the Employee class, and each has its own implementation of the get_salary method.
# Manager adds a bonus attribute to its __init__ method, and overrides the get_salary method to include the bonus in the calculation. 
# Developer adds a language attribute to its __init__ method, and overrides the get_salary method to add a $5000 bonus if the developer's language is Python.
# This code could be used in a production-level payroll application to manage employees' salaries. By using classes and inheritance, the code is organized, extensible, and easy to maintain.

# 이 코드에는 Employee, Manager 및 Developer의 세 가지 클래스가 있습니다. 
# Manager 및 Developer는 Employee 클래스에서 상속되며 각각 고유한 get_salary 메서드 구현이 있습니다.
# Manager는 __init__ 메서드에 bonus 속성을 추가하고 계산에 보너스를 포함하도록 get_salary 메서드를 재정의합니다. 
# Developer는 __init__ 메서드에 language 속성을 추가하고 개발자의 언어가 Python인 경우 get_salary 메서드를 재정의하여 $5000 보너스를 추가합니다.
# 이 코드는 생산 수준의 급여 애플리케이션에서 직원의 급여를 관리하는 데 사용할 수 있습니다. 
# 클래스와 상속을 사용하면 코드가 체계화되고 확장 가능하며 유지 관리가 쉽습니다.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_salary(self):
        if self.language == 'Python':
            return self.salary + 5000
        else:
            return self.salary
        
# In this code, we have a Zoo class that has the methods to add, remove and show animals. 
# We also have an Animal class that defines the attributes of each animal. 
# The Zoo class uses the Animal class to add and remove animals from the list of animals in the zoo. 
# The code demonstrates how classes can be used to create complex data structures and how to use them to interact with the data.

# 이 코드에는 동물을 추가, 제거 및 표시하는 메서드가 있는 Zoo 클래스가 있습니다. 
# 또한 각 동물의 속성을 정의하는 Animal 클래스도 있습니다. 
# Zoo 클래스는 Animal 클래스를 사용하여 동물원의 동물 목록에서 동물을 추가하고 제거합니다. 
# 이 코드는 클래스를 사용하여 복잡한 데이터 구조를 만드는 방법과 클래스를 사용하여 데이터와 상호 작용하는 방법을 보여줍니다.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
        else:
            print(f"{animal.name} is already in the zoo.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print(f"{animal.name} is not in the zoo.")

    def show_animals(self):
        for animal in self.animals:
            print(animal)

zoo = Zoo()

lion = Animal("Simba", "Lion")
tiger = Animal("Rajah", "Tiger")
zebra = Animal("Marty", "Zebra")

zoo.add_animal(lion)
zoo.add_animal(tiger)
zoo.add_animal(zebra)

zoo.show_animals()

zoo.remove_animal(tiger)

zoo.show_animals()