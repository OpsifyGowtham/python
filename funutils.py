import os

command = "df -h" #disk
command = "date"  #date

def check_cpu(command): #define a function
    print(os.system(command))
    
check_cpu("df -h") #calling a function

def check_date(command): #define a function
    print(os.system(command))
    
check_date("date") #calling a function

def check_systeminfo(command): #define a function
    return os.system(command)
    
check_systeminfo("systeminfo") #calling a function

def run_command(command): 
    print(os.system(command))
    
run_command("whoami")
run_command("pwd")