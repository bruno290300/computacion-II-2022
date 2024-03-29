import os, sys, threading, codecs
from multiprocessing import Queue



def th_function1(queue1,queue2):
    print("Hilo 1")
    sys.stdin = open(0)
    print("Ingrese una linea:")
    line = sys.stdin.readline()
    queue1.put(line)
    line_codec = queue2.get()
    print(f"Hilo 1 recibe mensaje encriptado:{line_codec}")


def th_function2(queue1,queue2):
    data = queue1.get()
    print(f"Hilo 2 recibe mensaje: {data}")
    line_codec = Rot13(data)
    print("Hilo 2 almacena mensaje encriptado..")
    queue2.put(line_codec)


def Rot13(line):
    line_codec = codecs.encode(line,'rot13')
    return line_codec


if __name__ == '__main__':
    qv1 = Queue()
    qv2 = Queue()
    th1 = threading.Thread(target = th_function1,args=(qv1,qv2), daemon = True)    
    th2 = threading.Thread(target = th_function2,args=(qv1,qv2), daemon = True)
    th1.start()
    th2.start()
    th1.join()
    th2.join()


