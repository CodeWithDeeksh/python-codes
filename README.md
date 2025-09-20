# 🐍 My Python Journey: A Portfolio of Practice Projects

This repository is a collection of Python scripts and applications I've developed while learning and practicing Python. It serves as a portfolio demonstrating my foundational skills and progress as a developer. Each project represents a key concept or problem I've worked through.

---

## 🎮 Tic-Tac-Toe Game

This is a console-based Tic-Tac-Toe game that pits a human player against an intelligent computer opponent. The game, initially a simple player-vs-random-computer version, has been enhanced to include an **unbeatable AI** using the **MiniMax algorithm**. This project demonstrates my understanding of game logic, input handling, and implementing advanced algorithms to solve a classic problem.

### ✨ Features
* **Player vs. Unbeatable AI:** The computer opponent uses the MiniMax algorithm to make optimal moves, making it impossible to defeat.
* **Dynamic Board Display:** The game board is visually updated in the console with clear spacing.
* **Win/Loss/Tie Detection:** The game accurately identifies and declares a winner or a tie.
* **Robust Input Handling:** The game handles invalid, out-of-bounds, and already-taken inputs gracefully.

### 🚀 How to Play
1. Ensure you have Python installed.
2. Run the game from your terminal:
    ```
    python tic_tac_toe.py
    ```
3. Follow the on-screen prompts to enter your moves.

---

## 🔒 Basic Keylogger

This is a simple proof-of-concept script that logs keyboard strokes. It's built using the `pynput` library and demonstrates my ability to work with external libraries and handle system events. The script captures both printable and special keys and saves them to a file. **Note:** This is a basic practice project created for learning purposes only. It should not be used for malicious activities.

### ✍️ How it Works
The script utilizes the `pynput.keyboard.Listener` to monitor keyboard events. When a key is pressed, the `keyPressed` function is triggered, which then writes the key's character or name to a file named `keyfile.txt`. The listener can be stopped by pressing the `Esc` key.

### ⚙️ Dependencies
* `pynput`
    ```
    pip install pynput
    ```
### ⚠️ Disclaimer
This code is for **educational purposes only**. Unauthorized use of such software is illegal and unethical.

---