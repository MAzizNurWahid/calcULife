# modules/math_logic.py

import sympy as sp

def parse_function(func_str):
    x = sp.Symbol('x')
    try:
        func = sp.sympify(func_str)
        return func
    except (sp.SympifyError, TypeError):
        return None

def differentiate_function(func):
    x = sp.Symbol('x')
    return sp.diff(func, x)

def integrate_function(func):
    x = sp.Symbol('x')
    return sp.integrate(func, x)

def evaluate_function(func, x_vals):
    x = sp.Symbol('x')
    return [float(func.subs(x, val)) for val in x_vals]
