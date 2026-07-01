# Hospital Management System 

A Python-based Hospital Management System developed using **Object-Oriented Programming (OOP)** principles. This project supports hospital administration tasks such as managing doctors, managing patients, assigning doctors to patients, scheduling appointments, discharging patients, generating reports, and storing patient records in a file.

The project includes both a **command-line interface (CLI)** and a simple **Tkinter graphical user interface (GUI)**.

## Live Demo

View the project working mechanism here:

[Hospital Management System](https://youtu.be/r7nsyKeEwng)

## About the Project

The Hospital Management System is designed to help an admin manage hospital-related operations in a simple and organized way. The admin can log in, manage doctor records, view patient information, assign doctors to patients, discharge patients, group patients by family name, relocate patients, schedule appointments, generate reports, and save or load patient records.

This project demonstrates important Python concepts such as classes, objects, inheritance, encapsulation, file handling, lists, dictionaries, user input handling, GUI development using Tkinter, and data visualization using Matplotlib.

## Features

### Admin Features

- Admin login
- Update admin details
- Register new doctors
- View doctor records
- Update doctor details
- Delete doctor records
- View patient records
- Add new patients
- Assign doctors to patients
- Relocate patients from one doctor to another
- Discharge patients
- View discharged patients
- Group patients by family name
- Schedule appointments
- Generate management reports
- View reports using diagrams
- Save patient data to a file
- Load patient data from a file

### Doctor Management Features

- Add doctor details
- View available doctors
- Update doctor name or speciality
- Delete doctor records
- Store doctor speciality
- Track doctor appointments

### Patient Management Features

- Add patient details
- View patient records
- Store patient age, mobile number, postcode, and illness type
- Assign a doctor to a patient
- Discharge a patient
- View discharged patients
- Group patients with the same surname
- Save patient records to `patients.txt`

### Appointment Features

- Select a patient
- Select a doctor
- Enter appointment date
- Enter appointment time
- Store appointment details for the selected doctor

### Report Features

- Total number of doctors
- Number of patients per doctor
- Appointments per month per doctor
- Patients grouped by illness type
- Bar charts and diagrams using Matplotlib

### GUI Features

- Admin login screen
- Main menu dashboard
- Manage doctors
- Add and view doctors
- Manage patients
- Add and view patients
- Schedule appointment placeholder
- View reports placeholder
- Logout option

## Tech Stack

- Python
- Tkinter
- Matplotlib
- Object-Oriented Programming
- File Handling
- Command-Line Interface

## Project Structure

```text
Hospital-Management-System/
├── Admin.py
├── Doctor.py
├── GUI.py
├── Main.py
├── Patient.py
├── Person.py
├── Admin Login Flowchart.pdf
├── Main Process Flowchart.pdf
├── Test Cases.pdf
└── README.md
```

## Main Files

### Main.py

This is the main command-line version of the application. It starts the system, creates initial admin, doctor, and patient records, and displays the main menu for hospital management operations.

### GUI.py

This file contains the Tkinter-based graphical user interface. It provides an admin login screen and basic GUI options for managing doctors and patients.

### Admin.py

This file contains the `Admin` class. It handles admin login, doctor management, patient management, appointment scheduling, patient discharge, report generation, file saving, and file loading.

### Doctor.py

This file contains the `Doctor` class. It stores doctor details such as name, speciality, assigned patients, and appointments.

### Patient.py

This file contains the `Patient` class. It stores patient details such as name, age, mobile number, postcode, assigned doctor, symptoms, and illness type.

### Person.py

This file contains the parent `Person` class, which is inherited by the `Doctor` and `Patient` classes.

## How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

To check Python version, run:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Install Required Library

This project uses Matplotlib for report diagrams. Install it using:

```bash
pip install matplotlib
```

Tkinter usually comes pre-installed with Python.

### Step 3: Open the Project Folder

Open the project folder in VS Code or any Python IDE.

### Step 4: Run the Command-Line Version

Run this file:

```bash
python Main.py
```

or:

```bash
python3 Main.py
```

Default admin login:

```text
Username: admin
Password: 123
```

### Step 5: Run the GUI Version

To run the Tkinter GUI version, run:

```bash
python GUI.py
```

or:

```bash
python3 GUI.py
```

Default GUI login:

```text
Username: admin
Password: 123
```

## Main Menu Options

The command-line system includes the following options:

```text
1  - Register/view/update/delete doctor
2  - Discharge patients
3  - View discharged patient
4  - Assign doctor to a patient
5  - Update admin details
6  - Patient Family Management
7  - Relocate Patients
8  - Schedule an appointment
9  - Generate Management Report
10 - Save Patient data to file
11 - Load Patient data from file
12 - Add Patient
13 - View Report in diagram
14 - Quit
```

## Data Storage

The system uses simple text-file storage.

- `admin.txt` stores updated admin details
- `patients.txt` stores saved patient records

These files may be created automatically when the program runs.

## Documentation

The project also includes supporting documentation:

- `Admin Login Flowchart.pdf`
- `Main Process Flowchart.pdf`
- `Test Cases.pdf`

These documents explain the system flow, implementation checklist, and testing process.

## Example Patient Data

The system starts with sample patient records such as:

- Sara Smith
- Mike Jones
- Daivd Smith

These records are used for testing and demonstration purposes.

## Example Doctor Data

The system starts with sample doctor records such as:

- Dr. John Smith - Internal Med.
- Dr. Jone Smith - Pediatrics
- Dr. Jone Carlos - Cardiology

## Author

**Bibek Karki**

## License

This project is created for academic and learning purposes.
