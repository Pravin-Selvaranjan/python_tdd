class SimpleCalc:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a/b

    def percent_calc(self, a, b):
        divide = a/b
        return divide * 100

    def dob(self,a, b):
        return (f"{a}/{b}")

    def cm_to_m(self, a):
        return a/100







Calculator = SimpleCalc()

Calculator.add(5, 6)
Calculator.subtract(10, 5)

print(Calculator.add(5, 7))
print(Calculator.percent_calc(5, 20))
print(Calculator.dob(6, 1993))
print(Calculator.cm_to_m(1000))


# create a function for dob another for %
# another function for cm to m
