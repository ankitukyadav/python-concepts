"""
Python Variables and Data Types Demo
This script demonstrates basic Python data types and variable usage.
"""

def demonstrate_data_types():
    """Showcase different Python data types with examples."""
    
    # Numeric types
    integer_num = 42
    float_num = 3.14159
    complex_num = 3 + 4j
    
    # String type
    greeting = "Hello, Python World!"
    multiline_text = """This is a
    multiline string example
    for demonstration purposes."""
    
    # Boolean type
    is_learning = True
    is_expert = False
    
    # Collection types
    fruits_list = ["apple", "banana", "cherry", "date"]
    coordinates_tuple = (10.5, 20.3)
    student_info = {
        "name": "Alex",
        "age": 25,
        "courses": ["Python", "Data Science"]
    }
    unique_numbers = {1, 2, 3, 4, 5}
    
    # Display information
    print("=== Python Data Types Demonstration ===")
    print(f"Integer: {integer_num} (type: {type(integer_num).__name__})")
    print(f"Float: {float_num} (type: {type(float_num).__name__})")
    print(f"Complex: {complex_num} (type: {type(complex_num).__name__})")
    print(f"String: {greeting} (type: {type(greeting).__name__})")
    print(f"Boolean: {is_learning} (type: {type(is_learning).__name__})")
    print(f"List: {fruits_list} (type: {type(fruits_list).__name__})")
    print(f"Tuple: {coordinates_tuple} (type: {type(coordinates_tuple).__name__})")
    print(f"Dictionary: {student_info} (type: {type(student_info).__name__})")
    print(f"Set: {unique_numbers} (type: {type(unique_numbers).__name__})")

if __name__ == "__main__":
    demonstrate_data_types()
