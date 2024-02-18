class CalculatorController:
    def __init__(self, model, ui):
        self.model = model
        self.ui = ui

    def handle_click(self, key):
        self.model.update_expression(key)
        self.ui.display.config(text=self.model.expression)

        if key == '=':
            result = self.model.evaluate_expression()
            if result != "Error":
                self.model.save_history()
