import multiprocessing as mp
from math import sqrt, log10
import os,sys, argparse
import time


def Main():
    parser = argparse.ArgumentParser(description="Programa que extrae elementos de una matriz y calcula la funcion dada")
    parser.add_argument("-p", type=int, help=" Genera un nùmero de procesos.")
    parser.add_argument("-f", type=str, help="Funcion con la matriz a utilizar.")
    parser.add_argument("-c",type=str, help="Operación a realizar.")
    args = parser.parse_args()
    matriz_pool(args)


def matriz_pool(args):
    with open(args.f, "r+") as fd:
        lines = fd.readlines() 
    pool = mp.Pool(processes=args.p)
    
    if args.c == "pot":
        for line in lines:
            resultados = pool.map(pot, line.split())
            print(resultados)

    elif args.c == "raiz":
        for line in lines:
            resultados = pool.map(raiz, line.split())
            print(resultados)

    elif args.c == "log":
        for line in lines:
            resultados = pool.map(log, line.split())
            print(resultados)
    

def pot(num):
    resultado = int(num)**2
    return resultado

def raiz(num):
    resultado = math.sqrt(int(num))
    return resultado

def log(num):
    resultado = math.log10(int(num))
    return resultado



if __name__ == "__main__":
    Main()