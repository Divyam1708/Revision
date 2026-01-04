class Bank:
    bank_count=1
    
    @classmethod
    def input_bank_data(cls):
        bank_id:str=input('Enter the Bank ID: ')
        city_code:str=input('Enter the Name of the Bank: ')
        branch:str=input('Enter the Name of the Bank: ')
        max_capacity_of_employees:int=int(input('Enter the Name of the Bank: '))
        established_on=input('Enter the Name of the Bank: ')
        reports_to=input('Enter the ID of the Bank it reports to: ')
        return cls()
    
    def __init__(self,bank_id,city_code,branch,max_capacity_of_employees,established_on,reports_to='None'):
        self.number=Bank.bank_count
        self.bank_id=bank_id
        self.city_code=city_code
        self.branch=branch
        self.max_capacity_of_employees=max_capacity_of_employees
        self.established_on=established_on
        self.reports_to=reports_to
        Bank.bank_count+=1
        
    def __str__(self):
        Info=(f'{self.bank_id} is in ZIP code: {self.city_code} '+
              f'with branch in {self.branch}, '+
              f'and was established in {self.established_on} for maximum working capacity as {self.max_capacity_of_employees} '+
              f'and it reports to {self.reports_to}'
              )
        return Info