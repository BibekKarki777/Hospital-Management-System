import matplotlib.pyplot as plt
from Doctor import Doctor

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """       
    
        self.__username = username
        self.__password = password
        self.__address =  address
        self.load_from_file()
            
    def load_from_file(self, filename='admin.txt'):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 3:
                    self.__username = lines[0].strip()
                    self.__password = lines[1].strip()
                    self.__address = lines[2].strip()
        except FileNotFoundError:
            self.save_to_file()

    def save_to_file(self, filename='admin.txt'):
        with open(filename, 'w') as file:
            file.write(f'{self.__username}\n')
            file.write(f'{self.__password}\n')
            file.write(f'{self.__address}\n')
    
    #Getters
    def get_name(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_address(self):
        return self.__address
    


    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        return self.__username in username and self.__password == password

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input('Enter the first name: ')
        surname = input('Enter the surname: ')
        speciality = input('Enter the speciality: ')
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input('Input: ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            first_name, surname, speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    name_exists = True # save time and end the loop
                    # break
            #ToDo6
            if not name_exists:# add the doctor ...
                doctors.append(Doctor(first_name, surname, speciality))   # ... to the list of doctors
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            while True:
                print('Choose the field to be updated:')
                print(' 1 First name')
                print(' 2 Surname')
                print(' 3 Speciality')
                op = int(input('Input: ')) # make the user input lowercase

                #ToDo8
                if op == 1:
                    first_name = input('Enter the new first name: ')
                    doctors[index].set_first_name(first_name)
                    print('First name updated successfully')
                    break

                elif op == 2:
                    surname = input('Enter the new surname: ')
                    doctors[index].set_surname(surname)
                    print('Surname updated successfully')
                    break

                elif op == 3:
                    speciality = input('Enter the new speciality: ')
                    doctors[index].set_speciality(speciality)
                    print('Speciality updated successfully')
                    break
                else:
                    print('Invalid Option!')


        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
            #ToDo9
            if self.find_index(doctor_index,doctors):
                del doctors[doctor_index]
                print('Doctor deleted.')
            else:
                print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name())
                print(f'The patient {patients[patient_index].full_name()} is now assign to doctor {doctors[doctor_index].full_name()}.')
                

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')
 
    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        #ToDo12
        try:
            patient_index = int(input('Please enter the patient ID: '))-1
            if patient_index < len(patients):
                discharge_patients.append(patients.pop(patient_index))
                print(f'Patient with ID {patient_index+1} discharged successfully.') 
            else:
                print('Invalid patient ID. Try again.')
        except ValueError:
            print('Invalid patient ID. Try again.')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        if len(discharged_patients) == 0:
            print('No discharged patients')
        else:
            print("-----Discharged Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            #ToDo13
            self.view(discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            username = input('Enter the new username: ')
            if username:
                self.__username = username
                self.save_to_file()
                print('Username updated successfully.')

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                self.save_to_file()
                print('Password updated successfully.')

        elif op == 3:
            #ToDo15
            address = input('Enter the new address: ')
            if address:
                self.__address = address
                self.save_to_file()
                print('Address updated successfully.')
        
        else:
            #ToDo16
            print('Invalid Option!')

    def group_by_family(self, patients):
        print('-----Family Group-----')
        families = {}
        for patient in patients:
            surname = patient.get_surname()
            if surname not in families:
                families[surname] = []
            families[surname].append(patient)

        for surname,members in families.items():
            print(f'\nFamily: {surname}')
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            for i,patient in enumerate(members, 1):
                print(f'{i:2} |{patient}')

    def relocate_patient(self, patients, doctors):
   
  
        print("-----Relocate Patient-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        try:
            patient_index = int(input('Enter the ID of the patient to relocate: ')) - 1

            if patient_index not in range(len(patients)):
                print('The patient ID entered was not found.')
                return

        except ValueError:
            print('Invalid input. Please enter a valid patient ID.')
            return

        print("-----Doctors Available-----")
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)

        try:
            new_doctor_index = int(input('Enter the ID of the new doctor: ')) - 1

            if new_doctor_index not in range(len(doctors)):
                print('The doctor ID entered was not found.')
                return

            # Assign the new doctor
            old_doctor = patients[patient_index].get_doctor()
            if old_doctor == 'Not Assigned':
                print('This is your first time assigned to doctor')

            else:
                new_doctor = doctors[new_doctor_index].full_name()
                patients[patient_index].link(new_doctor)

                print(f'Patient {patients[patient_index].full_name()} has been relocated from {old_doctor} to {new_doctor}.')

        except ValueError:
            print('Invalid input. Please enter a valid doctor ID.')

    def schedule_appointment(self, doctors, patients):
        print("-----Schedule Appointment-----")
        
        # Display patients
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        
        # Select patient
        try:
            patient_id = int(input("Enter patient ID: ")) - 1
            if patient_id < 0 or patient_id >= len(patients):
                print("Invalid patient ID.")
                return
            patient = patients[patient_id]
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        # Display doctors
        print("-----Doctors-----")
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        
        # Select doctor
        try:
            doctor_id = int(input("Enter doctor ID: ")) - 1
            if doctor_id < 0 or doctor_id >= len(doctors):
                print("Invalid doctor ID.")
                return
            doctor = doctors[doctor_id]
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        # Enter date
        date = input("Enter appointment date (YYYY-M-D): ")
        if len(date) != 8 or date[4] != '-' or date[6] != '-':
            print("Invalid date format. Use YYYY-M-D.")
            return
        
        time = input("Enter appointment time (H:M, 12-hour format(H:M AM/PM)): ")
        if len(time) != 7 or time[1] != ':' or not time[:1].isdigit() or not time[2:4].isdigit() or time[5:].upper() not in ['AM', 'PM']:
            print("Invalid time format. Use H:M (12-hour format)(AM/PM).")
            return
        
        # Create and add appointment
        appointment = {'Date': date, 'Time': time,'Patient': patient.full_name()}
        doctor.get_appointments().append(appointment)
        print(f"Appointment scheduled for {patient.full_name()} with {doctor.full_name()} on {date} at {time}.")
        
    def generate_management_report(self, doctors, patients):
        while True:
            print('\n-----Management Report-----')
            print(' 1- Total Doctors')
            print(' 2- Patient per doctor')
            print(' 3- Appointment per month per doctor')
            print(' 4- Patient by illness type')
            print(' 5- Return to Main Menu')

            op = input('Enter option: ')
            if op == '1':
                print(f'\n1. Total Doctors: {len(doctors)}')
            
            elif op == '2':
                print("\nPatients per doctor:")
                
                # Collect data
                doctor_patient_count = {}  # Dictionary to store doctor names and patient count

                for doctor in doctors:
                    doctor_name = doctor.full_name()
                    count = sum(1 for patient in patients if patient.get_doctor() == doctor_name)
                    doctor_patient_count[doctor_name] = count

                # Display the data in a table format
                if doctor_patient_count:
                    print("\n--------------------------------------------")
                    print("|      Doctor Name       |  No. of Patients |")
                    print("---------------------------------------------")

                    for doctor_name, count in doctor_patient_count.items():
                        print(f"| {doctor_name:<22} | {count:^16} |")

                    print("---------------------------------------------")
                else:
                    print("No patients assigned to doctors yet.")
                

            elif op == '3':
                    print("\n3. Appointments per month per doctor:")

                    for doctor in doctors:
                        appointments = doctor.get_appointments()
                        monthly_counts = {}

                        # Process appointment dates
                        for appt in appointments:
                            date = appt.get('Date')
                            if date:
                                month = date.split('-')[1]  # Extract month (Assuming format: YYYY-MM-DD)
                                monthly_counts[month] = monthly_counts.get(month, 0) + 1

                        # Display appointment data in table format
                        if monthly_counts:
                            print(f"\nAppointments for {doctor.full_name()}:")
                            print("------------------------------------")
                            print("|      Month      | No. of Appointments |")
                            print("------------------------------------")
                            
                            for month in sorted(monthly_counts.keys()):
                                print(f"|      {month:<10} | {monthly_counts[month]:^20} |")

                            print("------------------------------------")
                        else:
                            print(f'  - {doctor.full_name()}: No appointments')

            elif op == '4':
                print("\n4. Patients by Illness Type:")

                # Dictionary to store illness categories and patient count
                illness_categories = {
                    'Infectious': 0,
                    'Non-Infectious': 0,
                    'Chronic': 0
                }

                # Count patients per category
                for patient in patients:
                    illness_type = patient.get_illness_type()
                    if illness_type in illness_categories:
                        illness_categories[illness_type] += 1

                # Display patient distribution in a table format
                if sum(illness_categories.values()) > 0:
                    print("\n-------------------------------------------")
                    print("|   Illness Category    | No. of Patients |")
                    print("-------------------------------------------")

                    for category, count in illness_categories.items():
                        print(f"| {category:<18}    | {count:^16}|")

                    print("-------------------------------------------")
                else:
                    print("No patients available for categorization.")
            else:
                break

    def view_diagram(self, doctors, patients):
        while True:
            print(' 1- View diagram of Patients per doctor') 
            print(' 2- View diagram of Appointments per month doctor')
            print(' 3- View diagram of Patients per illness type')
            print(' 4- Return to menu')
            
            op = input('Enter Option: ')

            if op == '1':
                
                print("\nPatients per doctor:")
                doctor_names = []
                patient_counts = []
                
                # Collect data
                for doctor in doctors:
                    doctor_name = doctor.full_name()
                    count = sum(1 for patient in patients if patient.get_doctor() == doctor_name)
                    doctor_names.append(doctor_name)
                    patient_counts.append(count)
                
                # Generate Bar Chart
                if sum(patient_counts) > 0:
                    plt.figure(figsize=(6, 4))
                    bars = plt.bar(doctor_names, patient_counts)
                    plt.title("Patients per Doctor")
                    plt.xlabel("Doctors")
                    plt.ylabel("Number of Patients")
                    plt.xticks(rotation=45, ha='right')
                    
                    # Add value labels on top of bars
                    for bar in bars:
                        height = bar.get_height()
                        plt.text(bar.get_x() + bar.get_width()/2., height,
                                f'{height}',
                                ha='center', va='bottom')
                    
                    plt.tight_layout()
                    plt.show()
                else:
                    print("No patients to display chart.")

            elif op == '2':
                print("\n3. Appointments per month per doctor:")
                for doctor in doctors:
                    appointments = doctor.get_appointments()
                    monthly_counts = {}
                    
                    for appt in appointments:
                        date = appt.get('Date')
                        if date:
                            month = date.split('-')[1]
                            monthly_counts[month] = monthly_counts.get(month, 0) + 1
                    
                    # Generate Bar Chart for each doctor
                    if monthly_counts:
                        months = sorted(monthly_counts.keys())
                        counts = [monthly_counts[m] for m in months]
                        
                        plt.figure(figsize=(6, 3))
                        bars = plt.bar(months, counts)
                        plt.title(f"Appointments for {doctor.full_name()} by Month")
                        plt.xlabel("Month")
                        plt.ylabel("Number of Appointments")
                        
                        # Add value labels
                        for bar in bars:
                            height = bar.get_height()
                            plt.text(bar.get_x() + bar.get_width()/2., height,
                                    f'{height}',
                                    ha='center', va='bottom')
                        
                        plt.tight_layout()
                        plt.show()
                    else:
                        print(f'  -{doctor.full_name()}: No appointments')

            elif op == '3':

            
                print("\n4. Patients by Illness Type:")
                illness_categories = {
                    'Infectious': 0,
                    'Non-Infectious': 0,
                    'Chronic': 0
                }
                
                # Count patients per category
                for patient in patients:
                    illness_type = patient.get_illness_type()
                    if illness_type in illness_categories:
                        illness_categories[illness_type] += 1
                
                # Prepare chart data
                categories = list(illness_categories.keys())
                counts = list(illness_categories.values())
                
                # Generate Bar Chart
                if sum(counts) > 0:
                    plt.figure(figsize=(6, 4))
                    bars = plt.bar(categories, counts, color=['#ff9999','#66b3ff','#99ff99'])
                    plt.title("Patients by Illness Type")
                    plt.xlabel("Illness Category")
                    plt.ylabel("Number of Patients")
                    
                    # Add value labels
                    for bar in bars:
                        height = bar.get_height()
                        plt.text(bar.get_x() + bar.get_width()/3., height,
                                f'{height}',
                                ha='center', va='bottom')
                    
                    plt.show()
                else:
                    print("No patients to display chart.")

            elif op == '4':
                break
            else:
                print('Invalid Option!')
            
    def load_patients_from_file(self, filename):
        """Reads patient records from a file, prints them, and returns them as a list."""
        
        try:
            with open(filename, 'r') as file:
                patient_list = [line.strip() for line in file]  # Strip newline characters

            if patient_list:
                print("Patient Records:")
                for record in patient_list:
                    print(record)
                print("Patient data loaded from file successfully.")
            else:
                print("File is empty.")

            return patient_list

        except FileNotFoundError:
            print("File does not exist.")
            return []

    def save_patients_to_file(self, filename, patients, mode='a', show_message = True):
        """Writes patient records to a file."""
        
        with open(filename, mode) as file:
            for patient in patients:
                line = f"{patient.get_first_name()} , {patient.get_surname()} , {patient.get_age()} , {patient.get_mobile()} , {patient.get_postcode()} , {patient.get_illness_type()}\n"
                file.write(line)
        if show_message:        
            print("Patients data stored in file successfully")

