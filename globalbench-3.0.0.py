#!/usr/bin/python3

import time
import platform     # System info
# import os
from multiprocessing import Process

global integer
global fp

version = "3.0.0"
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
    print("Integer score:", round(puntint))
    print("FP score:", round(puntfp))

def algoint(nucleos):
    global integer

    # Operaciones por proceso de ejecución------------------------------------------------------------------------------
    def op1():
        #print('process id:', os.getpid())
        for x in range(30900900):
            resultado = 10 * x

    def op2():
        for x in range(30900900):
            resultado = 10 + x

    def op3():
        for x in range(30900900):
            resultado = 10 - x

    def op4():
        for x in range(30900900):
            resultado = x * x

    def op5():
        for x in range(30900900):
            resultado = x + x

    def op6():
        for x in range(30900900):
            resultado = x - x

    def op7():
        for x in range(30900900):
            resultado = x * x + x - x

    def op8():
        for x in range(30900900):
            resultado = x - x + x * x

    # Ejecución operaciones---------------------------------------------------------------------------------------------
    if nucleos == "0":
        start_time = time.time()
        for x in range(30900900):  # Cuarenta millones
            resultado = 10 * x
            resultado = 10 + x
            resultado = 10 - x
            resultado = x * x
            resultado = x + x
            resultado = x - x
            resultado = x * x + x - x
            resultado = x - x + x * x
    else:
        start_time = time.time()

        p = Process(target=op1)
        p.start()
        p2 = Process(target=op2)
        p2.start()
        p3 = Process(target=op3)
        p3.start()
        p4 = Process(target=op4)
        p4.start()
        p5 = Process(target=op5)
        p5.start()
        p6 = Process(target=op6)
        p6.start()
        p7 = Process(target=op7)
        p7.start()
        p8 = Process(target=op8)
        p8.start()

        p.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()

    # Fin operaciones---------------------------------------------------------------------------------------------------
    integer = ("%s" % (time.time() - start_time))
    stop_time = time.time()

    print("---",integer+"s ---")

def algoflp(nucleos):
    global fp

    # Operaciones por proceso de ejecución------------------------------------------------------------------------------
    def op1():
        for x in range(30900900):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op2():
        for x in range(30900900):
            resultado = 3.141592653589793 / (1 + x)

    def op3():
        for x in range(30900900):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op4():
        for x in range(30900900):
            resultado = 3.141592653589793 / (1 + x)

    def op5():
        for x in range(30900900):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op6():
        for x in range(30900900):
            resultado = 3.141592653589793 / (1 + x)

    def op7():
        for x in range(30900900):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op8():
        for x in range(30900900):
            resultado = 3.141592653589793 / (1 + x)

    # Ejecución operaciones---------------------------------------------------------------------------------------------
    if nucleos == "0":
        start_time = time.time()
        for x in range(30900900):  # Treinta millones
            resultado = 10 / 0x5F3759DF * (1 + x)
            resultado = 3.141592653589793 / (1 + x)
            resultado = 10 / 0x5F3759DF * (1 + x)
            resultado = 3.141592653589793 / (1 + x)
            resultado = 10 / 0x5F3759DF * (1 + x)
            resultado = 3.141592653589793 / (1 + x)
            resultado = 10 / 0x5F3759DF * (1 + x)
            resultado = 3.141592653589793 / (1 + x)

    else:
        start_time = time.time()
        p = Process(target=op1)
        p.start()
        p2 = Process(target=op2)
        p2.start()
        p3 = Process(target=op3)
        p3.start()
        p4 = Process(target=op4)
        p4.start()
        p5 = Process(target=op5)
        p5.start()
        p6 = Process(target=op6)
        p6.start()
        p7 = Process(target=op7)
        p7.start()
        p8 = Process(target=op8)
        p8.start()

        p.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()

    # Fin operaciones---------------------------------------------------------------------------------------------------
    fp = ("%s" % (time.time() - start_time))
    stop_time = time.time()

    print("---", fp + "s ---")

if __name__ == '__main__':
    print("Globalbench v"+version)
    print()

    if platform.processor() == "":
        print("CPU:", "ARM")
    else:
        print("CPU:", platform.processor())
    print("System:", platform.system())
    print("Python:", platform.python_version())
    print("Compiler:", platform.python_compiler())

    print()
    nucleos = input("Choose Single-Core (0) or Multi-Core (1): ")
    if nucleos == "0": print("Single-Core benchmark:")
    if nucleos != "0": print("Multi-Core benchmark:")
    print()

    print("Integer Benchmark...")
    algoint(nucleos)
    print("FP Benchmark...")
    algoflp(nucleos)
    punt()
