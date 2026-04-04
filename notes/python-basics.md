# Python Basics
*GodTier Sprint — Week 1*

## Key Concepts

- `.py` = file extension for Python files
- `print()` = displays text on screen. Always uses parentheses, never curly braces
- Code executes top to bottom, line by line — like reading a book
- SyntaxError = grammar mistake Python cannot read

## Packages
- Packages = collections of code someone else wrote that you can use
- `pip install packagename` = how you install a package
- `anthropic` = Anthropic's package for Claude (our primary)
- `google-generativeai` = Google's package for Gemini (Week 2)
- `requests` = downloads data from the internet

## Virtual Environments
- venv (Virtual ENVironment) = a private isolated copy of Python for one project
- `python -m venv .venv` = CREATE the venv (once per project)
- `.venv\Scripts\Activate.ps1` = ACTIVATE the venv (every terminal session)
- `(.venv)` appearing in your prompt = confirmation it is active