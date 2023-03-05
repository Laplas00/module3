from threading import Thread, Condition
from time import sleep
import logging


logging.basicConfig(level=logging.ERROR, format='%(threadName)s %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def timer(th):

    timer = 0.0
    while th:
        sleep(0.1)
        timer+=0.1
        timer = round(timer,2)
        print(f'-----------Secunds - {timer}', end='\r')
    print('Finish')

        
def cycle(num):
    a = 0
    for i in range(num):
        res = num*400-900/30*0.3*0.2          
        a += 1
        print(a,end='\r')

type()
int()

if __name__ == '__main__':
    threads = []
    condition = Condition()
    
    th = Thread(target=cycle, args=(999999,),)
    
    t_imer = Thread(target=timer, args=(condition,))
    threads.append(th)
    threads.append(t_imer)
    th.start()
    t_imer.start()
    

