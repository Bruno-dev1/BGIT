import sys
from pathlib import Path

import repository
import objects


# criação das funções
#.bgit/
def init():

    if Path(".bgit").is_dir():
        print("Repository exist!")
        sys.exit(1)

    repository.creatDirectorys()
    repository.createArchives()

    print("Repositório criado com sucesso!")


def status():
    print("status...")
    repository.find_repository()


def commit():
    print("comitando")


def hash_object(filename):

    with open(filename, "rb") as file:
        data = file.read()

    blob = objects.create_blob(data)

    object_hash = objects.write_object(blob)

    print(object_hash)


# para comandos
if len(sys.argv) > 1:

    command = sys.argv[1]

    match command:

        case "init":
            init()

        case "status":
            status()

        case "commit":
            commit()

        case "hash-object":
            hash_object(sys.argv[2])

        case _:
            print(f"O comando {command} não foi reconhecido")

else:
    print("Lista de comandos")