import tkinter as tk
from tkinter import messagebox, simpledialog
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("500x300")
        
        # Initialize Admin and sample data
        self.admin = Admin('admin', '123', 'B1 1AB')
        self.doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jone', 'Smith', 'Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
        self.patients = [Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', 'Infectious'),Patient('Mike','Jones', 37,'07555551234','L2 2AB','Non-Infectious'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','Chronic')]
        
        # Create Login Screen
        self.login_screen()
    
    def login_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Admin Login", font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        
        tk.Button(self.root, text="Login", command=self.check_login).pack(pady=10)
    
    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == self.admin.get_name() and password == self.admin.get_password():
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials")
    
    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Main Menu", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Manage Doctors", command=self.manage_doctors).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self.root, text="Manage Patients", command=self.manage_patients).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self.root, text="Schedule Appointment", command=self.schedule_appointment).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self.root, text="View Reports", command=self.view_reports).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(fill=tk.X, padx=20, pady=5)
    
    def manage_doctors(self):
        self.clear_window()
        tk.Label(self.root, text="Doctor Management", font=("Arial", 14)).pack(pady=10)
        
        tk.Button(self.root, text="Add Doctor", command=self.add_doctor).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self.root, text="View Doctors", command=self.view_doctors).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(fill=tk.X, padx=20, pady=5)
    
    def add_doctor(self):
        first_name = simpledialog.askstring("Input", "Enter first name:")
        surname = simpledialog.askstring("Input", "Enter surname:")
        speciality = simpledialog.askstring("Input", "Enter specialty:")
        if first_name and surname and speciality:
            self.doctors.append(Doctor(first_name, surname, speciality))
            messagebox.showinfo("Success", "Doctor added successfully")
    
    def view_doctors(self):
        doctor_list = "\n".join([doc.full_name() + " - " + doc.get_speciality() for doc in self.doctors])
        messagebox.showinfo("Doctors", doctor_list if doctor_list else "No doctors available")
    
    def manage_patients(self):
        self.clear_window()
        tk.Label(self.root, text="Patient Management", font=("Arial", 14)).pack(pady=10)
        
        tk.Button(self.root, text="Add Patient", command=self.add_patient).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self.root, text="View Patients", command=self.view_patients).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(fill=tk.X, padx=20, pady=5)
    
    def add_patient(self):
        first_name = simpledialog.askstring("Input", "Enter first name:")
        surname = simpledialog.askstring("Input", "Enter surname:")
        age = simpledialog.askinteger("Input", "Enter age:")
        mobile = simpledialog.askstring("Input", "Enter mobile number:")
        postcode = simpledialog.askstring("Input", "Enter postcode:")
        illness_type = simpledialog.askstring("Input", "Enter illness type:")
        
        if first_name and surname and age and mobile and postcode and illness_type:
            self.patients.append(Patient(first_name, surname, age, mobile, postcode, illness_type))
            messagebox.showinfo("Success", "Patient added successfully")
    
    def view_patients(self):
        patient_list = "\n".join([pat.full_name() + " - " + pat.get_illness_type() for pat in self.patients])
        messagebox.showinfo("Patients", patient_list if patient_list else "No patients available")
    
    def schedule_appointment(self):
        messagebox.showinfo("Coming Soon", "Appointment scheduling feature is under development!")
    
    def view_reports(self):
        messagebox.showinfo("Coming Soon", "Report viewing feature is under development!")
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the Tkinter GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()
