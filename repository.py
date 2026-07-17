from pathlib import Path
def creatDirectorys():
    print("iniciando repositório")
    root=Path("bgit")
    directories = [
        root,
        root / "objects",
        root / "refs",
        root / "refs" / "heads",
        root / "refs" / "tags",
       
    ]
    for directory in directories:
        directory.mkdir(parents=True,exist_ok= True)
        print(f"Criando {directory}...")

def createArchives():
    root=Path("bgit")
    archives = [
        root / "HEAD",
        root / "config",
    ]
    for archive in archives:
        archive.touch()
        print(f"Criando arquivo {archive}")
    (root / "HEAD").write_text("ref: refs/heads/main",encoding="utf-8")