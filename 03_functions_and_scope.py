"""
Python Functions and Scope Demo
This script demonstrates function definitions, parameters, return values, and scope.
"""

# Global variable
global_counter = 0

def simple_greeting(name="World"):
    """A simple function with default parameter."""
    return f"Hello, {name}! Welcome to Python programming."

def calculate_area(length, width):
    """Calculate rectangle area with multiple parameters."""
    area = length * width
    return area

def variable_arguments(*args, **kwargs):
    """Demonstrate *args and **kwargs usage."""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    
    total = sum(args) if args else 0
    return total

def scope_demonstration():
    """Demonstrate local vs global scope."""
    global global_counter
    local_variable = "I'm local!"
    
    print(f"Local variable: {local_variable}")
    print(f"Global counter before: {global_counter}")
    
    global_counter += 1
    
    print(f"Global counter after: {global_counter}")

def fibonacci_generator(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

def lambda_examples():
    """Demonstrate lambda functions and higher-order functions."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Lambda with map
    squares = list(map(lambda x: x**2, numbers))
    
    # Lambda with filter
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    
    # Lambda with sorted
    words = ["python", "java", "c", "javascript", "go"]
    sorted_by_length = sorted(words, key=lambda x: len(x))
    
    return squares, evens, sorted_by_length

def main():
    """Main function demonstrating all concepts."""
    print("=== Python Functions and Scope Demo ===")
    
    # Simple function calls
    print(simple_greeting())
    print(simple_greeting("Alice"))
    
    # Function with multiple parameters
    area = calculate_area(5, 3)
    print(f"\nRectangle area (5x3): {area}")
    
    # Variable arguments
    print("\n--- Variable Arguments Demo ---")
    result = variable_arguments(1, 2, 3, 4, name="Python", version=3.9)
    print(f"Sum of positional args: {result}")
    
    # Scope demonstration
    print("\n--- Scope Demo ---")
    scope_demonstration()
    scope_demonstration()  # Call again to see global counter increment
    
    # Fibonacci sequence
    print("\n--- Fibonacci Sequence ---")
    fib_sequence = fibonacci_generator(8)
    print(f"First 8 Fibonacci numbers: {fib_sequence}")
    
    # Lambda examples
    print("\n--- Lambda Functions Demo ---")
    squares, evens, sorted_words = lambda_examples()
    print(f"Squares: {squares}")
    print(f"Even numbers: {evens}")
    print(f"Words sorted by length: {sorted_words}")

if __name__ == "__main__":
    main()
