from os import system
from random import randint
import csv

clientes=[]
comunas=["Concepcion","Chiguayante","Talcahuano","Hualpen","San Pedro"]

def registrar_pedido():
    id=randint(10,1000)
    cilindro_6=0
    cilindro_10=0
    cilindro_20=0
    nombre=input("Ingrese su nombre: \n")
    apellido=input("Ingrese su apellido: \n")
    print(f"comunas disponible para hacer despacho {comunas}")
    sector=input("ingrese una comuna: \n")
    if sector not in comunas:
        print("comuna no disponible...intente otra vez")
        sector=input("ingrese una comuna: \n")
        if sector in comunas:
            print("comuna registrada ")
    direccion=input("Ingrese su direccion: \n")
    if direccion=="":
        print("tiene que escribrir su direccion, no puede estar vacio..")
        direccion=input("Ingrese su direccion: \n")

    try:
        while True:
            print("cual de las siguente opciones de cilindro desea comprar")
            cilindro=int(input(print("1.Dispensador de 6lts\n2.Dispensador de 10lts\n3.Dispensador de 20lts\n Ingrese su opcion: \n")))
            if cilindro ==1:
                cant_6=int(print("cuantos desa comprar"))
                cilindro_6+=cant_6
                print("cilindro 6lts")
            elif cilindro ==2:
                cant_10=int(print("cuantos desa comprar"))
                cilindro_10+=cant_10
                print("cilindro 10lts")
            elif cilindro==3:
                print("cilindro 20lts")
                cant_20=int(print("cuantos desa comprar"))
                cilindro_20+=cant_20
            else:
                print("opcion no disponible..")
            agregar=int(input(print("desea agregar mas cilindros (si/no)")))
            if agregar==1:
                print("volviendo al menu")
                return
            elif agregar==2:
                print("saliendo del menu")
                break
            else:
                print("respuesta invalidad..")
                return
    except ValueError:
        print("debe ingresar un numero.. intente otra vez..")
        return
    
    cliente={
        "ID":id,
        "nombre":nombre,
        "apellido":apellido,
        "direccion":direccion,
        "sector":sector,
        "cilindro":cilindro
    }
    clientes.append(cliente)
    print("cliente registrado.")


def listar_pedido():
    for cliente in clientes:
        print(f"ID{cliente['ID']}, Nombre{cliente['nombre','apellido']}, Direccion{cliente['direccion']}, Sector{cliente['sector']}, Cilindro{cliente['cilindro']}")
    print("pedidos encontrados")


def hoja_ruta():
    print(f"comunas disponibles {comunas}")
    sector=input("ingrese una comuna para imprimir: \n")
    if sector not in comunas:
        print("comuna no encontrada..")
    elif sector in comunas:
        with open(f"hoja_ruta{sector}.csv","w" , newline="") as archivo:
            lista=csv.writer(archivo)
            lista.writerow(f"ID{sector['ID']}, Nombre{sector['nombre','apellido']}, Direccion{sector['direccion']}, Sector{sector['sector']}, Cilindro{sector['cilindro']}")



            
def buscar_pedido():
    try:
        buscar=int(input((print("ingrese el id de su pedido:\n"))))
        for cliente in clientes:
            if cliente['ID']==buscar:
                print(f"ID{cliente['ID']}, Nombre{cliente['nombre','apellido']}, Direccion{cliente['direccion']}, Sector{cliente['sector']}, Cilindro{cliente['cilindro']}")
            else:
                print("cliente no encontrado")
    except ValueError:
        print("debe ingresar un numero")
        return



def menu():
    system("cls")
    while True:
        print("1.Registrar pedido\n2.2Listar pedido\n3.Imprimir hoja de ruta\n4.Buscar Pedido\n5.Salir de programa")
        opcion=input("ingrese su opcion ")
        
        if opcion=="1":
            registrar_pedido()
        elif opcion=="2":
            listar_pedido()
        elif opcion=="3":
            hoja_ruta()
        elif opcion=="4":
            buscar_pedido()
        elif opcion=="5":
            print("saliendo del programa....")
            break
        else:
            print("opcion invalida.. intente otra vez")
            return
        

if __name__=="__main__":
    menu()
