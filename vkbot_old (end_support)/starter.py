# Функция рестарта бота в случае краша
from subprocess import run
from time import sleep

file_path = "main.py" 

restart_timer = 2
def start_script():
    try:
        print("Process running.")
        run(["python3",file_path], check=True) 
    except:
        print("Process crashed.")
        handle_crash()

def handle_crash():
    sleep(restart_timer)
    start_script()

start_script()