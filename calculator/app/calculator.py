import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(
            self.root, width=20, font=("Arial", 24), borderwidth=2, relief="solid"
        )
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
            ("sin", 5, 0),
            ("cos", 5, 1),
            ("tan", 5, 2),
            ("sqrt", 5, 3),
            ("log", 6, 0),
            ("^", 6, 1),
            ("(", 6, 2),
            (")", 6, 3),
            ("C", 7, 0),
            ("%", 7, 1),
            ("!", 7, 2),
        ]

        for text, row, col in buttons:
            button = tk.Button(
                self.root,
                text=text,
                width=5,
                height=2,
                font=("Arial", 18),
                command=lambda t=text: self.on_button_click(t),
            )
            button.grid(row=row, column=col)

    def on_button_click(self, button_text):
        current_text = self.display.get()

        if button_text == "C":
            self.display.delete(0, tk.END)
        elif button_text == "=":
            try:
                result = self.evaluate_expression(current_text)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.display.insert(tk.END, button_text)

    def evaluate_expression(self, expression):
        try:
            # Replace the scientific functions with appropriate function calls
            expression = expression.replace("sin", "calculator.sine")
            expression = expression.replace("cos", "calculator.cosine")
            expression = expression.replace("tan", "calculator.tangent")
            expression = expression.replace("log", "calculator.log")
            expression = expression.replace("sqrt", "calculator.square_root")
            expression = expression.replace("^", "calculator.power")
            expression = expression.replace("!", "calculator.factorial")

            # Eval the final expression
            return eval(expression)
        except Exception as e:
            return "Error"
