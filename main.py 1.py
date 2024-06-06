class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        num_grades = sum([len(grades) for grades in self.grades.values()])
        return total_grades / num_grades if num_grades != 0 else 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_grades(self):
        print("Grades by Subject:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")

    def display_overall_grade(self):
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        gpa = self.get_gpa(average)
        print(f"\nOverall Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

def main():
    student_grades = StudentGrades()
    while True:
        print("\nOptions:")
        print("1. Add grade")
        print("2. Display grades")
        print("3. Display overall grade")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            student_grades.add_grade(subject, grade)
        elif choice == '2':
            student_grades.display_grades()
        elif choice == '3':
            student_grades.display_overall_grade()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
