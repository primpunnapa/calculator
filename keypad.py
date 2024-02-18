""" keypad for calculator"""
import tkinter as tk


class Keypad(tk.Frame):
    """
    Methods:
    __init__(self): Initializes the Keypad
    init_components(self): Initialize the components of the Keypad.
    handle_click(self, event): Handle button click events.
    bind(self): Bind an event handler to an event sequence.
    configure(self): Apply configuration settings to all buttons.
    """

    def __init__(self, parent, keynames=[], columns=1, controller=None, **kwargs):
        super().__init__(parent,**kwargs)
        self.keynames = keynames
        self.controller = controller
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        for k in range(len(self.keynames)):
            col = k % columns
            row = k // columns
            button = tk.Button(self, text=str(self.keynames[k]))

            options = {"padx": 2, "pady": 2, 'sticky': tk.NSEW}
            button.grid(row=row, column=col, **options)

        for fr in range(len(self.keynames)//columns):
            self.rowconfigure(fr, weight=1)
        for fc in range(columns):
            self.columnconfigure(fc, weight=1)

    def handle_click(self, key):
        """
        Handle button click events.
        """
        self.controller.handle_click(key)

    def bind(self, sequence, func):
        """Bind an event handler to an event sequence."""
        for button in self.winfo_children():
            button.bind(sequence, func)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.winfo_children():
            button[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        result = {}
        for button in self.winfo_children():
            return button[key]
        return result

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for button in self.winfo_children():
            button.configure(cnf, **kwargs)

    @property
    def frame(self):
        return super(Keypad, self)
