# WordGuessor Game

![telegram-cloud-document-2-5404789087259333355](https://github.com/user-attachments/assets/479ae761-2503-480e-a46f-48a0b3f30c23)


This is a simple **Hangman-style** word-guessing game built using Python's **Tkinter** library. Players must guess the hidden word by entering letters. If the player guesses all the correct letters before exhausting their attempts, they win. Otherwise, they lose.

## Features
- Random word generation from a predefined list.
- Real-time updates to reveal correctly guessed letters.
- Visual feedback for winning and losing conditions.
- Intuitive graphical user interface (GUI).

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   Ensure that Python 3 is installed on your machine. This project also uses `tkinter` and `openpyxl`, which come pre-installed with Python in most cases.

3. **Run the application:**
   ```bash
   python main.py
   ```

## Directory Structure
```
project-directory
|-- main.py
|-- assets/
    |-- pic2.png
    |-- button_1.png
    |-- button_2.png
    |-- button_3.png
```
Ensure the **assets** directory contains the required image files.

## Gameplay Instructions
1. **Start a new game:**
   - Click the **Start** button to initialize a new round. The game will display a hidden word using `x` placeholders.

2. **Guess letters:**
   - Type a single letter into the input box and press **Submit**.
   - Correct guesses will reveal the corresponding letters.

3. **Win or Lose:**
   - You win by guessing the entire word correctly.
   - You lose if you exceed a specific number of incorrect attempts.

4. **Exit:**
   - Click the **Exit** button to close the game.

