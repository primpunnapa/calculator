"""Model for calculator"""
from math import *


class CalculatorModel:
    """
    Methods:
    __init__(self): Initializes the CalculatorModel
    update_expression(self, key): Updates the expression based on the user input key.
    evaluate_expression(self): Evaluates the current expression and returns the result.
    handle_del(self): Handles the deletion of the expressions.
    handle_clear(self): Clears the current expression.
    save_history(self): Saves the current expression and its result to the history.
    """
    def __init__(self):
        """
        Initializes the CalculatorModel with an empty expression and history.
        """
        self.expression = ""
        self.history = []

    def update_expression(self, key):
        """
        Updates the expression of the user input.
        :param key: Representing the user input (e.g., digit, operator, function).
        """
        if key == "DEL":
            self.handle_del()
        elif key == "CLR":
            self.handle_clear()
        else:
            self.expression += key

    def evaluate_expression(self):
        """
        Evaluates the current expression and returns the result.
        :return: The result of the expression, or "Error" if the expression is invalid.
        """
        try:
            result = eval(self.expression)
            return str(result)
        except Exception:
            return "Error"

    def handle_del(self):
        """
        Handles the deletion of the expressions.
        """
        if self.expression.endswith('sqrt('):
            self.expression = self.expression[:-5]
        elif self.expression.endswith('log('):
            self.expression = self.expression[:-4]
        elif self.expression.endswith('log2('):
            self.expression = self.expression[:-5]
        elif self.expression.endswith('log10('):
            self.expression = self.expression[:-6]
        elif self.expression.endswith('**'):
            self.expression = self.expression[:-2]
        elif len(self.expression) > 0:
            self.expression = self.expression[:-1]

    def handle_clear(self):
        """
        Clears the current expression.
        """
        self.expression = ""

    def save_history(self):
        """
        Saves the current expression and its result to the history.
        """
        result = self.evaluate_expression()
        if result != "Error":
            self.history.append(f"{self.expression} = {result}")
            self.expression = ""
