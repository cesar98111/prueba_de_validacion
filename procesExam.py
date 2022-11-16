from multiprocessing import Process
import os
from datetime import datetime
from time import sleep

def hijo():
    print("Iniciando el proceso PID: ",os.getpid())
    sleep(3)
    
    print("terminando proceso con PID: ",os.getpid())
    os._exit(0)

def padre():
    n = 1

    while n <= 10:
        p = Process(target=hijo)
        p.start()
        now = datetime.now()

        print("nuevo hijo creado con pid ",p.pid, "a las ",now.hour,":",now.minute,":",now.second)
        sleep(10)
        p.join()
        
        n=n+1








if __name__=='__main__':
    padre()