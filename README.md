# ProjectEuler

## Notes

- Project setup originally with Python version 3.9.1
- "Py launcher" on windows (`py` instead of `python`) uses latest version

## Windows Setup

- File -> Settings -> Project -> Python Interpreter -> Gear icon -> Add new
- Exit terminal and start new to ensure venv is activated
- `python -m pip install -r requirements.txt`
- Create run configuration to run main.py (ensure it uses venv python)

## How to Create New Problem Solution

- Add new file to root of project in the form of problem_[problem #].py (ex: problem_23.py)
- In new problem file, define run method
- Update main.py import to the appropriate problem number
