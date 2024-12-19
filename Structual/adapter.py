from abc import ABC, abstractmethod

# Older format
class StudentV1:
    
    def __init__(self, name:str, surname:str, phone:str):
        self.name = name
        self.surname = surname
        self.phone = phone

# New format
class IStudent(ABC):
    
    @abstractmethod
    def get_data(self):
        raise NotImplementedError

class StudentV2(IStudent):
    
    def __init__(self, first_name:str, last_name:str, phone:str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
    
    def get_data(self):
        print(self.first_name, self.last_name, self.phone)

# Adapter to adapt older format into new format. 
class StudentAdapter(IStudent):
    
    def __init__(self, old_student):
        self.old_student:StudentV1 = old_student
    
    def get_data(self):
        print(self.old_student.name, self.old_student.surname, self.old_student.phone)
        

def run():
    new_students = [
        StudentV2("Mohit", "Tanwani", "8490"),
        StudentV2("Vishal", "Tanwani", "2890"),
    ]
    
    migrated_students = [
        StudentV1("Pratibha", "Hotwani", "8780")
    ]
    
    all_students = new_students.copy()
    for student in migrated_students:
        all_students.append(StudentAdapter(student))
        
    for student in all_students:
        student.get_data()
        
if __name__ == "__main__":
    run()