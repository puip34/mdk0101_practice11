# Пример реализации паттерна Фабрика
class Product:
    def __init__(self, name):
        self.name = name

    def operate(self):
        pass


class ConcreteProductA(Product):
    def operate(self):
        print(f"Operating {self.name} of type A")


class ConcreteProductB(Product):
    def operate(self):
        print(f"Operating {self.name} of type B")


class Factory:
    def create_product(self, product_type, name):
        if product_type == "A":
            return ConcreteProductA(name)
        elif product_type == "B":
            return ConcreteProductB(name)
        else:
            raise ValueError("Invalid product type")


# Пример реализации паттерна Абстрактная фабрика
class AbstractProductA:
    def operate(self):
        pass


class AbstractProductB:
    def operate(self):
        pass


class ConcreteProductAX(AbstractProductA):
    def operate(self):
        print("Operating ProductAX")


class ConcreteProductAY(AbstractProductA):
    def operate(self):
        print("Operating ProductAY")


class ConcreteProductBX(AbstractProductB):
    def operate(self):
        print("Operating ProductBX")


class ConcreteProductBY(AbstractProductB):
    def operate(self):
        print("Operating ProductBY")


class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactoryX(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductAX()

    def create_product_b(self):
        return ConcreteProductBX()


class ConcreteFactoryY(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductAY()

    def create_product_b(self):
        return ConcreteProductBY()


# Пример реализации паттерна Строитель
class ProductBuilder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_product(self):
        pass


class ConcreteProductBuilder(ProductBuilder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("PartA")

    def build_part_b(self):
        self.product.add_part("PartB")

    def build_part_c(self):
        self.product.add_part("PartC")

    def get_product(self):
        return self.product


# Пример реализации паттерна Наблюдатель
class Observer:
    def update(self, subject):
        pass


class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"Observer received update from {subject}")


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)


# Пример реализации паттерна Стратегия
class Strategy:
    def execute(self):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing strategy A")


class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing strategy B")


# Пример реализации паттерна Декоратор
class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        print("Executing operation in ConcreteComponent")


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()


class ConcreteDecorator(Decorator):
    def operation(self):
        super().operation()
        print("Additional operation in ConcreteDecorator")


# Пример реализации паттерна Фасад
class SubsystemA:
    def operation_a(self):
        print("SubsystemA operation")


class SubsystemB:
    def operation_b(self):
        print("SubsystemB operation")


class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def operation(self):
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()


def main():
    # Использование паттерна Фабрика
    factory = Factory()
    product_a = factory.create_product("A", "ProductA")
    product_a.operate()

    # Использование паттерна Абстрактная фабрика
    factory_x = ConcreteFactoryX()
    product_ax = factory_x.create_product_a()
    product_ax.operate()

    # Использование паттерна Строитель
    builder = ConcreteProductBuilder()
    builder.build_part_a()
    builder.build_part_b()
    builder.build_part_c()
    product = builder.get_product()
    product.list_parts()

    # Использование паттерна Наблюдатель
    subject = Subject()
    observer = ConcreteObserver()
    subject.attach(observer)
    subject.notify()

    # Использование паттерна Стратегия
    strategy_a = ConcreteStrategyA()
    strategy_b = ConcreteStrategyB()

    strategy_a.execute()
    strategy_b.execute()

    # Использование паттерна Декоратор
    component = ConcreteComponent()
    decorator = ConcreteDecorator(component)
    decorator.operation()

    # Использование паттерна Фасад
    facade = Facade()
    facade.operation()


if __name__ == "__main__":
    main()
