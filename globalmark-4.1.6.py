#!/usr/bin/python3

# Basic-----------------------------------------------------------------------------------------------------------------
import time
import platform  # System info
import os
import signal
from multiprocessing import Process
import subprocess  # Necesario para usar el sistema y sus funciones
# ----------------------------------------------------------------------------------------------------------------------

global integer
global fp
global puntint
global puntfp
global legacy

# Importacion Pymongo---------------------------------------------------------------------------------------------------
try:
    from pymongo import MongoClient, DESCENDING
    legacy = 0
except:
    print("Pymongo not found, you can install it with 'pip3 install pymongo'")
    print()
    input("Continue without database connection, press enter to continue: ")
    legacy = 1

# Importacion Kivy framework--------------------------------------------------------------------------------------------
try:
    # Kivy--------------------------------------------------------------------------------------------------------------
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.textinput import TextInput
    from kivy.uix.boxlayout import BoxLayout
    from random import randrange
    from kivy.uix.image import Image

    # Cambiar color ventana
    from kivy.core.window import Window
    Window.clearcolor = (0.6, 0.2, 0.2, 1)

    UI = 1
except:
    print("Kivy not found, running on CMD based interface.")
    print()
    input("Press enter key to continue: ")
    UI = 0

# Configuracion basica--------------------------------------------------------------------------------------------------
version = "4.1.6"
nucleos = "1"
rangobucle = 30900900
stresstest = "0"
# ----------------------------------------------------------------------------------------------------------------------

clear = lambda: subprocess.call('cls||clear', shell=True)  # Llamada al sistema

def mangodb(usuario, modo, puntint, puntfp, modoRW, arquitectura):
    # Dirección base de datos y credenciales
    uri = "mongodb+srv://cliente:globalbench88@globalbenchdb.morfhwo.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)   #Declaración cliente

    # Base de datos y contenido
    db = client.GlobalbenchDB
    coll = db.GlobalbenchColl

    # Modo de escritura
    if modoRW == 1:
        # Introducción de datos para subir
        doc = [
            {"User": usuario, "CPU": arquitectura, "Mode": modo, "Integer Score": puntint, "FP Score": puntfp}
        ]
        result = coll.insert_many(doc)  # Comando de ejecución para subir datos
        # result = coll.update_many({}, doc)

        input("Scores uploaded. Press any key to continue: ")

    # Modo de lectura
    if modoRW == 0:
        clear()
        print("Benchmark Scores")
        print()

        # Mostrar datos
        cursor = coll.find({}, {"_id": 0}).sort("Integer Score", DESCENDING)
        for doc in cursor:
            print(doc)
        print()
        input("Introduce any key to continue: ")

    # Cerrar conexión
    client.close()

def test(stresstest, numeronucleos):

    global modo_gui

    # Operaciones por proceso de ejecución------------------------------------------------------------------------------
    def op1(stresstest):
        while stresstest == "1":
            resultado = 10 * 10 + 10 - 10 / 10 - 10 + 10 * 10

    for i in range(numeronucleos):
        p = Process(target=op1, args=stresstest)
        p.start()
        pid = p.pid
        globals()[f'n{i}'] = pid

    if modo_gui == 0:
        input("Running test... (Enter any key to stop): ")
        for i in range(numeronucleos):
            os.kill(globals()[f'n{i}'], signal.SIGTERM)

    clear()

def punt():
    global integer
    global fp
    global puntint
    global puntfp
    global retornar_puntint
    global retornar_puntfp

    puntmax = 1000000

    intinteger = float(integer)
    intfp = float(fp)

    puntint = puntmax / intinteger
    puntfp = puntmax / intfp

    puntint = round(puntint)
    puntfp = round(puntfp)

    print()
    print("Integer score:", puntint)
    print("FP score:", puntfp)

    retornar_puntint = str(puntint)
    retornar_puntfp = str(puntfp)

    #return(retornar_puntint, retornar_puntfp)

def algoint(nucleos, rangobucle):
    global integer

    # Operaciones por proceso de ejecución------------------------------------------------------------------------------
    def op1():
        # print('process id:', os.getpid())
        for x in range(rangobucle):
            resultado = 10 * x

    def op2():
        for x in range(rangobucle):
            resultado = 10 + x

    def op3():
        for x in range(rangobucle):
            resultado = 10 - x

    def op4():
        for x in range(rangobucle):
            resultado = x * x

    def op5():
        for x in range(rangobucle):
            resultado = x + x

    def op6():
        for x in range(rangobucle):
            resultado = x - x

    def op7():
        for x in range(rangobucle):
            resultado = x * x + x - x

    def op8():
        for x in range(rangobucle):
            resultado = x - x + x * x

    # Ejecución operaciones---------------------------------------------------------------------------------------------
    if nucleos == "0":
        start_time = time.time()
        for x in range(rangobucle):  # Cuarenta millones
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
    #return(integer)

def algoflp(nucleos, rangobucle):
    global fp

    # Operaciones por proceso de ejecución------------------------------------------------------------------------------
    def op1():
        for x in range(rangobucle):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op2():
        for x in range(rangobucle):
            resultado = 3.141592653589793 / (1 + x)

    def op3():
        for x in range(rangobucle):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op4():
        for x in range(rangobucle):
            resultado = 3.141592653589793 / (1 + x)

    def op5():
        for x in range(rangobucle):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op6():
        for x in range(rangobucle):
            resultado = 3.141592653589793 / (1 + x)

    def op7():
        for x in range(rangobucle):
            resultado = 10 / 0x5F3759DF * (1 + x)

    def op8():
        for x in range(rangobucle):
            resultado = 3.141592653589793 / (1 + x)

    # Ejecución operaciones---------------------------------------------------------------------------------------------
    if nucleos == "0":
        start_time = time.time()
        for x in range(rangobucle):  # Treinta millones
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
    #return(fp)

if __name__ == '__main__':
    if UI == 0:
        global modo_gui
        modo_gui = 0

        principal = 1
        while principal == 1:
            clear()
            print("Globalmark v" + version)
            print()

            if platform.machine() == "":
                arquitectura = "ARM"
                print("CPU:", arquitectura)
            else:
                arquitectura = platform.machine()
                print("CPU:", arquitectura)
            print("System:", platform.system(), platform.version())
            print("Python:", platform.python_version())
            print("Compiler:", platform.python_compiler())

            print()
            print("- Single-Core Benchmark  (0)")
            if platform.system() != "Windows":
                print("- Multi-Core Benchmark   (1)")
                print("- Stress test            (2)")
            print("- Scoreboard             (3)")
            print("- Exit                   (4)")
            print()
            if platform.system() == "Windows":
                respuesta = input("Choose Option: ")
            else:
                respuesta = input("Choose Option: ")
            if platform.system() == "Windows" and respuesta == "1" or platform.system() == "Windows" and respuesta == "2":
                respuesta = "0"
            print()

            if respuesta == "0": nucleos = "0"
            if respuesta == "1": nucleos = "1"
            if respuesta == "2":
                numeronucleos = input("Choose the amount of cores to test: ")
                print()
                numeronucleos = int(numeronucleos)
                stresstest = "1"
                test(stresstest, numeronucleos)
            if respuesta == "3":
                if legacy == 0:
                    mangodb(0, 0, 0, 0, 0, 0)
                    stresstest = "1"  # Para saltar el benchmark
                else:
                    input("No database connection, please install pymongo (Press any key): ")
                    stresstest = "1"  # Para saltar el benchmark
            if respuesta == "4": exit()
            if nucleos == "0":
                print("Single-Core benchmark:")
                modo = "Single-Core"
            if nucleos != "0":
                print("Multi-Core benchmark:")
                modo = "Multi-Core"

            while stresstest == "0":
                print()
                print("Integer Benchmark...")
                algoint(nucleos, rangobucle)
                print("FP Benchmark...")
                algoflp(nucleos, rangobucle)
                punt()
                print()
                respuesta = input("Do you want to submit your score? (Y/n): ")
                if respuesta == "y" or respuesta == "Y":
                    usuario = input("Introduce your username: ")
                    print()
                    mangodb(usuario, modo, puntint, puntfp, 1, arquitectura)

                clear()
                stresstest = "1"  # Salida del bucle

            stresstest = "0"  # Reinicio variable
    else:
        class Globalmark(App):
            def build(self):

                global superBox
                global cabecera
                global pie

                global modo_gui
                modo_gui = 1

                global resultadoAintroducir
                resultadoAintroducir = 0

                # Función que detecta el texto del botón seleccionado en pantalla---------------------------------------
                def callback(instance):

                    Seleccion = instance.text  # contiene el string del boton
                    print(instance.text)

                    global superBox

                    global cabecera
                    global pie

                    global cabecera_info
                    global pie_info

                    global cabecera_single
                    global pie_single

                    global cabecera_single2
                    global pie_single2

                    global cabecera_multi
                    global pie_multi

                    global cabecera_multi2
                    global pie_multi2

                    global cabecera_stress
                    global pie_stress

                    global cabecera_stress2
                    global pie_stress2

                    global control_back

                    global single_integer
                    global single_fp
                    global single_puntint
                    global single_puntfp

                    if Seleccion == "Single-Core Benchmark":
                        superBox.remove_widget(cabecera)
                        superBox.remove_widget(pie)

                        control_back = "single"

                        nucleos = "0"
                        rangobucle = 30900900

                        def ejecutar(instance):
                            global cabecera_single
                            global pie_single
                            global cabecera_single2
                            global pie_single2

                            superBox.remove_widget(cabecera_single)
                            superBox.remove_widget(pie_single)

                            global single_integer
                            global single_fp
                            global single_puntint
                            global single_puntfp

                            # Llamada funciones
                            algoint(nucleos, rangobucle)
                            algoflp(nucleos, rangobucle)
                            punt()

                            single_integer = integer
                            single_puntint = retornar_puntint

                            single_fp = fp
                            single_puntfp = retornar_puntfp

                            # Interfaz----------------------------------------------------------------------------------
                            # Widgets de cabecera añadidos en el plano horizontal
                            cabecera_single2 = BoxLayout(orientation='vertical')  # Primer div

                            # Crear elementos de cabecera
                            try:
                                consola1 = Label(text="Integer: " + single_integer + "s Score: " + single_puntint)
                                consola2 = Label(text="FP: " + single_fp + "s Score: " + single_puntfp)
                            except:
                                consola1 = Label(text="Integer: " + "" + "Score: " + "")
                                consola2 = Label(text="FP: " + "" + "Score: " + "")

                            consola3 = Label(text="Singlecore Benchmark")
                            null = Label()

                            # Añadir elementos a cabecera
                            cabecera_single2.add_widget(consola3)
                            cabecera_single2.add_widget(null)
                            cabecera_single2.add_widget(consola1)
                            cabecera_single2.add_widget(consola2)

                            # Widgets de pie de página añadidos en el plano vertical
                            pie_single2 = BoxLayout(orientation='vertical')

                            # Crear elementos del pie
                            correr = Button(text="Run test", background_color=(1, 0.2, 0.2, 0.7))
                            correr.bind(on_press=ejecutar)

                            volver = Button(text="Back", background_color=(1, 0.2, 0.2, 0.7))
                            volver.bind(on_press=callback)

                            null1 = Label()
                            null2 = Label()
                            null3 = Label()
                            null4 = Label()
                            null5 = Label()

                            # Añadir elementos al pie
                            pie_single2.add_widget(null1)
                            pie_single2.add_widget(null2)
                            pie_single2.add_widget(null3)
                            pie_single2.add_widget(null4)
                            pie_single2.add_widget(correr)
                            pie_single2.add_widget(volver)

                            # Añadir cada división al layout global
                            superBox.add_widget(cabecera_single2)
                            superBox.add_widget(pie_single2)

                            # Mostrar layout completo
                            # return superBox
                            # Fin Interfaz------------------------------------------------------------------------------

                        # Interfaz--------------------------------------------------------------------------------------
                        # Widgets de cabecera añadidos en el plano horizontal
                        cabecera_single = BoxLayout(orientation='vertical')  # Primer div

                        # Crear elementos de cabecera
                        try:
                            consola1 = Label(text="Integer: " + single_integer + "s Score: " + single_puntint)
                            consola2 = Label(text="FP: " + single_fp + "s Score: " + single_puntfp)
                        except:
                            consola1 = Label(text="Integer: " + "" + "Score: " + "")
                            consola2 = Label(text="FP: " + "" + "Score: " + "")

                        consola3 = Label(text="Singlecore Benchmark")
                        null = Label()

                        # Añadir elementos a cabecera
                        cabecera_single.add_widget(consola3)
                        cabecera_single.add_widget(null)
                        cabecera_single.add_widget(consola1)
                        cabecera_single.add_widget(consola2)

                        # Widgets de pie de página añadidos en el plano vertical
                        pie_single = BoxLayout(orientation='vertical')

                        # Crear elementos del pie
                        correr = Button(text="Run test", background_color=(1, 0.2, 0.2, 0.7))
                        correr.bind(on_press=ejecutar)

                        volver = Button(text="Back", background_color=(1, 0.2, 0.2, 0.7))
                        volver.bind(on_press=callback)

                        null1 = Label()
                        null2 = Label()
                        null3 = Label()
                        null4 = Label()
                        null5 = Label()

                        # Añadir elementos al pie
                        pie_single.add_widget(null1)
                        pie_single.add_widget(null2)
                        pie_single.add_widget(null3)
                        pie_single.add_widget(null4)
                        pie_single.add_widget(correr)
                        pie_single.add_widget(volver)

                        # Añadir cada división al layout global
                        superBox.add_widget(cabecera_single)
                        superBox.add_widget(pie_single)

                        # Mostrar layout completo
                        #return superBox
                        # Fin Interfaz----------------------------------------------------------------------------------

                    if Seleccion == "Multi-Core Benchmark":
                        superBox.remove_widget(cabecera)
                        superBox.remove_widget(pie)

                        control_back = "multi"

                        nucleos = "1"
                        rangobucle = 30900900

                        def ejecutar(instance):

                            global multi_integer
                            global multi_fp
                            global multi_puntint
                            global multi_puntfp
                            global cabecera_multi2
                            global pie_multi2

                            superBox.remove_widget(cabecera_multi)
                            superBox.remove_widget(pie_multi)

                            # Llamada funciones
                            algoint(nucleos, rangobucle)
                            algoflp(nucleos, rangobucle)
                            punt()

                            multi_integer = integer
                            multi_puntint = retornar_puntint

                            multi_fp = fp
                            multi_puntfp = retornar_puntfp

                            # Interfaz----------------------------------------------------------------------------------
                            # Widgets de cabecera añadidos en el plano horizontal
                            cabecera_multi2 = BoxLayout(orientation='vertical')  # Primer div

                            # Crear elementos de cabecera
                            try:
                                consola1 = Label(text="Integer: " + multi_integer + "s Score: " + multi_puntint)
                                consola2 = Label(text="FP: " + multi_fp + "s Score: " + multi_puntfp)
                            except:
                                consola1 = Label(text="Integer: " + "" + " Score: " + "")
                                consola2 = Label(text="FP: " + "" + " Score: " + "")

                            consola3 = Label(text="Multicore Benchmark")
                            null = Label()

                            # Añadir elementos a cabecera
                            cabecera_multi2.add_widget(consola3)
                            cabecera_multi2.add_widget(null)
                            cabecera_multi2.add_widget(consola1)
                            cabecera_multi2.add_widget(consola2)

                            # Widgets de pie de página añadidos en el plano vertical
                            pie_multi2 = BoxLayout(orientation='vertical')

                            # Crear elementos del pie
                            correr = Button(text="Run test", background_color=(1, 0.2, 0.2, 0.7))
                            correr.bind(on_press=ejecutar)

                            volver = Button(text="Back", background_color=(1, 0.2, 0.2, 0.7))
                            volver.bind(on_press=callback)

                            null1 = Label()
                            null2 = Label()
                            null3 = Label()
                            null4 = Label()
                            null5 = Label()

                            # Añadir elementos al pie
                            pie_multi2.add_widget(null1)
                            pie_multi2.add_widget(null2)
                            pie_multi2.add_widget(null3)
                            pie_multi2.add_widget(null4)
                            pie_multi2.add_widget(correr)
                            pie_multi2.add_widget(volver)

                            # Añadir cada división al layout global
                            superBox.add_widget(cabecera_multi2)
                            superBox.add_widget(pie_multi2)

                            # Mostrar layout completo
                            # return superBox
                            # Fin Interfaz------------------------------------------------------------------------------

                        # Interfaz--------------------------------------------------------------------------------------
                        # Widgets de cabecera añadidos en el plano horizontal
                        cabecera_multi = BoxLayout(orientation='vertical')  # Primer div

                        # Crear elementos de cabecera
                        try:
                            consola1 = Label(text="Integer: " + multi_integer + "s Score: " + multi_puntint)
                            consola2 = Label(text="FP: " + multi_fp + "s Score: " + multi_puntfp)
                        except:
                            consola1 = Label(text="Integer: " + "" + " Score: " + "")
                            consola2 = Label(text="FP: " + "" + " Score: " + "")

                        consola3 = Label(text="Multicore Benchmark")
                        null = Label()

                        # Añadir elementos a cabecera
                        cabecera_multi.add_widget(consola3)
                        cabecera_multi.add_widget(null)
                        cabecera_multi.add_widget(consola1)
                        cabecera_multi.add_widget(consola2)

                        # Widgets de pie de página añadidos en el plano vertical
                        pie_multi = BoxLayout(orientation='vertical')

                        # Crear elementos del pie
                        correr = Button(text="Run test", background_color=(1, 0.2, 0.2, 0.7))
                        correr.bind(on_press=ejecutar)

                        volver = Button(text="Back", background_color=(1, 0.2, 0.2, 0.7))
                        volver.bind(on_press=callback)

                        null1 = Label()
                        null2 = Label()
                        null3 = Label()
                        null4 = Label()
                        null5 = Label()

                        # Añadir elementos al pie
                        pie_multi.add_widget(null1)
                        pie_multi.add_widget(null2)
                        pie_multi.add_widget(null3)
                        pie_multi.add_widget(null4)
                        pie_multi.add_widget(correr)
                        pie_multi.add_widget(volver)

                        # Añadir cada división al layout global
                        superBox.add_widget(cabecera_multi)
                        superBox.add_widget(pie_multi)

                        # Mostrar layout completo
                        #return superBox
                        # Fin Interfaz----------------------------------------------------------------------------------

                    if Seleccion == "Stress test":
                        superBox.remove_widget(cabecera)
                        superBox.remove_widget(pie)

                        control_back = "stress"
                        stresstest = "1"

                        # Funcion que registra contenido del input------------------------------------------------------
                        def on_text(instance, value):

                            global resultadoAintroducir

                            print('The widget', instance, 'have:', value)

                            try:
                                resultadoAintroducir = value
                                resultadoAintroducir = int(resultadoAintroducir)
                            except:
                                resultadoAintroducir = 0

                        def callback_stress(instance):

                            global resultadoAintroducir
                            global cabecera_stress2
                            global pie_stress2

                            Seleccion = instance.text  # contiene el string del boton
                            print(instance.text)

                            superBox.remove_widget(cabecera_stress)
                            superBox.remove_widget(pie_stress)

                            test(stresstest,resultadoAintroducir)

                            # Interfaz----------------------------------------------------------------------------------
                            # Widgets de cabecera añadidos en el plano horizontal
                            cabecera_stress2 = BoxLayout(orientation='vertical')  # Primer div

                            # Crear elementos de cabecera
                            numero_nucleos = str(resultadoAintroducir)
                            textinput = Label(text="Running stresstest with " + numero_nucleos + " cores")

                            # Añadir elementos a cabecera
                            cabecera_stress2.add_widget(textinput)

                            # Widgets de pie de página añadidos en el plano vertical
                            pie_stress2 = BoxLayout(orientation='vertical')

                            # Crear elementos del pie
                            volver = Button(text="Back", background_color=(1, 0.2, 0.2, 0.7))
                            volver.bind(on_press=callback)

                            null1 = Label()
                            null2 = Label()
                            null3 = Label()
                            null4 = Label()
                            null5 = Label()

                            # Añadir elementos al pie
                            pie_stress2.add_widget(null1)
                            pie_stress2.add_widget(null2)
                            pie_stress2.add_widget(null3)
                            pie_stress2.add_widget(null4)
                            pie_stress2.add_widget(null5)
                            pie_stress2.add_widget(volver)

                            # Añadir cada división al layout global
                            superBox.add_widget(cabecera_stress2)
                            superBox.add_widget(pie_stress2)

                            # Mostrar layout completo
                            # return superBox
                            # Fin Interfaz------------------------------------------------------------------------------
                        # ----------------------------------------------------------------------------------------------

                        # Interfaz--------------------------------------------------------------------------------------
                        # Widgets de cabecera añadidos en el plano horizontal
                        cabecera_stress = BoxLayout(orientation='vertical')  # Primer div

                        # Crear elementos de cabecera
                        textinput = TextInput()
                        textinput.bind(text=on_text)

                        titulo = Label(text="Introduce number of cores/threads")
                        null2 = Label()

                        # Añadir elementos a cabecera
                        cabecera_stress.add_widget(titulo)
                        cabecera_stress.add_widget(textinput)
                        cabecera_stress.add_widget(null2)

                        # Widgets de pie de página añadidos en el plano vertical
                        pie_stress = BoxLayout(orientation='vertical')

                        # Crear elementos del pie
                        correr_stress = Button(text="Run test", background_color=(1, 0.2, 0.2, 0.7))
                        correr_stress.bind(on_press=callback_stress)

                        volver = Button(text="Back", background_color=(1, 0.2, 0.2, 0.7))
                        volver.bind(on_press=callback)

                        null1 = Label()
                        null2 = Label()
                        null3 = Label()
                        null4 = Label()
                        null5 = Label()

                        # Añadir elementos al pie
                        pie_stress.add_widget(null1)
                        pie_stress.add_widget(null2)
                        pie_stress.add_widget(null3)
                        pie_stress.add_widget(null4)
                        pie_stress.add_widget(correr_stress)
                        pie_stress.add_widget(volver)

                        # Añadir cada división al layout global
                        superBox.add_widget(cabecera_stress)
                        superBox.add_widget(pie_stress)

                        # Mostrar layout completo
                        # return superBox
                        # Fin Interfaz----------------------------------------------------------------------------------

                    if Seleccion == "Scoreboard":
                        #superBox.remove_widget(cabecera)
                        #superBox.remove_widget(pie)

                        #control_back = "score"
                        print()

                    if Seleccion == "Back":
                        if control_back == "info":
                            superBox.remove_widget(pie_info)
                            superBox.remove_widget(cabecera_info)

                            superBox.add_widget(cabecera)
                            superBox.add_widget(pie)

                        if control_back == "single":
                            try:
                                superBox.remove_widget(pie_single2)
                                superBox.remove_widget(cabecera_single2)
                            except:
                                superBox.remove_widget(pie_single)
                                superBox.remove_widget(cabecera_single)
                            else:
                                superBox.remove_widget(pie_single)
                                superBox.remove_widget(cabecera_single)

                            superBox.add_widget(cabecera)
                            superBox.add_widget(pie)

                        if control_back == "multi":
                            try:
                                superBox.remove_widget(pie_multi2)
                                superBox.remove_widget(cabecera_multi2)
                            except:
                                superBox.remove_widget(pie_multi)
                                superBox.remove_widget(cabecera_multi)
                            else:
                                superBox.remove_widget(pie_multi)
                                superBox.remove_widget(cabecera_multi)

                            superBox.add_widget(cabecera)
                            superBox.add_widget(pie)

                        if control_back == "stress":
                            try:
                                superBox.remove_widget(pie_stress2)
                                superBox.remove_widget(cabecera_stress2)
                                for i in range(resultadoAintroducir):
                                    os.kill(globals()[f'n{i}'], signal.SIGKILL)
                            except:
                                superBox.remove_widget(pie_stress)
                                superBox.remove_widget(cabecera_stress)
                            else:
                                superBox.remove_widget(pie_stress)
                                superBox.remove_widget(cabecera_stress)

                            superBox.add_widget(cabecera)
                            superBox.add_widget(pie)

                    if Seleccion == "Info":

                        superBox.remove_widget(cabecera)
                        superBox.remove_widget(pie)

                        control_back = "info"

                        # Interfaz--------------------------------------------------------------------------------------
                        # Widgets de cabecera añadidos en el plano horizontal
                        cabecera_info = BoxLayout(orientation='vertical') # Primer div

                        # Crear elementos de cabecera
                        consola1 = Label(text="Globalmark v" + version)

                        if platform.machine() == "":
                            arquitectura = "ARM"
                            consola2 = Label(text="CPU: " + arquitectura)
                        else:
                            arquitectura = platform.machine()
                            consola2 = Label(text="CPU: " + arquitectura)

                        consola3 = Label(text="System: " + platform.system() + platform.version())
                        consola4 = Label(text="Python: " + platform.python_version())
                        consola5 = Label(text="Compiler: " + platform.python_compiler())

                        null = Label()

                        # Añadir elementos a cabecera
                        cabecera_info.add_widget(consola1)
                        cabecera_info.add_widget(null)
                        cabecera_info.add_widget(consola2)
                        cabecera_info.add_widget(consola3)
                        cabecera_info.add_widget(consola4)
                        cabecera_info.add_widget(consola5)

                        # Widgets de pie de página añadidos en el plano vertical
                        pie_info = BoxLayout(orientation='vertical')

                        # Crear elementos del pie
                        volver = Button(text="Back", background_color=(1, 0.2, 0.2, 0.7))
                        volver.bind(on_press=callback)

                        null1 = Label()
                        null2 = Label()
                        null3 = Label()
                        null4 = Label()
                        null5 = Label()

                        # Añadir elementos al pie
                        pie_info.add_widget(null1)
                        pie_info.add_widget(null2)
                        pie_info.add_widget(null3)
                        pie_info.add_widget(null4)
                        pie_info.add_widget(null5)
                        pie_info.add_widget(volver)

                        # Añadir cada división al layout global
                        superBox.add_widget(cabecera_info)
                        superBox.add_widget(pie_info)

                        # Mostrar layout completo
                        #return superBox
                        # Fin Interfaz----------------------------------------------------------------------------------
                # ------------------------------------------------------------------------------------------------------

                # Interfaz principal------------------------------------------------------------------------------------
                # Layout global de superBox cada widget dispuestos uno encima de otro-----------------------------------
                superBox = BoxLayout(orientation='vertical')

                # Widgets de cabecera añadidos en el plano horizontal---------------------------------------------------
                cabecera = BoxLayout(orientation='horizontal')  # Primer div--------------------------------------------

                # Crear elementos de cabecera---------------------------------------------------------------------------
                consola = Image(source="./data/globalmark-logo.png")

                # Añadir elementos a cabecera---------------------------------------------------------------------------
                cabecera.add_widget(consola)

                # Widgets de pie de página añadidos en el plano vertical------------------------------------------------
                pie = BoxLayout(orientation='vertical')

                # Crear elementos del pie-------------------------------------------------------------------------------
                single = Button(text="Single-Core Benchmark", background_color=(1, 0.2, 0.2, 0.7))
                single.bind(on_press=callback)

                multi = Button(text="Multi-Core Benchmark", background_color=(1, 0.2, 0.2, 0.7))
                multi.bind(on_press=callback)

                stress = Button(text="Stress test", background_color=(1, 0.2, 0.2, 0.7))
                stress.bind(on_press=callback)

                score = Button(text="Scoreboard", background_color=(1, 0.2, 0.2, 0.3))
                score.bind(on_press=callback)

                info = Button(text="Info", background_color=(1, 0.2, 0.2, 0.7))
                info.bind(on_press=callback)

                null = Label()

                # Añadir elementos al pie-------------------------------------------------------------------------------
                pie.add_widget(single)
                pie.add_widget(multi)
                pie.add_widget(stress)
                pie.add_widget(null)
                pie.add_widget(score)
                pie.add_widget(info)

                # Añadir cada división al layout global-----------------------------------------------------------------
                superBox.add_widget(cabecera)
                superBox.add_widget(pie)

                # Mostrar layout completo-------------------------------------------------------------------------------
                return superBox
                # Fin Interfaz------------------------------------------------------------------------------------------

        Globalmark().run()
