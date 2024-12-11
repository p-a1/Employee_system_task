import csv
from employee import Employee,check_email,check_salay
from employeeManeger import Manager
import os
import time


#function exists in this file
#1.check_authantication
#2.load_data
#3.showList
#4.choces
#5.update_list
#6.add_employee
#7.save_data
#8.main

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
Time=5  
#this function is to check if the user is authanticated
def check_authantication(managers,email,password):
    founded=False
    for i in managers.items():
        if i[1].check_password(password) and i[1].check_email(email):
            founded=True
    return founded

#this function is to  load the data from the csv file
def load_data(file):
    employees=dict()
    managers=dict()
    ids=list()
    reader= csv.reader(file)
    for row in reader:
        if len(row)>1:
            if row[0]=='employee':
                employees[int(row[1])]=Employee(*row[2:],new=False)
                employees[int(row[1])].set_id(int(row[1]))
                ids.append(int(row[1]))
            elif row[0]=='manager':
                managers[int(row[3])]=Manager(row[1],row[2],*row[4:],new=False)
                managers[int(row[3])].set_id(int(row[3]))
                ids.append(int(row[3]))
            
    Employee.set_Ids(ids)
    return employees,managers

#this function is to show the list that the program can do
def showList():
    print('ente the number that is oposite to your choce:',
          '\nNew Employee','1'.rjust(13),
          '\nList all employees','2'.rjust(7),
          '\nUpdate employee','3'.rjust(10),
          '\nDelete Employee','4'.rjust(10),
          '\nEnd the program','5\n'.rjust(11) ,end='')
    while(1):
        try:
            print('*'*50)
            choce=int(input('please chooc number: '))
            print('*'*50)
            if choce>0 and choce<6:
                return choce
            else :print('the choce is invalid!!')
        except:
            print('the choce is invalid!!')
    clear_console()

#this function is to choose from the list that is the program can do
def choces(choce,employees):
    if choce==1:
        employee=add_employee()
        employees[employee.get_id()]=employee
        print('\nemployee added')
        time.sleep(Time)
        clear_console()
        return 1
    elif choce==2:
        for enum,i in enumerate(employees.items()):
            print(f'employee {enum+1} whith id {i[1].get_id()}')
            i[1].show()
            close=0
        while close !='q':
            close=input('to close enter q: ')
        clear_console()
        return 1
    elif choce==3 or choce==4:
        Id=-1
        employee=0
        while(True):
            try:
                Id=int(input('Enter the employee id: '))
                employees[Id]
                break
            except:
                print('not found!!')
        if choce==3:
            print('*'*50)
            values=update_list()
            if not values[0]: # type: ignore
                return 1
            else:
                employees[Id].update(*values) # type: ignore
                print(f'employee with {Id} updated')
                time.sleep(Time)
                clear_console()
                return 1
        if choce==4:
            del(employees[Id])
            Employee.del_id(Id)
            print('*'*50)
            print(f'employee with id {Id} deleted')
            print(f'employee with {Id} deleted')
            time.sleep(Time)
            clear_console()
            return 1
    else:
        return 0
        
#this function is to deal with the update option
def update_list():
    print('ente the number that is oposite to the attribute you want to udate:',
          '\nName','1'.rjust(13),
          '\nemail','2'.rjust(12),
          '\nsalary','3'.rjust(11),
          '\nposition','4'.rjust(9),
          '\nnothing else','5\n'.rjust(6) ,end='')
    choce=-1
    while(1):
        try:
            print('*'*50)
            choce=int(input('please chooc number: '))
            print('*'*50)
            if choce>0 and choce<5:
                break
            else :print('the choce is invalid!!')
        except:
            print('the choce is invalid!!')
    if choce==1:
        name=input('enter the new name: ')
        return [name,'name']
    elif choce==2:
        email=check_email()
        return [email,'email']
    elif choce==3:
        return check_salay()
    elif choce==4:
        position=input('enter the position: ')
        return [position,'position']
    else:return {False}

#this function is to add employee data
def add_employee():
    name=input('Enter the name of the employee: ')
    position=input('Enter the position of the employee: ')
    email=check_email()
    salary=input('Enter the salary of the employee: ')
    employeee=Employee(name,position,salary,email,True)
    print(employeee.get_id())
    return employeee
#this function is to write the data to the file
def save_data(file,employees,managers):
    writer=csv.writer(file)
    data=employees | managers
    writer.writerows([i.list_data() for i in data.values()])
    file.close()
    
    
    
    
def main():
    print('*'*50)
    print('PROGRAM STARTED'.center(50))
    print('\n')
    file=open('data.csv','r')
    employees,managers=load_data(file)
    exist=False
    for i in range(3):
        print('*'*50)
        email=input('please enter the email: ')
        password=input('please enter the password: ')
        print('*'*50)
        exist=check_authantication(managers,email,password)
        if exist:
            break
    if(not exist):
        print('you are not authanticated')
        exit() # type: ignore
    clear_console()
    while True:
        choce=showList()
        choce=choces(choce,employees)
        if not choce :
            break
    file.close()
    print(' THANK YOU FOR USE OUR PROGRAM'.center(50))
    print('*'*50)
    time.sleep(Time)
    file=open('data.csv','w',newline='', encoding='utf-8')
    save_data(file,employees,managers)
    exit()         
main()