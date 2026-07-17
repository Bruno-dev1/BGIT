# BGit

> A Git implementation written in Python for educational purposes.

BGit is a project created to study and understand how Git works internally by building a simplified version from scratch. Instead of only learning Git commands, the goal is to recreate its core features and understand the data structures, object model, and repository architecture that make Git so powerful.

This project is **not** intended to replace Git. It is an educational implementation focused on learning software architecture, file systems, hashing, and version control concepts.

---

## Goals

- Understand Git internals.
- Learn how version control systems work.
- Practice Python through a real-world project.
- Explore Git's object database.
- Recreate Git commands step by step.

---

## Planned Features

- [x] Repository initialization (`bgit init`)
- [ ] Repository configuration
- [ ] SHA-1 object hashing
- [ ] Blob objects
- [ ] Tree objects
- [ ] Commit objects
- [ ] Object storage
- [ ] References (`HEAD`, branches, tags)
- [ ] Staging Area (Index)
- [ ] `bgit add`
- [ ] `bgit commit`
- [ ] `bgit status`
- [ ] `bgit log`
- [ ] `bgit checkout`
- [ ] `bgit branch`

---

## Project Structure

```text
bgit/
│
├── bgit.py              # Entry point
├── repository.py        # Repository creation and discovery
├── objects.py           # Git objects (Blob, Tree, Commit)
├── refs.py              # References (HEAD, branches, tags)
├── index.py             # Staging Area
├── config.py            # Repository configuration
├── utils.py             # Helper functions
│
├── commands/
│   ├── init.py
│   ├── add.py
│   ├── commit.py
│   ├── status.py
│   ├── log.py
│   └── checkout.py
│
└── tests/
```

---

## Current Progress

Currently, BGit can:

- Initialize a repository
- Create the repository directory structure
- Create the initial `HEAD` file
- Create the initial configuration file

Repository layout:

```text
.bgit/
│
├── objects/
├── refs/
│   ├── heads/
│   └── tags/
├── HEAD
└── config
```

---

## Roadmap

### Phase 1 — Repository

- Repository initialization
- Configuration
- Repository discovery

### Phase 2 — Git Objects

- SHA-1 hashing
- Blob objects
- Object compression
- Object storage

### Phase 3 — Trees

- Tree parsing
- Directory snapshots

### Phase 4 — Commits

- Commit creation
- Commit history

### Phase 5 — References

- HEAD
- Branches
- Tags

### Phase 6 — Staging Area

- Index file
- File tracking
- Status detection

### Phase 7 — Advanced Commands

- Checkout
- Merge (optional)
- Diff (optional)

---

## Technologies

- Python 3.10+
- pathlib
- hashlib
- zlib

---

## Learning Objectives

During this project, I aim to deepen my understanding of:

- Version Control Systems (VCS)
- Git internals
- File system organization
- Data serialization
- SHA-1 hashing
- Object-oriented programming
- Software architecture
- Clean code practices

---

## Inspiration

This project is inspired by the excellent educational project **Write Yourself a Git (WYAG)**, but it is being developed independently as a personal learning exercise, with my own implementation and project structure.

---

## License

This project is licensed under the MIT License.