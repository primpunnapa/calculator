"""Display the calculator user interface."""
from calculator_ui import CalculatorUI
from calculator_model import CalculatorModel
from calculator_controller import CalculatorController


if __name__ == '__main__':
    model = CalculatorModel()
    ui = CalculatorUI()
    controller = CalculatorController(model, ui)
    ui.controller = controller
    ui.mainloop()