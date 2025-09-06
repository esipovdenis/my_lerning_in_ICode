# Напишите класс Calculator со следующими методами:
# add(a,b) +
# subtract(a,b) -
# multiply(a,b) *
# divide(a,b) (проверка деления на ноль) /

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return  a - b

    def multiply (self, a, b):
        return a * b

    def divide (self, a, b):
        if b == 0:
            return "Нельзя делить на ноль"
        else:
            return a / b

calc = Calculator()

result = calc.add(3, 5)
print(f"Результат слагаемых: {result}")

result = calc.subtract(6, 3)
print(f'Результат производных: {result} ')

result = calc.multiply(2, 7)
print(f'Результат произведения: {result} ')

result = calc.divide(14, 7)
print(f'Результат частное: {result} ')
