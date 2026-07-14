# BMI Calculator

A simple BMI (Body Mass Index) calculator built with Python and Tkinter, supporting both metric and imperial units.

## Features

- Switch between **Metric** (kg / cm) and **Imperial** (lb / in) units
- Calculates BMI and displays a color-coded category:
  - **Underweight** (blue) — BMI < 18.5
  - **Normal weight** (green) — 18.5 ≤ BMI < 25
  - **Overweight** (orange) — 25 ≤ BMI < 30
  - **Obese** (red) — BMI ≥ 30
- Input validation with friendly error messages for missing, negative, or non-numeric values
- Press `Enter` or click the button to calculate

## Requirements

- Python 3.x
- Tkinter (included with standard Python installations)

## How to Run

```bash
python3 bmi_calculator.py
```

## Usage

1. Select your preferred unit system (Metric or Imperial)
2. Enter your weight and height in the corresponding fields
3. Click **Calculate BMI** or press `Enter`
4. View your BMI value and category displayed below

## Formulas Used

- **Metric:** `BMI = weight (kg) / height (m)²`
- **Imperial:** `BMI = 703 × weight (lb) / height (in)²`

## File Structure

```
bmi_calculator.py   # Main application file
```

## Notes

- BMI is a general screening tool and does not account for factors like muscle mass, bone density, or body composition. It should not be used as a sole indicator of health.
