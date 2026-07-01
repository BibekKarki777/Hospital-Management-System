
from Person import Person
class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, illness_type):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        super().__init__(first_name,surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'Not Assigned'
        self.__symptoms = ['Hypertension', 'Ear Infection', 'Chest Discomfort']
        self.__illness_type = illness_type
       
    


    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return f'{self.get_first_name()} {self.get_surname()}'
    
    def get_age(self):
        return self.__age
    
    def get_mobile(self):
        return self.__mobile
    
    def get_postcode(self):
        return self.__postcode
    
    def get_doctor(self) :
        #ToDo3
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        print('------Symptoms------')
        for index,symptom in enumerate(self.__symptoms, start=1):
            print(f'{index}. {symptom}')

    def get_illness_type(self):
        return self.__illness_type

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'

