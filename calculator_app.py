"""Display the calculator user interface."""
from calculator_ui import Calculator_UI
from calculator_model import CalculatorModel
from calculator_controller import CalculatorController


if __name__ == '__main__':
    model = CalculatorModel()
    ui = Calculator_UI(None)
    controller = CalculatorController(model, ui)
    ui.controller = controller
    ui.mainloop()