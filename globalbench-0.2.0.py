import time

global integer
global fp

version = "0.2.0"

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

def algoint():
    global integer
    start_time = time.time()

    for x in range(90900900): #Noventa millones
        resultado0 = 10 * x
        resultado1 = 10 + x
        resultado2 = 10 - x
        # print(resultado0)
        # print(resultado1)
        # print(resultado2)

    integer = ("%s" % (time.time() - start_time))
    stop_time = time.time()

    print("---",integer+"s ---")

def algoflp():
    global fp
    start_time = time.time()

    for x in range(90900900): #Noventa millones
        resultado = 10 / 0x5F3759DF * (1 + x)
        #print(resultado)

    fp = ("%s" % (time.time() - start_time))
    stop_time = time.time()

    print("---", fp + "s ---")

if __name__ == '__main__':
    print("Globalbench v"+version)
    print("Integer Benchmark...")
    algoint()
    print("FP Benchmark...")
    algoflp()
    punt()
