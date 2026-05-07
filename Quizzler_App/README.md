# Quizzler App

A small True/False quiz GUI built with Python. The app fetches questions
from the Open Trivia Database (OpenTDB) and presents them in a simple
Tkinter interface with True/False image buttons and score tracking.

**Features**
- Fetches 10 boolean (True/False) questions from OpenTDB
- Simple GUI using `tkinter` with image buttons (`images/true.png`, `images/false.png`)
- Score tracking and immediate feedback (green/red) between questions

**Requirements**
- Python 3.7 or newer
- `requests` package (for fetching questions)
- Internet connection to fetch live questions from OpenTDB
- `tkinter` (normally included with standard Python installs)

**Install**
1. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install requests
```

**Run**
- Open a terminal in the project folder (Quizzler_App) and run:

```bash
python main.py
```

Note: Run from the `Quizzler_App` folder so the `images/` paths load correctly.

**Project files**
- `main.py` — Entry point. Builds question objects, starts the quiz UI.
- `ui.py` — Tkinter-based user interface and mainloop.
- `quiz_brain.py` — Quiz logic: question flow, scoring, and answer checking.
- `question_model.py` — Simple `Question` model (`text` and `answer`).
- `data.py` — Fetches question data from OpenTDB using `requests` (see note below).
- `images/` — Contains `true.png` and `false.png` used as button images.

**Notes & customization**
- `data.py` currently fetches questions from OpenTDB at runtime. If you
  want to run the app offline, replace the request block and use the
  static `question_data` list (there is an example commented out in `data.py`).
- If the image buttons do not display, ensure the `images` folder and
  files are present and that you run `python main.py` from the project folder.

**Contributing / Troubleshooting**
- If you see network errors, check your internet connection and API availability.
- Ensure `requests` is installed in the active Python environment.

Have fun quizzing! 🎉
