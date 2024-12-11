from employee import Employee
class Manager(Employee):
    def __init__(self,email,password, Name, Position, Salary,new):
        super().__init__( Name, Position, Salary,email,new)
        self.id=id
        self.password=password
    def check_email(self,email):
        if self.email==email:
            return True
    def check_password(self,password):
        if self.password==password:
            return True
    def list_data(self):
        return['manager',self.email,self.password,self.get_id(),self.name, self.position, self.salary]