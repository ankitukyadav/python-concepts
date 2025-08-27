"""
Python Control Structures Demo
This script demonstrates if-else statements, loops, and control flow.
"""

def number_classifier(num):
    """Classify a number based on various conditions."""
    print(f"\nAnalyzing number: {num}")
    
    # If-elif-else demonstration
    if num > 0:
        print("✓ Positive number")
    elif num < 0:
        print("✗ Negative number")
    else:
        print("⚬ Zero")
    
    # Nested conditions
    if num != 0:
        if num % 2 == 0:
            print("✓ Even number")
        else:
            print("✓ Odd number")
    
    # Multiple conditions
    if num > 0 and num <= 100:
        print("✓ Number is between 1 and 100")

def loop_demonstrations():
    """Show different types of loops in Python."""
    print("\n=== Loop Demonstrations ===")
    
    # For loop with range
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(f"Count: {i}")
    
    # For loop with list
    colors = ["red", "green", "blue", "yellow"]
    print("\nIterating through colors:")
    for color in colors:
        print(f"Color: {color}")
    
    # While loop
    print("\nCountdown using while loop:")
    countdown = 5
    while countdown > 0:
        print(f"T-minus {countdown}")
        countdown -= 1
    print("Blast off! 🚀")
    
    # Loop with break and continue
    print("\nNumbers 1-10, skipping 5, stopping at 8:")
    for num in range(1, 11):
        if num == 5:
            continue  # Skip 5
        if num == 8:
            break     # Stop at 8
        print(f"Number: {num}")

def main():
    """Main function to run all demonstrations."""
    print("=== Python Control Structures Demo ===")
    
    # Test number classification
    test_numbers = [15, -7, 0, 42, -3]
    for number in test_numbers:
        number_classifier(number)
    
    # Show loop examples
    loop_demonstrations()

if __name__ == "__main__":
    main()
