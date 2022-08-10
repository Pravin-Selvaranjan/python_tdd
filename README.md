# Python_TDD
![tdd](https://user-images.githubusercontent.com/110179866/183909077-95747713-aca5-4c67-ac27-0c1ec1aa7985.jpeg)

- 1. Create precise tests: Developers need to create precise unit tests to verify the functionality of specific features. They must ensure that the test compiles so that it can execute. In most cases, the test is bound to fail. This is a meaningful failure as developers are creating compact tests based on their assumptions of how the feature will behave.


- 2. Correcting the Code: Once a test fails, developers need to make the minimal changes required to correct the code so that it can run successfully when re-executed.


- 3. Refactor the Code: Once the test runs successfully, check for redundancy or any possible code optimizations to enhance overall performance. Ensure that refactoring does not affect the external behavior of the program.

# Benefits
- Fewer bugs and errors
- Higher quality code
- Save costs in the long run 


# SIMPLY

- Run everything backwards, start from basic testing of basic functionality to see if everything is in order
- if receiving errors, correct the errors!
- refactor(rejig) your code with optimisation at the forefront of your mind.


- When creating a file to test make sure it begins with Test_


```

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






Calculator = SimpleCalc()

Calculator.add(5, 6)
Calculator.subtract(10, 5)

print(Calculator.add(5, 7))
print(Calculator.percent_calc(5, 20))
print(Calculator.dob(6, 1993))

# create a function for dob another for %
# another function for cm to m
```

```
from calc import SimpleCalc
import unittest
import pytest



class Calculator_tests(unittest.TestCase):
    calc_obj = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2, 5), 7)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(5, 5), 25)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(10, 2), 5)

    def test_percent(self):
        self.assertEqual(self.calc_obj.percent_calc(5,10), 50)

    def test_dob(self):
        self.assertEqual(self.calc_obj.dob(6, 1993), "6/1993")

```
```
Test_tdd_tests.py::Calculator_tests::test_add PASSED                                                                                                                                                                             [ 16%] 
Test_tdd_tests.py::Calculator_tests::test_divide PASSED                                                                                                                                                                          [ 33%] 
Test_tdd_tests.py::Calculator_tests::test_dob PASSED                                                                                                                                                                             [ 50%] 
Test_tdd_tests.py::Calculator_tests::test_multiply PASSED                                                                                                                                                                        [ 66%] 
Test_tdd_tests.py::Calculator_tests::test_percent PASSED                                                                                                                                                                         [ 83%] 
Test_tdd_tests.py::Calculator_tests::test_subtract PASSED                                                                                                                                                                        [100%] 

========================================================================================================== 6 passed in 0.03s ========================================================================================================== 
PS C:\Users\pvs15\PycharmProjects\python_tdd> 
```

