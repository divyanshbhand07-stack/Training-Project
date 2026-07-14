import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(bg="#1e1e1e")

        self.expression = ""
        self.input_text = tk.StringVar(value="0")

        self._build_display()
        self._build_buttons()

        # Allow keyboard input
        self.bind("<Key>", self._on_key)

    # ---------- UI ----------
    def _build_display(self):
        display_frame = tk.Frame(self, bg="#1e1e1e")
        display_frame.pack(fill="both", padx=10, pady=(15, 5))

        entry = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=("Segoe UI", 28, "bold"),
            justify="right",
            bd=0,
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            state="readonly",
            readonlybackground="#1e1e1e",
        )
        entry.pack(fill="both", ipady=15)

    def _build_buttons(self):
        btns_frame = tk.Frame(self, bg="#1e1e1e")
        btns_frame.pack(padx=10, pady=10)

        buttons = [
            ("C", "clear"), ("⌫", "back"), ("%", "op"), ("÷", "op"),
            ("7", "num"), ("8", "num"), ("9", "num"), ("×", "op"),
            ("4", "num"), ("5", "num"), ("6", "num"), ("−", "op"),
            ("1", "num"), ("2", "num"), ("3", "num"), ("+", "op"),
            ("±", "sign"), ("0", "num"), (".", "num"), ("=", "eq"),
        ]

        colors = {
            "num": ("#333333", "white"),
            "op": ("#ff9500", "white"),
            "eq": ("#ff9500", "white"),
            "clear": ("#a5a5a5", "black"),
            "back": ("#a5a5a5", "black"),
            "sign": ("#a5a5a5", "black"),
        }

        row, col = 0, 0
        for (text, kind) in buttons:
            bg, fg = colors[kind]
            btn = tk.Button(
                btns_frame,
                text=text,
                font=("Segoe UI", 18, "bold"),
                width=5,
                height=2,
                bd=0,
                bg=bg,
                fg=fg,
                activebackground="#555555",
                activeforeground="white",
                command=lambda t=text: self._on_button(t),
            )
            btn.grid(row=row, column=col, padx=4, pady=4)
            col += 1
            if col > 3:
                col = 0
                row += 1

    # ---------- Logic ----------
    def _on_button(self, char):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "=":
            self._calculate()
            return
        elif char == "±":
            self._toggle_sign()
            return
        else:
            mapping = {"×": "*", "÷": "/", "−": "-"}
            self.expression += mapping.get(char, char)

        self._update_display()

    def _toggle_sign(self):
        # Toggle sign of the last number in the expression
        import re
        match = re.search(r"(-?\d+\.?\d*)$", self.expression)
        if match:
            num = match.group(1)
            start, end = match.span(1)
            if num.startswith("-"):
                new_num = num[1:]
            else:
                new_num = "-" + num
            self.expression = self.expression[:start] + new_num + self.expression[end:]
        self._update_display()

    def _update_display(self):
        display = self.expression.replace("*", "×").replace("/", "÷").replace("-", "−")
        self.input_text.set(display if display else "0")

    def _calculate(self):
        try:
            # Safe-ish eval: only allow digits, operators, dot, parentheses
            allowed = set("0123456789.+-*/() ")
            if not all(c in allowed for c in self.expression):
                raise ValueError("Invalid characters")
            result = eval(self.expression, {"__builtins__": {}}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
        except ZeroDivisionError:
            self.expression = ""
            self.input_text.set("Error: Div by 0")
            return
        except Exception:
            self.expression = ""
            self.input_text.set("Error")
            return

        self._update_display()

    def _on_key(self, event):
        key = event.char
        if key in "0123456789.+-/*()":
            self.expression += key
            self._update_display()
        elif key == "\r":  # Enter
            self._calculate()
        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
            self._update_display()
        elif key.lower() == "c":
            self.expression = ""
            self._update_display()


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()