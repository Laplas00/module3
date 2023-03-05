from threading import Thread
from time import sleep




def sobaka(arg):
    print('gav gav '+arg)
    sleep(2)


def cat(arg):
    print('meow '+arg)
    sleep(2)


if __name__ == '__main__':
    for i in range(5):
        th = Thread(target=sobaka,args=['larisa',])
        tb = Thread(target=cat,args=['larisa',])
        th.start()
        tb.start()
    
    sleep(4)

