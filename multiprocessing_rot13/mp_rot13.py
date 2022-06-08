from multiprocessing import Process, Pipe, Queue
import multiprocessing
import os, time, sys, codecs


def hijo1(p,q):
    sys.stdin = open(0)
    print("Ingrese una linea:")
    line = sys.stdin.readline()
    p.send(line)
    p.close()
    print("Hijo 1 lee:",line)
    time.sleep(2) 
    line_codec = q.get()
    print("Hijo 1 lee mensaje encriptado:",line_codec)
    
    
def hijo2(p,q):
    line = str(p.recv())
    print("Hijo 2 lee:",line)
    time.sleep(2)
    line_codec = codecs.encode(line,'rot_13')
    q.put(line_codec)


if __name__ == "__main__":
    a,b = multiprocessing.Pipe()
    q = multiprocessing.Queue()
    p1 = Process(target=hijo1, args=(a,q))
    p2 = Process(target=hijo2, args= (b,q))    
    p1.start()
    p2.start()
    p1.join()
    p2.join()

