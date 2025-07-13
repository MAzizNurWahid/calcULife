import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, lambdify, diff

x = symbols('x')

def plot_function_and_derivative(expr_str, ax):
    ax.clear()
    try:
        expr = sympify(expr_str)
        func = lambdify(x, expr, 'numpy')
        d_expr = diff(expr, x)
        d_func = lambdify(x, d_expr, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)
        y_d_vals = d_func(x_vals)
        ax.plot(x_vals, y_vals, label='f(x)', color='cyan')
        ax.plot(x_vals, y_d_vals, label="f'(x)", color='magenta')
        ax.set_title('Grafik f(x) dan Turunannya')
        ax.legend()
    except Exception as e:
        ax.text(0.5, 0.5, str(e), ha='center', va='center')
