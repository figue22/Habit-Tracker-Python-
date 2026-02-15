
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

        if nombre_habito != "" and not habitos.get(nombre_habito):
            if meta_semanal <= 7:
                registro = plantilla_registro()
                info_habito = {"meta_semanal": meta_semanal, "registro": registro }
                habitos[nombre_habito] = info_habito
            else:
                print(f"\n❌ Error: La meta semanal no puede ser mayor a 7\n")

        else:
            print(f"\n❌ Error: El habito ya existe o es vacio\n")

    except ValueError:
        print(f"❌Debes ingresar un numero como meta semanal")


    return habitos

def listar_habitos(habitos):
     """
     Funcion que lista el diccionario de habitos con cada habito existente enmuerados del 1 a n
     
     :param habitos: Diccionario que guarda los habitos
     """
     for i, habito in enumerate(habitos, start= 1):
        print(f"{i}.{habito}")


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
        if valor == True:
            contador += 1

    dias_faltantes = meta_semanal - contador

    if dias_faltantes == 0:
        return f"\nPerfecto, has llegado a tu meta semanal, {meta_semanal}/{contador} dias 💪🎉\n"
    
    elif dias_faltantes < 0:
        return f"\nExcelente, has sobrepasado tu meta semanal, {meta_semanal}/{contador} dias 🔥🔥\n"
    
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

    if nombre_habito in habitos and nombre_habito != "":
        print("\n")
        registro = habitos[nombre_habito]["registro"]
        listar_habitos(registro)
        dia = input("\nIngresa el dia de la semana que quieres marcar (Como hecho o sin hacer) 🌞\n").capitalize()

        if dia in registro and dia != "":
            registro[dia] = not registro[dia]
            print(contar_dias_faltantes(habitos, nombre_habito))
            

        else:
            print("\n❌ Error: El dia es invalido o vacio\n")
    
    else:
        print("\n❌ Error: El habito no esta registrado o es vacio\n")


    return habitos


def mostrar_progreso(habitos):
    """
    Funcion que muestra el progreso en dias y porcentaje de cada habito
    
    :param habitos: Diccionario que contiene todos los habitos
    """
    
    for habito, valor in habitos.items():
        contador = 0
        for dia in valor['registro'].values():
            if dia == True:
                contador += 1

        procentaje = round((contador/valor['meta_semanal']) * 100)
        
        print(f"{habito}: {contador}/{valor['meta_semanal']} ({procentaje}%)")


def eliminar_habito(habitos) -> dict:
    """
    Funcion que permite elegir un habito y eliminarlo
    
    :param habitos: Diccionario que contiene los habitos
    :return: Diccionario de habitos con el habito eliminado
    :rtype: dict
    """
    listar_habitos(habitos)

    habito_eliminar = input("\nIngresea el habito que deseas eliminar🚮\n").capitalize()

    if habito_eliminar in habitos and habito_eliminar != "":
        habitos.pop(habito_eliminar)
        print(f"\nEl habito {habito_eliminar} ha sido eliminado con exito ✅\n")

    else:
        print("\n❌ Error: El habito no está registrado o es vacio\n")

    return habitos















