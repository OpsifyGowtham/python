import os
import datetime

def run_command(command): 
    print(os.system(command))
    
def show_date():
    today = datetime.date.today()
    print("Today's date is:", today)
    
show_date()