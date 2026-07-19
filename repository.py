from pathlib import Path
def creatDirectorys():
    print("starting repository")
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
        print(f"Creating {directory}...")
def createArchives():
    root=Path("bgit")
    archives = [
        root / "HEAD",
        root / "config",
    ]
    for archive in archives:
        archive.touch()
        print(f"Archive {archive} created...")
    (root / "HEAD").write_text("ref: refs/heads/main",encoding="utf-8")
def find_repository():
    path_atual = Path.cwd()
    while True:
        if (path_atual / "bgit").exists():
            print(f"repository finded! {path_atual / "bgit"}")
            break
        if path_atual != path_atual.parent :
            print("Repository not founded!")
            break
        path_atual = path_atual.parent

    