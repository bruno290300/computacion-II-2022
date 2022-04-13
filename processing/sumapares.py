import argparse, os, time


parser = argparse.ArgumentParser()

parser.add_argument("-n","--num",type = int, help="procesos hijos que quiere generar")
parser.add_argument("-v", "--verbose",action= "store_true",help= "Modo verboso")

args = parser.parse_args()


def child():
    if os.fork() == 0:
        suma = sum([i for i in range(os.getpid()) if i % 2 == 0])
        if modo_verboso == True:
            print ("Starting process " f'{os.getpid()}')
            print ({os.getpid()}, "-", {os.getppid()},":", {suma}) 
            print ("Ending process " f'{os.getpid()}')

        else:
            print ({os.getpid()}, "-", {os.getppid()},":", {suma}) 
        
        os._exit(0)

modo_verboso = False


if args.verbose:
    modo_verboso = True

if args.num > 0:
    for i in range(args.num):
        child()
    for i in range (args.num):
        os.wait()



