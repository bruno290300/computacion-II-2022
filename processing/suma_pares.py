import os, argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n","--num",type = int, help=" Procesos hijos que se quiere generar")
parser.add_argument("-v", "--verbose",action= "store_true",help= "modo verboso")
args = parser.parse_args()


def child():
    if os.fork():
        sumapares = sum([i for i in range(os.getpid()) if i % 2 == 0])
        if modo_verboso:
            print("Starting process")
            print(f'{os.getpid()} - {os.getppid()}: {sumapares}')
            print("Ending process")
        else:
            print(f'{os.getpid()} - {os.getppid()}: {sumapares}')
            os._exit(0)

modo_verboso=True


for i in range(args.num):
    child()
    