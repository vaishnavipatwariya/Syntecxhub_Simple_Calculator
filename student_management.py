import json
import os

# -------------------- Student Class --------------------
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


# -------------------- Manager Class --------------------
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    # Load from file
    def load_students(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    # Save to file
    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    # Add student
    def add_student(self, student):
        # Unique ID check
        for s in self.students:
            if s["id"] == student.student_id:
                print("❌ Student ID already exists!")
                return

        self.students.append(student.to_dict())
        self.save_students()
        print("✅ Student added successfully!")

    # Update student
    def update_student(self, student_id, new_name, new_grade):
        for student in self.students:
            if student["id"] == student_id:
                student["name"] = new_name
                student["grade"] = new_grade
                self.save_students()
                print("✅ Student updated successfully!")
                return

        print("❌ Student ID not found!")

    # Delete student
    def delete_student(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                self.students.remove(student)
                self.save_students()
                print("🗑️ Student deleted successfully!")
                return

        print("❌ Student ID not found!")

    # List all students
    def list_students(self):
        if not self.students:
            print("📭 No student records found.")
            return

        print("\n----- Student Records -----")
        for s in self.students:
            print(f"ID: {s['id']}  |  Name: {s['name']}  |  Grade: {s['grade']}")
        print("---------------------------\n")


# -------------------- Main CLI Menu --------------------
def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter ID: ")
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")

            student = Student(student_id, name, grade)
            manager.add_student(student)

        elif choice == "2":
            student_id = input("Enter ID to update: ")
            new_name = input("Enter new name: ")
            new_grade = input("Enter new grade: ")

            manager.update_student(student_id, new_name, new_grade)

        elif choice == "3":
            student_id = input("Enter ID to delete: ")
            manager.delete_student(student_id)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()
