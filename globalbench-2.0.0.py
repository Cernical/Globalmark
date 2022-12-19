#!/usr/bin/python3

import time
import platform     #System info
import os
from multiprocessing import Process

global integer
global fp

version = "2.0.0"
nucleos = "1"

def punt():
    global integer
    global fp

    puntmax = 1000000

    intinteger = float(integer)
    intfp = float(fp)

    puntint = puntmax / intinteger
    puntfp = puntmax / intfp

    print()
    print("Integer score:",round(puntint))
    print("FP score:",round(puntfp))

def algoint(nucleos):
    global integer

    def op1():
        #print()
        #print('process id:', os.getpid())
        for x in range(90900900):  # Noventa millones
            resultado0 = 10 * x
            #print(resultado0)
        #print("Fin op1")

    def op2():
        #print('process id:', os.getpid())
        for x in range(90900900):  # Noventa millones
            resultado1 = 10 + x
            #print(resultado1)
        #print("Fin op2")

    def op3():
        #print('process id:', os.getpid())
        #print()
        for x in range(90900900):  # Noventa millones
            resultado2 = 10 - x
            #print(resultado2)
        #print("Fin op3")

    if nucleos == "0":
        start_time = time.time()
        for x in range(90900900):  # Noventa millones
            resultado0 = 10 * x
            resultado1 = 10 + x
            resultado2 = 10 - x
            # print(resultado0)
            # print(resultado1)
            # print(resultado2)
    else:
        start_time = time.time()
        p = Process(target=op1)
        p.start()
        p2 = Process(target=op2)
        p2.start()
        p3 = Process(target=op3)
        p3.start()

        p.join()
        p2.join()
        p3.join()

    integer = ("%s" % (time.time() - start_time))
    stop_time = time.time()

    print("---",integer+"s ---")

def algoflp(nucleos):
    global fp

    def op1():
        for x in range(90900900):  # Noventa millones
            resultado1 = 10 / 0x5F3759DF * (1 + x)

    def op2():
        for x in range(90900900):  # Noventa millones
            resultado2 = 3.141592653589793 / (1 + x)

    if nucleos == "0":
        start_time = time.time()
        for x in range(90900900):  # Noventa millones
            resultado1 = 10 / 0x5F3759DF * (1 + x)
            resultado2 = 3.141592653589793 / (1 + x)
            # print(resultado1)
            # print(resultado2)
    else:
        start_time = time.time()
        p = Process(target=op1)
        p.start()
        p2 = Process(target=op2)
        p2.start()

        p.join()
        p2.join()

    fp = ("%s" % (time.time() - start_time))
    stop_time = time.time()

    print("---", fp + "s ---")

if __name__ == '__main__':
    print("Globalbench v"+version)
    print()

    if platform.processor() == "":
        print("CPU:", "Undisclosed")
    else:
        print("CPU:", platform.processor())
    print("System:", platform.system())
    print("Python:", platform.python_version())
    print("Compiler:", platform.python_compiler())

    print()
    nucleos = input("Choose Single-Core (0) or Multi-Core (1): ")
    print()

    print("Integer Benchmark...")
    algoint(nucleos)
    print("FP Benchmark...")
    algoflp(nucleos)
    punt()
