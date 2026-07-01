from Person import Person

class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        super().__init__(first_name,surname)
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

        
    def full_name(self) :
        #ToDo1
        return f'Dr. {self.get_first_name()} {self.get_surname()}'

    def get_speciality(self) :
        #ToDo6
        return self.__speciality

    def set_speciality(self, new_speciality):
        #ToDo7
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.patients.append(patient)
    
    def get_appointments(self):
        return self.__appointments
    
    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'

