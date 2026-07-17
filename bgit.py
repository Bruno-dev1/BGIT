import sys
from pathlib import Path


#criaçao  das funções
#.bgit/
def init():

    print("iniciando repositório")
    paths = [".bgit","objects","refs","heads","tags"]
def status():
    print("status...")
def commit():
    print("comitando")

#para comandos
if(len(sys.argv)> 1):
    command = sys.argv[1]
    print("Comando recebido: "+command)
    match command:
        case "init":
            init()
            
        case "status":
            status()
        case "commit":
            commit()
        case _:
            print(f"o comando {command} não foi reconhecido")

else:
    print("Lista de comandos")