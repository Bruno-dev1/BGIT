import sys
from pathlib import Path
import repository


#criaçao  das funções
#.bgit/
def init():

    if Path("bgit/").is_dir():
        print("Repository exist!")
        sys.exit(1)
    repository.creatDirectorys()
    repository.createArchives()  
    print("repositório criado com sucesso!")         
def status():
    print("status...")
    repository.find_repository()
def commit():
    print("comitando")

#para comandos
if(len(sys.argv)> 1):
    command = sys.argv[1]
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