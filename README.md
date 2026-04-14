# Python Training — TRAINEE_TASKS_-CCAC-

A structured Python training programme covering core language fundamentals and object-oriented programming. Each task is completed on its own branch and reviewed via Pull Request.

---

## Repository structure

```
TRAINEE_TASKS_-CCAC-/
├── 01_Basics/
│   ├── 01_calculator_task.py
│   ├── 02_word_counter.py
│   └── 03_fizzbuzz.py
├── 02_OOP/
│   ├── 01_OOP_bank_account.py
│   └── 02_OOP_Animal_shelter.py
└── README.md
```

---

## Tasks

| # | File | Topic | Status |
|---|------|-------|--------|
| 1 | `01_Basics/01_calculator_task.py` | Functions, error handling | ⬜ Not started |
| 2 | `01_Basics/02_word_counter.py` | Loops, strings, dictionaries | ⬜ Not started |
| 3 | `01_Basics/03_fizzbuzz.py` | Conditionals, loops | ⬜ Not started |
| 4 | `02_OOP/01_OOP_bank_account.py` | Classes, `__init__`, methods | ⬜ Not started |
| 5 | `02_OOP/02_OOP_Animal_shelter.py` | Inheritance, polymorphism | ⬜ Not started |

> Update status to 🔄 In progress, 👀 In review, or ✅ Done as you work through each task.

---

## Workflow

Each task follows the same Git workflow:

```bash
# 1. Create a branch for the task
git checkout -b task-1-calculator

# 2. Write your code, then stage and commit
git add .
git commit -m "Add calculator with division guard"

# 3. Push the branch
git push origin task-1-calculator

# 4. Open a Pull Request to main on GitHub
```

### Pull Request checklist

Before opening a PR, make sure:

- [ ] The script runs without errors
- [ ] Edge cases are handled (e.g. division by zero, empty input)
- [ ] Variable and function names are clear and readable
- [ ] No unused code or `print` statements left over from debugging
- [ ] PR description explains what the code does and how to run it

---

## How to run

Each task is a standalone Python script. Run from the project root:

```bash
python 01_Basics/01_calculator_task.py
python 02_OOP/01_OOP_bank_account.py
```

**Requirements:** Python 3.8 or higher. No external packages needed.

---

## Code review

Pull Requests are reviewed by the team lead before merging. Address all comments before requesting a re-review. Approval is required to merge into `main`.

---

## Author
**Overseer:** vee.dev_