# CS Circle

Homework repo for teaching Devarshi and Priansh computer science.

## Layout

```
cs-circle/
├── devarshi/           # Devarshi's submissions
│   └── homework1.py
├── priansh/            # Priansh's submissions
│   └── homework1.py
├── tests/              # Shared test suite (teacher-authored)
│   ├── conftest.py
│   └── test_homework1.py
├── check.sh            # Test runner
└── README.md
```

## Branch workflow

- `main` — canonical copy of the lesson plan + framework.
- `devarshi` — Devarshi's working branch. He pushes his homework here.
- `priansh` — Priansh's working branch. He pushes his homework here.

Each cousin clones the repo, checks out their own branch, and only edits files
inside their own folder:

```bash
git clone <repo>
cd cs-circle
git checkout priansh     # or: git checkout devarshi
# edit priansh/homework1.py
git add priansh/homework1.py
git commit -m "homework 1 attempt"
git push origin priansh
```

## Testing a submission (teacher)

Quick check on the current branch:

```bash
./check.sh priansh
./check.sh devarshi
```

Pull their latest work first, then test:

```bash
./check.sh priansh --branch
./check.sh devarshi --branch
```

Under the hood the runner just sets a `STUDENT` env var and hands off to
pytest, so you can also run pytest directly:

```bash
STUDENT=priansh pytest tests/ -v
STUDENT=devarshi pytest tests/test_homework1.py::TestAddSecond -v
```

## Assignments

### Homework 1 — Linked lists

Implement `addSecond(data)` and `removeSecond()` on the `LinkedList` class in
your own `homework1.py`. See the docstrings in the starter file for the exact
contract. Run `./check.sh <you>` to see which tests pass.
