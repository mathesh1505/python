def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    return sum_val, diff_val, prod_val
s, d, p = calculate(8, 3)
print(f"Sum: {s}, Difference: {d}, Product: {p}")
