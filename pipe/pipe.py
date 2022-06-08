import getopt, sys, os

opt,arg = getopt.getopt(sys.argv[1:], 'f:')

for (op,ar) in opt:
    if op == '-f':
        file_read = ar


def write():
    file = open(file.txt, 'r')
    return file.readlines()

lineas = []


def child(line):
    if not os.fork():
        os.write(w, line[::-1].encode('ascii'))
        os._exit(0)
    else:
        valor = os.read(r, 100)
        lines.append(valor.decode())


if __name__ == '__main__':
    lines = write()
    r, w = os.pipe()
    
    for line in lines:
        child(line)
    
    for line in lines:
        os.wait()

    for line in lineas:
        print(line)