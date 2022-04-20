import os, argparse, string, time

parser = argparse.ArgumentParser()

parser.add_argument('-n', type=int, help="Genera una cantidad de procesos según el número ingresado")
parser.add_argument('-r', type=int, help="Almacena en el archivo su letra según el número ingresado")
parser.add_argument('-f', help="Path del archivo a trabajar")
parser.add_argument('-v', action="store_true", help="Ingresa en modo verboso")

args = parser.parse_args()

file = open(args.f, 'w+')

abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

for i in range(args.n):
    if os.fork() == 0:
        if args.v:
            print(f"Proceso{os.getpid()} escribiendoletra '{abc[i]}'")
        for r in range(args.r):
            file.write(abc[i])
            file.flush()
        time.sleep(1)
        os._exit(0)


for i in range(args.n):
    os.wait()
file2 = open(args.f, 'r')
print(file2.readlines())