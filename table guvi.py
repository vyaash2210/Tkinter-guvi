import tkinter as tk
from tkinter import messagebox

class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")

        # Data structures for storing students and teachers
        self.students = []
        self.teachers = []

        self.create_widgets()

    def create_widgets(self):
        # Teacher section
        self.label_teacher_id = tk.Label(self.root, text="Teacher ID:")
        self.label_teacher_id.grid(row=0, column=0, padx=5)

        self.entry_teacher_id = tk.Entry(self.root, width=20)
        self.entry_teacher_id.grid(row=0, column=1, padx=5)

        self.label_teacher_name = tk.Label(self.root, text="Teacher Name:")
        self.label_teacher_name.grid(row=0, column=2, padx=5)

        self.entry_teacher_name = tk.Entry(self.root, width=20)
        self.entry_teacher_name.grid(row=0, column=3, padx=5)

        # Buttons for teacher operations
        self.button_create_teacher = tk.Button(self.root, text="Create Teacher", command=self.create_teacher)
        self.button_create_teacher.grid(row=1, column=0, columnspan=4, pady=10)

        # Student section
        self.label_student_id = tk.Label(self.root, text="Student ID:")
        self.label_student_id.grid(row=2, column=0, padx=5)

        self.entry_student_id = tk.Entry(self.root, width=20)
        self.entry_student_id.grid(row=2, column=1, padx=5)

        self.label_student_name = tk.Label(self.root, text="Student Name:")
        self.label_student_name.grid(row=2, column=2, padx=5)

        self.entry_student_name = tk.Entry(self.root, width=20)
        self.entry_student_name.grid(row=2, column=3, padx=5)

        # Buttons for student operations
        self.button_create_student = tk.Button(self.root, text="Create Student", command=self.create_student)
        self.button_create_student.grid(row=3, column=0, columnspan=4, pady=10)

        self.button_read_students = tk.Button(self.root, text="Read Students", command=self.read_students)
        self.button_read_students.grid(row=4, column=0, columnspan=4, pady=10)

        self.button_update_student = tk.Button(self.root, text="Update Student", command=self.update_student)
        self.button_update_student.grid(row=5, column=0, columnspan=4, pady=10)

        self.button_delete_student = tk.Button(self.root, text="Delete Student", command=self.delete_student)
        self.button_delete_student.grid(row=6, column=0, columnspan=4, pady=10)

        # Principal and Admin buttons
        self.button_create_principal = tk.Button(self.root, text="Create Principal", command=self.create_principal)
        self.button_create_principal.grid(row=7, column=0, columnspan=4, pady=10)

        self.button_create_admin = tk.Button(self.root, text="Create Admin", command=self.create_admin)
        self.button_create_admin.grid(row=8, column=0, columnspan=4, pady=10)

    def create_teacher(self):
        teacher_id = self.entry_teacher_id.get()
        teacher_name = self.entry_teacher_name.get()

        # Perforing any desired logic with the entered teacher data, for example, show a message box
        message = f"Teacher created!\nID: {teacher_id}\nName: {teacher_name}"
        messagebox.showinfo("Teacher Created", message)

    def create_student(self):
        student_id = self.entry_student_id.get()
        student_name = self.entry_student_name.get()

        # Storing student data in the students list
        self.students.append({"id": student_id, "name": student_name})

        # Performing any desired logic with the entered student data, for example, show a message box
        message = f"Student created!\nID: {student_id}\nName: {student_name}"
        messagebox.showinfo("Student Created", message)

    def read_students(self):
        # Displaying a messagebox with a list of students
        students_list = "\n".join([f"ID: {student['id']}, Name: {student['name']}" for student in self.students])
        messagebox.showinfo("Students List", students_list)

    def update_student(self):
        # For simplicity, let's just display a messagebox for updating a student
        messagebox.showinfo("Update Student", "Updating a student...")

    def delete_student(self):
        # For simplicity, let's just display a messagebox for deleting a student
        messagebox.showinfo("Delete Student", "Deleting a student...")

    def create_principal(self):
        # For simplicity, let's just display a messagebox for creating a principal
        messagebox.showinfo("Create Principal", "Creating a principal...")

    def create_admin(self):
        # For simplicity, let's just display a messagebox for creating an admin
        messagebox.showinfo("Create Admin", "Creating an admin...")

# Creating main window
root = tk.Tk()
app = SchoolManagementSystem(root)

# Starting the Tkinter event loop
root.mainloop()
