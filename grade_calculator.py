# Week 2 Project: Student Grade Calculator
# This program calculates student grades based on marks
# and displays encouraging messages.

def calculate_grade(marks):
    """
    This function takes marks as input
    and returns the grade and an encouraging message.
    """
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! 😊"
    elif marks >= 60:
        return "D", "You passed. Keep improving! 💪"
    else:
        return "F", "Don't give up! Try harder next time 💡"


# Taking student name
student_name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid input! Marks must be between 0 and 100.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n📊 RESULT FOR", student_name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
