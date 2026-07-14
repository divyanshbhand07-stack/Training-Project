import tkinter as tk
from tkinter import font

class BMICalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BMI Calculator")
        self.geometry("380x480")
        self.resizable(False, False)
        self.configure(bg="#1e1e2e")

        self.unit = tk.StringVar(value="metric")  # metric or imperial

        self._build_ui()

    # ---------- UI ----------
    def _build_ui(self):
        title_font = font.Font(family="Segoe UI", size=22, weight="bold")
        label_font = font.Font(family="Segoe UI", size=12)
        result_font = font.Font(family="Segoe UI", size=16, weight="bold")

        tk.Label(
            self, text="BMI Calculator", font=title_font,
            bg="#1e1e2e", fg="white"
        ).pack(pady=(25, 15))

        # Unit toggle
        unit_frame = tk.Frame(self, bg="#1e1e2e")
        unit_frame.pack(pady=(0, 15))

        tk.Radiobutton(
            unit_frame, text="Metric (kg / cm)", variable=self.unit, value="metric",
            font=label_font, bg="#1e1e2e", fg="white", selectcolor="#2d2d44",
            activebackground="#1e1e2e", activeforeground="white",
            command=self._update_labels
        ).grid(row=0, column=0, padx=10)

        tk.Radiobutton(
            unit_frame, text="Imperial (lb / in)", variable=self.unit, value="imperial",
            font=label_font, bg="#1e1e2e", fg="white", selectcolor="#2d2d44",
            activebackground="#1e1e2e", activeforeground="white",
            command=self._update_labels
        ).grid(row=0, column=1, padx=10)

        # Weight input
        form_frame = tk.Frame(self, bg="#1e1e2e")
        form_frame.pack(pady=10, padx=30, fill="x")

        self.weight_label = tk.Label(
            form_frame, text="Weight (kg):", font=label_font, bg="#1e1e2e", fg="white"
        )
        self.weight_label.grid(row=0, column=0, sticky="w", pady=8)

        self.weight_entry = tk.Entry(
            form_frame, font=label_font, bg="#2d2d44", fg="white",
            insertbackground="white", bd=0, relief="flat"
        )
        self.weight_entry.grid(row=0, column=1, pady=8, ipady=6, sticky="ew")

        self.height_label = tk.Label(
            form_frame, text="Height (cm):", font=label_font, bg="#1e1e2e", fg="white"
        )
        self.height_label.grid(row=1, column=0, sticky="w", pady=8)

        self.height_entry = tk.Entry(
            form_frame, font=label_font, bg="#2d2d44", fg="white",
            insertbackground="white", bd=0, relief="flat"
        )
        self.height_entry.grid(row=1, column=1, pady=8, ipady=6, sticky="ew")

        form_frame.columnconfigure(1, weight=1)

        # Calculate button
        tk.Button(
            self, text="Calculate BMI", font=label_font, bg="#ff9500", fg="white",
            bd=0, activebackground="#ffb340", activeforeground="white",
            command=self._calculate, cursor="hand2"
        ).pack(pady=20, ipadx=10, ipady=8, fill="x", padx=30)

        # Result display
        self.result_frame = tk.Frame(self, bg="#2d2d44")
        self.result_frame.pack(pady=5, padx=30, fill="both", expand=True)

        self.bmi_value_label = tk.Label(
            self.result_frame, text="--", font=result_font, bg="#2d2d44", fg="white"
        )
        self.bmi_value_label.pack(pady=(20, 5))

        self.bmi_category_label = tk.Label(
            self.result_frame, text="Enter your details above", font=label_font,
            bg="#2d2d44", fg="#aaaaaa"
        )
        self.bmi_category_label.pack(pady=(0, 20))

        self.error_label = tk.Label(
            self, text="", font=("Segoe UI", 10), bg="#1e1e2e", fg="#ff5555"
        )
        self.error_label.pack()

        # Enter key triggers calculation
        self.bind("<Return>", lambda event: self._calculate())

    def _update_labels(self):
        if self.unit.get() == "metric":
            self.weight_label.config(text="Weight (kg):")
            self.height_label.config(text="Height (cm):")
        else:
            self.weight_label.config(text="Weight (lb):")
            self.height_label.config(text="Height (in):")

    # ---------- Logic ----------
    def _calculate(self):
        self.error_label.config(text="")
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if weight <= 0 or height <= 0:
                raise ValueError("Values must be positive")

            if self.unit.get() == "metric":
                height_m = height / 100
                bmi = weight / (height_m ** 2)
            else:
                # Imperial formula: 703 * weight(lb) / height(in)^2
                bmi = 703 * weight / (height ** 2)

            category, color = self._get_category(bmi)

            self.bmi_value_label.config(text=f"{bmi:.1f}", fg=color)
            self.bmi_category_label.config(text=category, fg=color)

        except ValueError:
            self.error_label.config(text="Please enter valid positive numbers.")
            self.bmi_value_label.config(text="--", fg="white")
            self.bmi_category_label.config(text="Enter your details above", fg="#aaaaaa")

    @staticmethod
    def _get_category(bmi):
        if bmi < 18.5:
            return "Underweight", "#5dade2"
        elif bmi < 25:
            return "Normal weight", "#58d68d"
        elif bmi < 30:
            return "Overweight", "#f5b041"
        else:
            return "Obese", "#ec7063"


if __name__ == "__main__":
    app = BMICalculator()
    app.mainloop()