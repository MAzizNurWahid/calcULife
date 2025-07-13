from sympy import symbols, diff, integrate, sympify

x = symbols('x')

def compute_derivative(expr_str):
    try:
        expr = sympify(expr_str)
        derivative = diff(expr, x)
        return derivative
    except Exception as e:
        return f"Error: {str(e)}"

def compute_integral(expr_str, a=None, b=None):
    try:
        expr = sympify(expr_str)
        if a is not None and b is not None:
            result = integrate(expr, (x, a, b))
        else:
            result = integrate(expr, x)
        return result
    except Exception as e:
        return f"Error: {str(e)}"
