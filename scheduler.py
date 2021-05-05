import schedule # run command 'pip install schedule'
import time
import os
import shutil



def copy_files(destination): # Function that takes destination as argument and copies all files to that destination
    files = os.listdir('A')
    print('copying.....')
    for f in files:
        if f != 'e.txt':
            shutil.copy('A/'+f, destination)
            print(f)
    print('Done.........')

def first(): # function to perform first copy function , ie; copy to 'B'
    os.mkdir("B")
    copy_files('B')

def task(): # function to perform the basic task
    ts = str(time.time())
    os.mkdir(ts)
    copy_files(ts)
    
def task_monthly():
    if date.today().day == 1:
        ts = str(time.time())
        os.mkdir(ts)
        copy_files(ts)


first() # One time
schedule.every().minutes.do(task) # Every minute
schedule.every().hour.do(task) # Every Hour
schedule.every().week.do(task) # Every week
schedule.every().day.do(task) # Daily
schedule.every().day.do(task_monthly) # Monthly

while True:
  
    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)




