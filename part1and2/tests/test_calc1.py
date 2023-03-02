from unittest import TestCase

from part1and2.calc1 import Interpreter


# from part1and2.calc1 import Interpreter
class CalcTest(TestCase):

    def test_interpreter(self):
        result = Interpreter('   3    +     2').expr()
        self.assertEquals(result, 5)

    def test_interpreter_minus(self):
        result = Interpreter('   200    -     2').expr()
        self.assertEquals(result, 198)

    def test_interpreter_multidigits_number(self):
        result = Interpreter('   198    +     2').expr()
        self.assertEquals(result, 200)

    def test_interpreter_not_support_more_then_two_numbers(self):
        result = Interpreter(' 18 + 2 + 2').expr()
        self.assertEquals(result, 20)
