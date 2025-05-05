import tkinter as tk
from app import calculator

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorApp = calculator.CalculatorApp
    app = CalculatorApp(root)
    root.mainloop()
