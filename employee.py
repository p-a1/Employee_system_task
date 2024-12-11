import re
class Employee:
    ID=[]
    def __init__(self, Name, Position, Salary,Email,new):
        self.name=Name
        self.email=Email
        self.position=Position
        self.salary=Salary
        if new:
            i=0
            while True:
                if i not in Employee.ID:
                    break
                i+=1
            self.id=i
            Employee.ID.append(i)
    def show(self):
        print(f'employee name is {self.name}\nEmail: {self.email}\nPosition: {self.position}\nSalary: {self.salary}\n')
        print('*'*50)
    def update(self,new_value,target_value):
        if target_value=='name':
            self.name=new_value
        elif target_value=='position':
            self.position=new_value
        elif target_value=='email':
            self.email=new_value
        else:
            self.salary=new_value
    def get_id(self):
        return self.id
    def set_id(self,id):
        self.id=id
    def list_data(self):
        return['employee',self.get_id(),self.name, self.position, self.salary,self.email]
    @staticmethod
    def set_Ids(value):
        Employee.ID=value
    @staticmethod
    def del_id(id):
        print(Employee.ID)
        Employee.ID.remove(id)




def check_email():
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        try:
            email=input('enter your email: ')
            if bool(re.match(email_regex,email)):
                return email 
            else:
                print('not valid!!')
        except:
            print('invalid email!!')
def check_salay():
    while True:
        try:
            salary=int(input('Enter the salary'))
            if salary>0:
                return [salary,'salary']
        except:
            print('Enter vaild salary!!')