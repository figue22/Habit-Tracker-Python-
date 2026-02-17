
#Definimos el diccionario principal que guardar todo lo relacionado con habitos

habitos = {"Leer": 
                {"meta_semanal": 5, 
                 "registro": 
                            {"Lunes":True, 
                             "Martes": True, 
                             "Miercoles":True, 
                             "Jueves":True, 
                             "Viernes":True, 
                             "Sabado":False, 
                             "Domingo":False}                
                },

            "Comer": 
                {"meta_semanal": 7, 
                 "registro": 
                            {"Lunes":True, 
                             "Martes": True, 
                             "Miercoles":True, 
                             "Jueves":False, 
                             "Viernes":False, 
                             "Sabado":False, 
                             "Domingo":False}                
                }                  
            }   # habitos { leer: {meta_semanal: 5, "registro": {"Lunes":True, "Martes": True...}}}


def plantilla_registro() -> dict:
    """
    Funcion que retorna el diccionario inicial para registrar los dias en los que se realizo el habito.

    :return: retorna un diccionario con los dias de la semana como clave y el valor de todos es False
    :rtype: dict
    """
    registro = {"Lunes":False,
                "Martes":False,
                "Miercoles":False,
                "Jueves":False,
                "Viernes":False,
                "Sabado":False,
                "Domingo":False}
    
    return registro


def validar_campo(diccionario, campo, crear = True ) -> bool:
    """
    Funcion que valida que un campo no sea vacio y que no exista en caso de ser para crear un 
    habito o que exista en caso de no ser para crear
    
    :param habitos: Diccionario que guarda todos los habitos existentes
    :param campo: es el campo que se quiere validar
    :param crear: Indica si se va a verificar para creacion 
    :return: Retorna False e imprime el error con caso de que ocurra
    :rtype: bool
    """
   
    if not campo:
        print(f"\n❌ Error: Hay un campo vacio\n")
        return False
    
    if crear:
        if campo in diccionario:
                print(f"\n❌ Error:{campo} ya existe\n")
                return False
    else:
        if campo not in diccionario:
            print(f"\n❌ Error: {campo} no esta registrado\n")
            return False
        
    return True


def crear_habito(habitos) -> dict:
    """
    Función que pide los datos del habito y lo agrega al diccionario de habitos
    
    :param habitos: Diccionario que guarda los habitos 
    :return: devuelve el diccionario de habitos
    :rtype: dict
    """
    try:
        nombre_habito = input("\nIngresa el nombre del habito que quieres crear ⬇️\n").capitalize()
        meta_semanal = int(input(f"\nIngresa la meta semanal para {nombre_habito} ⬇️\n"))

        if not validar_campo(habitos, nombre_habito):
            return
            
        if meta_semanal <= 0 or meta_semanal > 7:
            print(f"\n❌ Error: La meta semanal debe ser un numero entre 1 y 7\n")
            return

        registro = plantilla_registro()
        info_habito = {"meta_semanal": meta_semanal, "registro": registro }
        habitos[nombre_habito] = info_habito
        print("Habito creado con exito, sigue avanzando 🔝🔥")

    except ValueError:
        print(f"❌Debes ingresar un numero como meta semanal")


    return habitos

def listar_habitos(habitos, es_registro = False):
     """
     Funcion que lista el diccionario de habitos o de registro de dias ralizados
     
     :param habitos: Diccionario que guarda los habitos
     :param es_registro: Verifica si es el diccionario de registro de dias para listarlos de forma diferente

     """
     for habito, valor in habitos.items():
        if es_registro:
            if valor:
                print(f"➡️ {habito}: ✅")
            else:
                print(f"➡️ {habito}: ❌")

        else:
            print(f"➡️ {habito}")



def contar_dias_faltantes(habitos, nombre_habito) -> str:
    """
    Funcion que toma el registro de dias de un habito y retorna cuantos dias le faltan al usuario para la meta
    
    :param habitos: Diccionario que guarda los habitos 
    :param nombre_habito: Nombre del habito que se desea contar
    :return: Mensaje indicando cuantos dias le faltan al usuario
    :rtype: str
    """
    registro = habitos[nombre_habito]["registro"]
    contador = 0
    meta_semanal = habitos[nombre_habito]["meta_semanal"]

    for valor in registro.values():
        if valor:
            contador += 1

    dias_faltantes = meta_semanal - contador

    if dias_faltantes == 0:
        return f"\nPerfecto, has llegado a tu meta semanal, {meta_semanal}/{contador} dias 💪🎉\n"
    
    elif dias_faltantes < 0:
        return f"\nExcelente, has sobrepasado tu meta semanal, {contador}/{meta_semanal} dias 🔥🔥\n"
    
    else:
        return f"\nVas muy bien, ya casi llegas a tu meta, {contador}/{meta_semanal} dias 💯🎯\n"


def marcar_dia(habitos) -> dict:
    """
    Funcion que marca un dia como completado o no hecho (True o False)
    
    :param habitos: Diccionario que guarda todos los habitos
    :return: Retorna el diccionario de habitos
    :rtype: dict
    """
    
    listar_habitos(habitos)

    nombre_habito = input("\nIngresa el nombre del habito 💯\n").capitalize()

    if not validar_campo(habitos, nombre_habito, False):
        return

    registro = habitos[nombre_habito]["registro"]
    listar_habitos(registro, True)
    dia = input("\nIngresa el dia de la semana que quieres marcar (Como hecho o sin hacer) 🌞\n").capitalize()
 
    if not dia:
        print(f"\n❌ Error: Dia vacio\n")
        return
    
    if dia not in registro:
        print(f"\n❌ Error: Dia invalido\n")
        return
    

    registro[dia] = not registro[dia]
    print(contar_dias_faltantes(habitos, nombre_habito))

    return habitos


def calcular_progreso(habitos) -> dict:
    """
    Funcion que calcula el progreso en dias y porcentaje de cada habito
    
    :param habitos: Diccionario que contiene todos los habitos
    :return: Retorna un diccionario con los dias expresados como fraccion y como porcentaje
    :rtype: dict
    """
    calculos = {}
    for habito, valor in habitos.items():
        contador = 0
        for dia in valor['registro'].values():
            if dia:
                contador += 1

        porcentaje = round((contador/valor['meta_semanal']) * 100)
        dias_fraccion = f"{contador}/{valor['meta_semanal']}"
        

        calculos[habito] = [dias_fraccion, porcentaje]

    return calculos


def ver_progreso(habitos):
    """
    Funcion que muestra el progreso de cada habito en dias y porcentaje
    
    :param habitos: Diccionario que contiene todos los habitos registrados
    """
    progreso_habitos = calcular_progreso(habitos)
    for habito, progreso in progreso_habitos.items():
        print (f"{habito}: {progreso[0]} dias ({progreso[1]}%)")
    

def eliminar_habito(habitos) -> dict:
    """
    Funcion que permite elegir un habito y eliminarlo
    
    :param habitos: Diccionario que contiene los habitos
    :return: Diccionario de habitos con el habito eliminado
    :rtype: dict
    """
    listar_habitos(habitos)

    habito_eliminar = input("\nIngresea el habito que deseas eliminar🚮\n").capitalize()

    if not validar_campo(habitos, habito_eliminar, False):
        return
    
    habitos.pop(habito_eliminar)
    print(f"\nEl habito {habito_eliminar} ha sido eliminado con exito ✅\n")

    return habitos


def estadisticas(habitos):
    """
    Funcion que calcula todas las estadisticas
    
    :param habitos: Diccionario que guarda todos los habitos existentes
    """

    if len(habitos) == 0:
        print("No tienes habitos registrados en este momento 😢")
    
    else:
        print("\n-----Estas son tus estadisticas generales de habitos 📊----\n")
        print(f"->El total de habitos que tienes registrados es de {total_habitos(habitos)} habitos")
        print(f"->{habito_mayor_cumplimiento(habitos)}")
        print(f"->{promedio_general_cumplimiento(habitos)}")



def total_habitos(habitos) -> int:
    """
    Funcion que calcula el total de habitos registrados
    
    :param habitos: Diccionario que contiene todos los habitos
    :return: Devuelve la longitud del diccionario de habitos, es decir, cuantos tiene
    :rtype: int
    """
    return len(habitos)


def obtener_porcentaje(item):
    """
    Funcion auxiliar para obtener el habito con mayor cumplimiento obteniendo el porcentaje (item[1][1] --> 100%)
    
    :param item: Es cada item del diccionaro
    """
    return item[1][1]

def habito_mayor_cumplimiento(habitos) -> str:
    """
    Funcion que calcula el habito con mayor porcentaje de cumplimiento
    
    :param habitos: Diccionario que guarda todos los habitos registrados
    :return: retorna un mensaje que indica el habito con mayor cumplimiento, los dias y el porcentaje
    :rtype: str
    """
    progreso_habitos = calcular_progreso(habitos)

    max_habitos = max(progreso_habitos.items(), key= obtener_porcentaje)

    return f"{max_habitos[0]} es el habito con mayor cumplimiento, con {max_habitos[1][0]} dias y un porcentaje de {max_habitos[1][1]}%✅🔥"


def promedio_general_cumplimiento(habitos) -> str:
    """"
    Funcion que calcula el promedio general de cumplimiento de todos los habitos y lo expresa en porcentaje

    :param habitos: Diccionario que contiene todos los habitos registrados
    :return: Retorna un mensaje al usuario con el promedio general
    :rtype: str
    """
    
    progreso_habitos = calcular_progreso(habitos)

    suma = 0

    for progreso in progreso_habitos.values():
        suma+= progreso[1]

    promedio = suma / len(habitos)

    return f"El promedio general de cumplimiento de los habitos es de {promedio}%, sigue avanzando💪💯"



def menu_principal(habitos):
    """
    Funcion que muestra el menu principal al usuario y le permite elegir una opcion para realizar una accion

    :param habitos: Diccionario que contiene todos los habitos registrados
    """
    while True:
        print("\nBienvenido a tu tracker de habitos, elige una opcion para comenzar ⬇️\n")
        print("1. Crear un nuevo habito 💪")
        print("2. Marcar un dia como hecho o sin hacer ❌✅")
        print("3. Ver progreso 💯🔝")
        print("4. Eliminar un habito ❌")
        print("5. Ver estadisticas 📶")
        print("6. Salir 👋")

        opcion = input("\nIngresa el numero de la opcion que deseas elegir 💯\n")

        if opcion == "1":
            crear_habito(habitos)

        elif opcion == "2":
            marcar_dia(habitos)

        elif opcion == "3":
            ver_progreso(habitos)

        elif opcion == "4":
            eliminar_habito(habitos)
        
        elif opcion == "5":
            estadisticas(habitos)

        elif opcion == "6":
            print("\nGracias por usar tu tracker de habitos, sigue avanzando💪💯\n")
            break

        else:
            print("\n❌ Error: Opcion invalida, ingresa un numero del 1 al 6\n")



            
if __name__ == "__main__":
    menu_principal(habitos)

        

        



