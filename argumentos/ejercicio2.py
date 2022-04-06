import os, argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', "--source_file", type=str, required=True, help=" archivo origen")
parser.add_argument('-o', "--destiny_file", type=str, help="archivo destino")

args = parser.parse_args()


if os.path.isfile(args.origen):
    archivo = open(args.origen, "r")
    escritura = archivo.read()
    archivo.close()
    archivo2 = open(args.destino,"a+")
    archivo2.write(escritura)
    archivo2.close()
    print ("Se ha sobreescrito el archivo origen por el archivo destino")

