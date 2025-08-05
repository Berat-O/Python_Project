
# 🎱 Magic 8-Ball Game

## 📌 Description

This is a simple **Magic 8-Ball** game written in Python, designed as a practice exercise for using **functions** and **random number generation**.
The game mimics the classic toy by giving a random answer to a yes/no question.

## 🧠 How It Works

1. The user is prompted to ask a yes/no question.
2. The program randomly selects a number between 1 and 9.
3. Each number corresponds to a specific fortune response.
4. The selected answer is displayed as the "prediction."

## 🛠️ Technologies Used

* Python 3
* `random` module for RNG
* Functions for logic abstraction

## ▶️ Usage

Run the script using any Python interpreter:

```bash
python magic8ball.py
```

Then type a yes-or-no question and press `Enter`.
You’ll receive a randomized fortune as a response.

## 🔮 Sample Output

```
Ask a yes or no question:
> Will I ace my exams?
Outlook not so good
```

## 🧩 Function Breakdown

* `get_answer(answer_number)`: Returns a fortune based on a number (1 to 9).
