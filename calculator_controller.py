"""For controller of calculator"""
from calculator_model import CalculatorModel
from calculator_ui import CalculatorUI


class CalculatorController:
    """
    Methods:
        __init__(self, model, ui): Initializes the CalculatorController.
        handle_click(self, key): Handles button clicks, updating the model and UI accordingly.
    """

    def __init__(self, model: CalculatorModel, ui: CalculatorUI):
        """
        Initializes the CalculatorController.

        :param model: CalculatorModel
        :param ui: CalculatorUI
        """
        self.model = model
        self.ui = ui

    def handle_click(self, key):
        """
        Handles button clicks, updating the model and UI accordingly.

        :param key: The key representing the button clicked.
        """
        self.model.update_expression(key)
        self.ui.display.config(text=self.model.expression)

        if key == '=':
            result = self.model.evaluate_expression()
            if result != "Error":
                self.model.save_history()
