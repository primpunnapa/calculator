"""code for a calculator with class-based UI."""

import tkinter as tk
from keypad import Keypad
from calculator_model import CalculatorModel


class CalculatorUI(tk.Tk):
    """
    Methods:
    __init__(self): Initializes the CalculatorUI
    init_components(self): Initialize the components of the calculator UI.
    handle_click(self, event): Handle button click events.
    run(self): Show the UI and wait for user input
    """
    def __init__(self):
        """
        Initialize the calculator UI.
        """
        super().__init__()
        self.title('Calculator')
        self.model = CalculatorModel()
        self.init_components()

    def init_components(self):
        """
        Initialize the components of the calculator UI.

        """
        self.display = tk.Label(self, text="", justify='right', anchor='e')
        self.display.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.display.configure(background='#FFA07A', font=('Charter', 40), fg='#33A1C9')

        keypad = Keypad(self,
                        ['7', '8', '9', '4', '5', '6', '1', '2', '3', ' ', '0', '.'], columns=3)
        operation = Keypad(self,['*', '/', '+', '-', '^', 'mod', '(', ')', '=', 'exp', 'ln', 'log10', 'log2',
                                 'sqrt', 'DEL', 'CLR'], columns=2)

        keypad.bind('<Button>', self.handle_click)
        keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        keypad.configure(foreground='#33A1C9')

        operation.bind('<Button>', self.handle_click)
        operation.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        operation.configure(foreground='#33A1C9')

        # Create a Listbox for history
        self.history_listbox = tk.Listbox(self, height=5, width=15)
        self.history_listbox.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        self.history_listbox.configure(font=('Charter', 16), foreground='#33A1C9')

    def handle_click(self, event):
        """
        Handle button click events.
        :param event: The click event.
        """
        key = event.widget['text']
        if key == "=":
            result = self.model.evaluate_expression()

            if result != "Error":
                self.display.config(fg='#33A1C9')

                history_item = f"{self.model.expression} = {result}"
                self.model.save_history()
                self.history_listbox.insert(tk.END, history_item)

                self.model.handle_clear()
                self.display.config(text=result)
            else:
                self.display.config(fg='red')

        elif key == '^':
            self.model.expression += '**'
            self.display.config(text=self.model.expression)

        elif key == 'mod':
            self.model.expression += '%'
            self.display.config(text=self.model.expression)

        elif key == 'CLR':
            # Clear the input
            self.model.handle_clear()
            self.display.config(text="")

        elif key == 'DEL':
            # Delete the last input value
            self.model.handle_del()
            self.display.config(text=self.model.expression)

        elif key in {'sqrt', 'exp', 'log2', 'log10', 'ln'}:
            # Handle special operations
            if self.model.expression and self.model.expression[-1].isdigit():
                self.model.expression = key + '(' + self.model.expression + ')'
            else:
                self.model.expression = self.model.expression + key + '('
            self.display.config(text=self.model.expression)

        else:
            self.model.expression += key
            self.display.config(text=self.model.expression)

    def run(self):
        """Show the UI and wait for user input"""
        self.mainloop()
