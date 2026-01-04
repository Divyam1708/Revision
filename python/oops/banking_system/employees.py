from banking_system.banks import Bank

class Employee(Bank):
    employee_count=1

    def __init__(self,name,e_id,age,salary,position,commisioned_on,bank_id):
        self.employee_count=Employee.employee_count
        self.e_id=e_id
        self.name=name
        self.age=age
        self.salary=salary
        self.position=position
        self.commisioned_on=commisioned_on
        self.bank_id=bank_id
        Employee.employee_count+=1
    
    def __str__(self):
        return (f'{self.id} : {self.name}')
    
    # @classmethod
    def create_object(cls):
        name=input('Enter name: ')
        return cls(name)
    
