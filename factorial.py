def other_table(num, up_to, operation):
    """Generates a table of squares, cubes, or factorials."""
    results = []
    for i in range(1, up_to + 1):
        results.append((i, operation(i)))
    return results

def square(x):
    return x * x

def cube(x):
    return x * x * x

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

# Example usage:
squares = other_table(9, 10, square)
cubes = other_table(9, 10, cube)
factorials = other_table(9, 10, factorial)

print("Squares:")
for i, sq in squares:
    print(f"{i} squared = {sq}")

print("Cubes:")
for i, c in cubes:
    print(f"{i} cubed = {c}")

print("Factorials:")
for i, f in factorials:
    print(f"{i}! = {f}")
