from math import *


class CalculatorModel:
    def __init__(self):
        self.expression = ""
        self.history = []

    def update_expression(self, key):
        if key == "DEL":
            self.handle_del()
        elif key == "CLR":
            self.handle_clear()
        else:
            self.expression += key

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            return str(result)
        except Exception as e:
            return "Error"


    def handle_del(self):
        if self.expression.endswith('sqrt('):
            self.expression = self.expression[:-5]
        elif self.expression.endswith('log2('):
            self.expression = self.expression[:-5]
        elif self.expression.endswith('log10('):
            self.expression = self.expression[:-6]
        elif self.expression.endswith('**'):
            self.expression = self.expression[:-2]
        elif len(self.expression) > 0:
            self.expression = self.expression[:-1]

    def handle_clear(self):
        self.expression = ""

    def save_history(self):
        result = self.evaluate_expression()
        if result != "Error":
            self.history.append(f"{self.expression} = {result}")
            self.expression = ""