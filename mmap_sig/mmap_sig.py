import os, argpase, time, signal, sys, os


def Main():
    parser = argparse.ArgumentParser(description="Comandos a utilizar")
    parser.add_argument("-f","--function",type=str, help="Ingresar archivo a buscar")
    global args
    args = parser.parse_args()
    path(args.function)
    generator(args.function)



def generator(args):
    global list_pid
    list_pid = []
    global mapeo
    mapeo = mmap.mmap(-1,1024)
    print("El padre espera señales")
    for i in range(2):
        ret = os.fork()
        if ret == 0:
            if i == 0:
                for i in sys.stdin:
                    if i[:3] == "bye":
                        os.kill(os.getpid(), signal.SIGUSR2)
                        print(" el padre muere..")
                        sys.exit(0)
                    mapeo.write(i.encode())
                    os.kill(os.getppid(),signal.SIGUSR1)
            
            else:
                signal.signal(signal.SIGUSR1, handler_hijo)
                signal.signal(signal.SIGUSR2, handler_hijo)
                while True:
                    signal.pause()
        else:
            list_pid.append(ret)

    signal.signal(signal.SIGUSR1, handler_padre)
    signal.signal(signal.SIGUSR2, handler_padre)
    signal.pause()
    os.wait()

def handler_padre(s,f):
    if s == signal.SIGUSR1:
        reading = mapeo.readline().decode()
        print(reading)
        time.sleep(1)
        os.kill(list_pid[1],signal.SIGUSR1)
    elif s == signal.SIGUSR2:
        os.kill(list_pid[1], signal.SIGUSR2)
        os.wait()
        sys.exit(0)


def handler_hijo(s,f):
    if s == signal.SIGUSR1:
        reading = mapeo.readline().decode().upper()
        fd = open(args.function, "a")
        fd.write(reading)
        fd.close()
        print("Hijo 2 lee:",reading)
    elif s == signal.SIGUSR2:
        print("Hijo 2 muriendo...")
        sys.exit(0)



def path(args):
    
    if os.path.exists(args):
        pass
    else:
        file = open(args,"w")
        file.close()

if __name__ == "__main__":
    Main()