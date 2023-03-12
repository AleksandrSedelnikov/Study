import subprocess

def bash_pid():
    try:
        pid = subprocess.check_output("ps -u | grep bash | grep -v grep | awk '{print $2}'",stderr=subprocess.STDOUT,shell=True, universal_newlines=True)
        f = open('now_bash_pid.txt', 'w')
        f.write("PID terminal: {}".format(pid))
        f.close()
        return 0
    except Exception as e:
        return "Error: {}".format(e)
    

def main():
    result = bash_pid()
    if (result == 0):
        print('Выполнено успешно.')
    else:
        print(result)

if __name__ == "__main__":
    main()

