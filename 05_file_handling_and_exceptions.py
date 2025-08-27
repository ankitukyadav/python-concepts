"""
Python File Handling and Exception Handling Demo
This script demonstrates file operations and error handling in Python.
"""

import os
import json
from datetime import datetime

def create_sample_files():
    """Create sample files for demonstration."""
    # Create a simple text file
    with open("sample_data.txt", "w") as file:
        file.write("Welcome to Python File Handling!\n")
        file.write("This is line 2\n")
        file.write("This is line 3\n")
        file.write("Python makes file handling easy!\n")
    
    # Create a JSON file
    sample_data = {
        "students": [
            {"name": "Alice", "grade": 95, "subject": "Python"},
            {"name": "Bob", "grade": 87, "subject": "Python"},
            {"name": "Charlie", "grade": 92, "subject": "Python"}
        ],
        "created_date": datetime.now().isoformat()
    }
    
    with open("student_data.json", "w") as file:
        json.dump(sample_data, file, indent=2)

def read_text_file():
    """Demonstrate different ways to read text files."""
    print("=== Reading Text File ===")
    
    try:
        # Method 1: Read entire file
        with open("sample_data.txt", "r") as file:
            content = file.read()
            print("Entire file content:")
            print(content)
        
        # Method 2: Read line by line
        print("\nReading line by line:")
        with open("sample_data.txt", "r") as file:
            for line_num, line in enumerate(file, 1):
                print(f"Line {line_num}: {line.strip()}")
        
        # Method 3: Read all lines into a list
        with open("sample_data.txt", "r") as file:
            lines = file.readlines()
            print(f"\nTotal lines read: {len(lines)}")
            
    except FileNotFoundError:
        print("Error: sample_data.txt not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_and_append_file():
    """Demonstrate writing and appending to files."""
    print("\n=== Writing and Appending to Files ===")
    
    try:
        # Write to a new file
        with open("output.txt", "w") as file:
            file.write("This is a new file created by Python!\n")
            file.write(f"Created on: {datetime.now()}\n")
        
        # Append to the file
        with open("output.txt", "a") as file:
            file.write("This line was appended!\n")
            file.write("Python file handling is awesome!\n")
        
        # Read and display the result
        with open("output.txt", "r") as file:
            print("Contents of output.txt:")
            print(file.read())
            
    except Exception as e:
        print(f"Error writing to file: {e}")

def handle_json_data():
    """Demonstrate JSON file handling."""
    print("\n=== JSON File Handling ===")
    
    try:
        # Read JSON data
        with open("student_data.json", "r") as file:
            data = json.load(file)
        
        print("Student data from JSON:")
        for student in data["students"]:
            print(f"- {student['name']}: {student['grade']} in {student['subject']}")
        
        # Add a new student
        new_student = {"name": "Diana", "grade": 89, "subject": "Python"}
        data["students"].append(new_student)
        data["last_updated"] = datetime.now().isoformat()
        
        # Write updated data back to file
        with open("student_data.json", "w") as file:
            json.dump(data, file, indent=2)
        
        print("Added new student Diana to the JSON file!")
        
    except FileNotFoundError:
        print("JSON file not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
    except Exception as e:
        print(f"Error handling JSON: {e}")

def exception_handling_examples():
    """Demonstrate various exception handling scenarios."""
    print("\n=== Exception Handling Examples ===")
    
    # Example 1: Division by zero
    def safe_division(a, b):
        try:
            result = a / b
            return f"{a} / {b} = {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero!"
        except TypeError:
            return "Error: Invalid input types for division!"
    
    print(safe_division(10, 2))
    print(safe_division(10, 0))
    print(safe_division("10", 2))
    
    # Example 2: List index error
    def safe_list_access(lst, index):
        try:
            return f"Element at index {index}: {lst[index]}"
        except IndexError:
            return f"Error: Index {index} is out of range!"
        except TypeError:
            return "Error: Invalid list or index type!"
    
    sample_list = [1, 2, 3, 4, 5]
    print(safe_list_access(sample_list, 2))
    print(safe_list_access(sample_list, 10))
    
    # Example 3: Multiple exceptions with finally
    def file_operation_with_finally(filename):
        file_handle = None
        try:
            file_handle = open(filename, "r")
            content = file_handle.read()
            return f"File content length: {len(content)}"
        except FileNotFoundError:
            return f"Error: File '{filename}' not found!"
        except PermissionError:
            return f"Error: No permission to read '{filename}'!"
        finally:
            if file_handle:
                file_handle.close()
                print(f"File handle for '{filename}' closed.")
    
    print(file_operation_with_finally("sample_data.txt"))
    print(file_operation_with_finally("nonexistent.txt"))

def cleanup_demo_files():
    """Clean up demonstration files."""
    files_to_remove = ["sample_data.txt", "student_data.json", "output.txt"]
    
    for filename in files_to_remove:
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"Removed {filename}")
        except Exception as e:
            print(f"Error removing {filename}: {e}")

def main():
    """Main function to run all demonstrations."""
    print("=== Python File Handling and Exception Demo ===")
    
    # Create sample files
    create_sample_files()
    
    # Demonstrate file operations
    read_text_file()
    write_and_append_file()
    handle_json_data()
    
    # Demonstrate exception handling
    exception_handling_examples()
    
    # Clean up (optional - comment out if you want to keep the files)
    print("\n=== Cleanup ===")
    cleanup_demo_files()

if __name__ == "__main__":
    main()
