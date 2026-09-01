# Ejercicio 1 — “Caja del Kiosco” 

#Validacion del nombre
nombre_cliente = ""

while True:
    nombre_cliente = input("Ingrese su nombre: ")
    if nombre_cliente.isalpha():
        break
    else:
        print("ERROR: Ingrese un nombre valido")


#Validacion de productos 
cantidad_productos = 0

while True:
    productos_ingresados = input("Ingrese la cantidad de productos: ").strip()

    if productos_ingresados.isdigit():
        productos_ingresados = int(productos_ingresados)
        
        if productos_ingresados > 0:
            cantidad_productos = productos_ingresados
            break
        else:
            print("ERROR: Ingrese un numero mayor a 0")
    else:
        print("ERROR: Ingrese una cantidad valida")


#Declaro variables para guardar valores luego 
precio_total = 0
precio_total_descuentos = 0.0
descuento = ""

resumen_productos = ""

#Iteracion por producto, definicion de su precio y si tiene descuento
for i in range(cantidad_productos):

    #Validacion de precios correctos
    while True:
        precio_producto = input(f"Precio Producto {i + 1}: ").strip()

        if precio_producto.isdigit():
            precio_producto = int(precio_producto)
            precio_total += precio_producto
            break
        else:
            print("ERROR: Ingrese un precio entero valido")

    while True:
        descuento = input("¿El producto tiene descuento? (S/N): ").strip()

        if descuento != "" and descuento in "sS":
            precio_total_descuentos += precio_producto * 0.90
            break
        elif descuento != "" and descuento in "nN":
            precio_total_descuentos += precio_producto
            break
        else:
            print("ERROR: Ingrese uno de los caracteres validos (S/N)")

    #Guardo cada producto por iteracion para luego mostralo en el ticket final
    resumen_productos += f"Producto {i + 1} - Precio {precio_producto}   Descuento (S/N): {descuento} \n"

#Creo el promedio de los productos, luego de la ejecucion del bucle para que utilice los datos ya almacenados
promedio = precio_total_descuentos / cantidad_productos

print("/////////////////////////////////////////////////////////////////////")
print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")
print(resumen_productos)
print(f"Total sin descuentos: ${precio_total}")
print(f"Total con descuentos: ${precio_total_descuentos}")
print(f"Ahorro: ${precio_total - precio_total_descuentos:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("/////////////////////////////////////////////////////////////////////")


#////////////////////////////////////////////////////////////////////////////////////////////////////

#Ejercicio 2 — “Acceso al Campus y Menú Seguro” 

#Definicion de credenciales
usuario_correcto = "alumno"
clave_correcta = "python123"
#Definicion de una instancia para validar el acceso si ingresa correctamente las credenciales
cuenta_habilitada = False

#Primero valida el usuario que ingrese bien las credenciales
for i in range(3):

    print(f"Intento {i + 1}/3")
    usuario = input("Usuario: ")
    contraseña = input("Clave: ")

    if usuario[:] == usuario_correcto[:] and contraseña[:] == clave_correcta[:]:
        cuenta_habilitada = True
        break
    else:
        print("ERROR: Credenciales inválidas. \n")

    if i == 2:
        print("CUENTA BLOQUEADA")

#Una vez habilitada la cuenta interactua con el menu
while cuenta_habilitada:
    print("1) Estado   2) Cambiar clave   3) Mensaje   4) Salir")

    opcion = input("Opción: ").strip()

    if opcion.isdigit():
        opcion = int(opcion)
#Navegacion por el menu y validacion de ingresar correctamente la opcion
        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            while True:
                nueva_clave = input("Ingresa una nueva clave: ")
                if len(nueva_clave) < 6:
                    print("ERROR: Minimo 6 caracteres")
                else:
                    while True:
                        confirmar_clave = input("Confirme su nueva clave: ")
                        if nueva_clave[:] == confirmar_clave[:]:
                            clave_correcta = nueva_clave
                            print("¡Clave modificada!")
                            break
                        else:
                            print("La clave no coincide")
                    break
        elif opcion == 3:
            print("No necesitás más motivación. Necesitás empezar.")
        elif opcion == 4:
            print("¡Hasta la próxima!")
            break        
        else:
            print("ERROR: Opción fuera de rango")
    else:
        print("ERROR: Ingrese un numero valido")
        

#////////////////////////////////////////////////////////////////////////////////////////////////////

#  Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)” 

#Acceso de operador para entrar al sistema
while True:
    nombre_operador = input("Ingrese el nombre de operador: ")

    if nombre_operador.isalpha():
        print(f"Hola {nombre_operador}!")
        break
    else:
        print("Error: Ingrese un nombre valido solo con letras")

#Declaracion de variables para utilizar durante la logica del programa
salir = True

lunesT1 = "Libre"
lunesT2 = "Libre"
lunesT3 = "Libre"
lunesT4 = "Libre"
turnos_lunes = 0

martesT1 = "Libre"
martesT2 = "Libre"
martesT3 = "Libre"
turnos_martes = 0

#Creacion del menu repetitivo hasta que el usuario decida salir
while salir:
    print("1) Reservar turno   2) Cancelar turno   3) Agenda del dia   4) Resumen general   5) Cerrar sistema")

    opcion = input("Opción: ").strip()
    
    if opcion.isdigit():
        opcion = int(opcion)

        #Reserva de turno: Iteraccion de dia para reserva, evaluacion de que el paciente no tenga turno ese dia y luego que si no tiene turno le asigne el primer turno libre disponible
        if opcion == 1:
            print("\n///////////////////////////////////////////")
            print("Elegir dia:\n   1)Lunes   2)Martes   3)Salir")

            while True:
                confirmacion = True
                dia = input("Seleccione una opcion: ").strip()
                if dia.isdigit():

                    if dia == "1":
                        while confirmacion:
                            nombre_paciente = input("Ingrese el nombre del paciente: ").lower()
                            if nombre_paciente.isalpha():

                                if nombre_paciente == lunesT1 or nombre_paciente == lunesT2 or nombre_paciente == lunesT3 or nombre_paciente == lunesT4:
                                    print("El paciente ya tiene cita este dia") 
                                    break
                                elif lunesT1 == "Libre":
                                    lunesT1 = nombre_paciente
                                    turnos_lunes += 1
                                    print("Se guardo el turno Lunes 1")
                                    confirmacion = False
                                elif lunesT2 == "Libre":
                                    lunesT2 = nombre_paciente 
                                    turnos_lunes += 1
                                    print("Se guardo el turno Lunes 2")
                                    confirmacion = False
                                elif lunesT3 == "Libre":
                                    lunesT3 = nombre_paciente
                                    turnos_lunes += 1
                                    print("Se guardo el turno Lunes 3")
                                    confirmacion = False
                                elif lunesT4 == "Libre":
                                    lunesT4 = nombre_paciente
                                    turnos_lunes += 1
                                    print("Se guardo el turno Lunes 4")
                                    confirmacion = False
                                else:
                                    print("¡Los turnos del dia estan completos!")
                                    confirmacion = False

                            else:
                                print("Error: El nombre del paciente debe ser solo letras")
                                
                    elif dia == "2":
                        while confirmacion:
                            nombre_paciente = input("Ingrese el nombre del paciente: ").lower()
                            if nombre_paciente.isalpha():

                                if nombre_paciente == martesT1 or nombre_paciente == martesT2 or nombre_paciente == martesT3:
                                    print("El paciente ya tiene cita este dia") 
                                    break
                                elif martesT1 == "Libre":
                                    martesT1 = nombre_paciente
                                    turnos_martes += 1
                                    print("Se guardo el turno Martes 1")
                                    confirmacion = False
                                elif martesT2 == "Libre":
                                    martesT2 = nombre_paciente 
                                    turnos_martes += 1
                                    print("Se guardo el turno Martes 2")
                                    confirmacion = False
                                elif martesT3 == "Libre":
                                    martesT3 = nombre_paciente
                                    turnos_martes += 1
                                    print("Se guardo el turno Martes 3")
                                    confirmacion = False
                                else:
                                    print("¡Los turnos del dia estan completos!")
                                    confirmacion = False

                            else:
                                print("Error: El nombre del paciente debe ser solo letras")

                    elif dia == "3":
                        break

                    else:
                        print("Error: Seleccione un numero dentro del rango")

                else:
                    print("Error: Ingrese un numero valido") 
                break       

        #Cancelacion de turno: Interaccion para seleccionar dia y nombre del paciente para eliminar todos los datos y liberar el dia
        elif opcion == 2:
            print("\n///////////////////////////////////////////")
            print("Elegir dia:\n   1)Lunes   2)Martes   3)Salir")

            while True:
                confirmacion = True
                dia = input("Seleccione una opcion: ").strip()
                if dia.isdigit():

                    if dia == "1":
                        while confirmacion:
                            nombre_paciente = input("Ingrese el nombre del paciente: ").lower()
                            if nombre_paciente.isalpha():
                                if nombre_paciente[:] in lunesT1:
                                    lunesT1 = "Libre"
                                    turnos_lunes -= 1
                                    print("Se cancelo la cita Lunes 1")
                                    confirmacion = False
                                elif nombre_paciente[:] in lunesT2:
                                    lunesT2 = "Libre"
                                    turnos_lunes -= 1
                                    print("Se cancelo la cita Lunes 2")
                                    confirmacion = False
                                elif nombre_paciente[:] in lunesT3:
                                    lunesT3 = "Libre"
                                    turnos_lunes -= 1
                                    print("Se cancelo la cita Lunes 3")
                                    confirmacion = False
                                elif nombre_paciente[:] in lunesT4:
                                    lunesT4 = "Libre"
                                    turnos_lunes -= 1
                                    print("Se cancelo la cita Lunes 4")
                                    confirmacion = False
                                else:
                                    print("Error: El nombre ingresado no esta en sistema")
                                    confirmacion = False
                            else:
                                print("Error: El nombre del paciente debe ser solo letras")

                    elif dia == "2":
                        while confirmacion:
                            nombre_paciente = input("Ingrese el nombre del paciente: ").lower()
                            if nombre_paciente.isalpha():
                                if nombre_paciente[:] in martesT1:
                                    martesT1 = "Libre"
                                    turnos_martes -= 1
                                    print("Se cancelo la cita Martes 1")
                                    confirmacion = False
                                elif nombre_paciente[:] in martesT2:
                                    martesT2 = "Libre"
                                    turnos_martes -= 1
                                    print("Se cancelo la cita Martes 2")
                                    confirmacion = False
                                elif nombre_paciente[:] in martesT3:
                                    martesT3 = "Libre"
                                    turnos_martes -= 1
                                    print("Se cancelo la cita Martes 3")
                                    confirmacion = False
                                else:
                                    print("Error: El nombre ingresado no esta en sistema")
                                    confirmacion = False        
                            else:
                                print("Error: El nombre del paciente debe ser solo letras")

                    elif dia == "3":
                        break

                    else:
                        print("Error: Seleccione un numero dentro del rango")

                else:
                    print("Error: Ingrese un numero valido") 
                break  

        #Agenda del dia: Interaccion para elegir que dia visualizar los turnos
        elif opcion == 3:
            print("\n///////////////////////////////////////////")
            print("Elegir dia:\n   1)Lunes   2)Martes   3)Salir")
            
            while True:
                dia = input("Seleccione una opcion: ").strip()
                if dia.isdigit():

                    if dia == "1":
                        print("//////////////////")
                        print("LUNES")
                        print(f"Turno 1 - {lunesT1}")
                        print(f"Turno 2 - {lunesT2}")
                        print(f"Turno 3 - {lunesT3}")
                        print(f"Turno 4 - {lunesT4}")
                        break
                    elif dia == "2":
                        print("//////////////////")
                        print("MARTES")
                        print(f"Turno 1 - {martesT1}")
                        print(f"Turno 2 - {martesT2}")
                        print(f"Turno 3 - {martesT3}")
                        break
                    elif dia == "3":
                        break

                else:
                    print("Error: Seleccione un numero dentro del rango")

        #Agenda completa: Todos los dias con todos los turnos y el calculo general de que dia tiene mas turnos o dias libres
        elif opcion == 4:
            print("/////////////////////")
            print("LUNES")
            print(f"Turno 1 - {lunesT1}")
            print(f"Turno 2 - {lunesT2}")
            print(f"Turno 3 - {lunesT3}")
            print(f"Turno 4 - {lunesT4}")            
            print("/////////////////////")
            print("MARTES")
            print(f"Turno 1 - {martesT1}")
            print(f"Turno 2 - {martesT2}")
            print(f"Turno 3 - {martesT3}")

            if turnos_lunes > turnos_martes:
                print(f"Hay mas turnos el lunes ({turnos_lunes})")
            elif turnos_martes > turnos_lunes:
                print(f"Hay mas turnos el martes ({turnos_martes})")
            else:
                print("Hay la misma cantidad de turnos para lunes y martes")
                            
        elif opcion == 5:
            print("Sistema cerrado")  
            salir = False

        else:
            print("ERROR: Opción fuera de rango")
    else:
        print("ERROR: Ingrese un numero valido")


#////////////////////////////////////////////////////////////////////////////////////////////////////

# Ejercicio 4  — “Escape Room: La Bóveda” 

#Declaracion de variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

termina_juego = True
contador_antispam = 0

#Importacion de modulos para generar lestras aleatorias en la opcion de hackear panel
import string
import random

#Creacion de agente
while True:
    nombre_agente = input("Ingrese el nombre de su agente: ").strip()

    if nombre_agente.isalpha():
        print(f"¡Que gusto que seas tu {nombre_agente}!\nEres la persona indicada para esta mision de alto riesgo...")
        break
    else:
        print("Error: Ingrese un nombre valido de solo letras")


print("\n////////////////////")
print("ESCAPA DE LA BOVEDA")
print("////////////////////")

while termina_juego:
#Primero evalua que el usuario no gano el juego, si no se cumple, continua evaluando las condiciones de derrota. Mientras ninguna condicion de derrota se cumpla, continua con la interaccion del juego
    if cerraduras_abiertas < 3:
        
        if energia <= 0:
            print("PERDISTE ¡Te quedaste sin energia!")
            termina_juego = False

        elif tiempo <= 0:
            print("PERDISTE ¡Se acabo el tiempo!")
            termina_juego = False

        elif alarma and tiempo <= 3:
            print("PERDISTE ¡Se bloqueo el sistema!")
            termina_juego = False

        else:
            print(f"\nEnergia: {energia}\nTiempo: {tiempo}\nCerraduras abiertas: {cerraduras_abiertas}")

            if alarma == False:
                print("Alarma: Desactivada")
            else:
                print("Alarma: Activada")

            print("\n///// ELIGE UNA ACCION /////")
            print("1) Forzar cerradura (-20 Energia, -2 Tiempo)\n2) Hackear panel (-10 Energia, -3 Tiempo)\n3) Descansar (+15 Energia, -1 Tiempo)")

            accion = input("Accion: ")

            if accion.isdigit():
                accion = int(accion)

                #Forzar cerradura: Con contador de spam, y condicion de cuanta energia tiene para saber si abre la cerradura o tiene posibilidades de activar la alarma
                if accion == 1:

                    if alarma == False:
                        energia -= 20
                        tiempo -= 2

                        #Contador de cuantas veces fuerza cerradura de forma seguida, si elige otra opcion, el contador de spam vuelve a 0
                        contador_antispam += 1
                        if contador_antispam == 3:
                            print("¡La cerradura se trabó, acaba de activarse la ALARMA!")
                            cerraduras_abiertas -=1
                            alarma = True 

                        if energia < 40:
                            print("CUIDADO, tienes la energia baja. ¡Un paso en falso y activaras la alarma! Confia en tu instinto para no activarla...")
                            while True:
                                numero_activacion = input("1)   2)   3): ")
                                if numero_activacion.isdigit():
                                    if numero_activacion == "1" or numero_activacion == "2":
                                        print("Eso estuvo cerca, prioriza descansar antes de forzar nuevamente la cerradura")
                                        break
                                    elif numero_activacion == "3":
                                        print("¡Activaste la alarma!")
                                        alarma = True
                                        break
                                    else:
                                        print("Error: Ingresa un numero dentro del rango de opciones")
                                else:
                                    print("Error: Ingresa un numero valido")
                        else:
                            cerraduras_abiertas += 1
                            print("¡Muy bien! Lograste abrir una cerradura")
                    else:
                        print("¡La alarma esta encendida, no puedes forzar la cerradura!")

                #Hackear panel: Crea 4 letras y las agrega a codigo parcial, cuando el codigo parcial tenga 8 letras, se abre una cerradura           
                elif accion == 2:
                    contador_antispam = 0
                    energia -= 10
                    tiempo -= 3

                    print("Obteniendo informacion del panel...")
                    for i in range(4):
                        #Uso de los modulos para generar letras aleatorias en mayusculas
                        letra = random.choice(string.ascii_uppercase)
                        print(letra)
                        codigo_parcial += letra

                    if len(codigo_parcial) >= 8:
                        cerraduras_abiertas += 1
                        codigo_parcial = ""
                        print("¡Hackeo exitoso! Abriste una cerradura")

                #Descanso: Evalua si esta la alarma activada para definir cuanta energia recupera
                elif accion == 3:
                    contador_antispam = 0
                    if alarma == False:
                        if (energia + 15) <= 100:
                            energia += 15
                            tiempo -= 1
                            print("Ese descanso vino bastante bien, recuperaste 15 de energia.")
                        else:
                            print("¡No puedes tener más de 100 de energia!")
                    else:
                        if (energia + 5) <= 100:
                            energia += 5
                            tiempo -= 1
                            print("Recuperaste poca energia (5) porque la alarma esta activada.")
                        else:
                            print("¡No puedes tener más de 100 de energia!")
                                
                else:
                    print("=========================================\nError: Ingrese un numero dentro del rango\n=========================================")    

            else:
                print("================================\nError: Ingrese un numero valido\n================================")

    else:
        print("¡Lograste escapar de la bóveda!")
        termina_juego = False


#////////////////////////////////////////////////////////////////////////////////////////////////////

# Ejercicio 5  — “Escape Room:"La Arena del Gladiador"

#Declaracion de variables iniciales
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
bd_gladiador = 15
bd_enemigo = 12
turno_gladiador = True

termina_juego = True
nombre_gladiador = ""

#Creacion de personaje
while True:
    nombre_gladiador = input("Ingrese el nombre de su gladiador: ").strip()

    if nombre_gladiador.isalpha():
        print(f"¡Bienvenido/a {nombre_gladiador} a la arena de batalla!")
        break
    else:
        print("Error: Ingrese un nombre valido de solo letras")

print("\n======================")
print("LA ARENA DEL GLADIADOR")
print("======================")

while termina_juego:

    #Primero evalua que ambos personajes tengan vida, caso contrario, evalua cual de los dos tiene 0 o menos para determinar el fin de la partida
    if vida_enemigo > 0 and vida_gladiador > 0:

        #Cada accion finaliza el turno del gladiador
        while turno_gladiador:
            print(f"{nombre_gladiador}: {vida_gladiador}HP | Enemigo: {vida_enemigo}HP\nPociones: {pociones_vida}")
            print("\n///// ELIGE UNA ACCION /////")
            print("1) Ataque pesado\n2) Ráfaga veloz\n3) Curar")
            accion = input("Accion: ")

            if accion.isdigit():
                accion = int(accion)

                #Ataque pesado: Evalua la vida del enemigo para saber si el golpe es critico o con el daño base
                if accion == 1:

                    if vida_enemigo < 20:
                        critico = bd_gladiador * 1.5
                        vida_enemigo -= critico
                        print(f"GOLPE CRITICO ¡Atacaste al enemigo por {critico} puntos de daño!")
                    else:
                        vida_enemigo -= bd_gladiador
                        print(f"¡Atacaste al enemigo por {bd_gladiador} puntos de daño!")
                    turno_gladiador = False

                #Ataque rafaga: Por cada iteracion, genera daño al enemigo
                elif accion == 2:

                    cont_daño = 0
                    for i in range(3):
                        cont_daño += 5
                        print("Golpe conectado por 5 de daño")
                    vida_enemigo -= cont_daño
                    print(f"¡Atacaste al enemigo por {cont_daño} puntos de daño!")
                    turno_gladiador = False

                #Curar: Evalua las pociones disponibles para poder curarse o no
                elif accion == 3:

                    if pociones_vida > 0:
                        vida_gladiador += 30
                        pociones_vida -= 1
                        print("Recuperaste 30 puntos de vida")
                    else:
                        print("¡No quedan pociones!")
                        turno_gladiador = False

                else:
                    print("=========================================\nError: Ingrese un numero dentro del rango\n=========================================")
            else:
                print("================================\nError: Ingrese un numero valido\n================================")

        #Ataque del enemigo, una vez terminado activa nuevamente el turno del gladiador
        print("¡El enemigo ataco por 12 puntos de daño!")
        vida_gladiador -= bd_enemigo
        print("\n===========\nNUEVO TURNO\n===========")
        turno_gladiador = True
        
    elif vida_enemigo <= 0:
        print(f"VICTORIA {nombre_gladiador} ha ganado la batalla.")
        termina_juego = False

    else:
        print("DERROTA. Has caído en combate.")
        termina_juego = False