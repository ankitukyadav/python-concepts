"""
Python Classes and Objects Demo
This script demonstrates object-oriented programming concepts in Python.
"""

class Student:
    """A class representing a student with basic information and methods."""
    
    # Class variable
    school_name = "Python Learning Academy"
    student_count = 0
    
    def __init__(self, name, age, student_id):
        """Initialize a new student instance."""
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
        self.enrolled_courses = []
        
        # Increment class variable
        Student.student_count += 1
    
    def add_grade(self, subject, grade):
        """Add a grade for a specific subject."""
        self.grades.append({"subject": subject, "grade": grade})
        print(f"Added grade {grade} for {subject} to {self.name}'s record")
    
    def enroll_course(self, course_name):
        """Enroll student in a course."""
        if course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course_name)
            print(f"{self.name} enrolled in {course_name}")
        else:
            print(f"{self.name} is already enrolled in {course_name}")
    
    def calculate_average_grade(self):
        """Calculate the average grade of the student."""
        if not self.grades:
            return 0
        
        total = sum(grade["grade"] for grade in self.grades)
        return round(total / len(self.grades), 2)
    
    def get_student_info(self):
        """Return formatted student information."""
        avg_grade = self.calculate_average_grade()
        return f"""
Student Information:
Name: {self.name}
Age: {self.age}
ID: {self.student_id}
Enrolled Courses: {', '.join(self.enrolled_courses) if self.enrolled_courses else 'None'}
Average Grade: {avg_grade}
School: {self.school_name}
        """
    
    @classmethod
    def get_student_count(cls):
        """Class method to get total number of students."""
        return cls.student_count
    
    @staticmethod
    def is_passing_grade(grade):
        """Static method to check if a grade is passing."""
        return grade >= 60

class Teacher(Student):  # Inheritance example
    """A class representing a teacher, inheriting from Student."""
    
    def __init__(self, name, age, teacher_id, subject):
        """Initialize a teacher instance."""
        # Call parent constructor
        super().__init__(name, age, teacher_id)
        self.subject = subject
        self.students_taught = []
    
    def assign_grade(self, student, grade):
        """Assign a grade to a student."""
        if isinstance(student, Student):
            student.add_grade(self.subject, grade)
            if student not in self.students_taught:
                self.students_taught.append(student)
        else:
            print("Invalid student object")
    
    def get_teacher_info(self):
        """Return formatted teacher information."""
        return f"""
Teacher Information:
Name: {self.name}
Age: {self.age}
ID: {self.student_id}
Subject: {self.subject}
Students Taught: {len(self.students_taught)}
        """

def demonstrate_oop_concepts():
    """Demonstrate various OOP concepts."""
    print("=== Python Classes and Objects Demo ===")
    
    # Create student instances
    alice = Student("Alice Johnson", 20, "S001")
    bob = Student("Bob Smith", 19, "S002")
    charlie = Student("Charlie Brown", 21, "S003")
    
    # Create teacher instance
    prof_python = Teacher("Dr. Python", 35, "T001", "Computer Science")
    
    # Enroll students in courses
    alice.enroll_course("Python Programming")
    alice.enroll_course("Data Structures")
    bob.enroll_course("Python Programming")
    charlie.enroll_course("Web Development")
    
    # Add grades
    alice.add_grade("Python Programming", 95)
    alice.add_grade("Data Structures", 88)
    bob.add_grade("Python Programming", 92)
    charlie.add_grade("Web Development", 85)
    
    # Teacher assigns grades
    prof_python.assign_grade(alice, 90)
    prof_python.assign_grade(bob, 87)
    
    # Display information
    print(alice.get_student_info())
    print(bob.get_student_info())
    print(prof_python.get_teacher_info())
    
    # Class method usage
    print(f"Total students created: {Student.get_student_count()}")
    
    # Static method usage
    test_grades = [95, 88, 45, 72, 55]
    for grade in test_grades:
        status = "PASS" if Student.is_passing_grade(grade) else "FAIL"
        print(f"Grade {grade}: {status}")

if __name__ == "__main__":
    demonstrate_oop_concepts()
