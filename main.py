
#Definimos el diccionario principal que guardar todo lo relacionado con habitos

habitos = {}   # habitos { leer: {meta_semanal: 5, "registro": {"Lunes":True, "Martes": True...}}}




def plantilla_registro() -> dict:
    """
    Funcion que retorna el diccionario inicial para registrar los dias en los que se realizo el habito.
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
    """
    try:
        nombre_habito = input("\nIngresa el nombre del habito que quieres crear ⬇️\n").capitalize()
        meta_semanal = int(input(f"\nIngresa la meta semanal para {nombre_habito} ⬇️\n"))

        if nombre_habito != "" and not habitos.get(nombre_habito):
            registro = plantilla_registro()
            info_habito = {"meta_semanal": meta_semanal, "registro": registro }
            habitos[nombre_habito] = info_habito

        else:
            print(f"\n❌ Error: El habito ya existe o es vacio\n")

    except ValueError:
        print(f"❌Debes ingresar un numero como meta semanal")


    return habitos


def marcar_dia_completado(habitos):
    
    for i, habito in enumerate(habitos):
        print(f"{i}. {habito}")
        
print(marcar_dia_completado())




