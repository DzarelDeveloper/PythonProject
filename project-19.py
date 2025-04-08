# Project-19 : TTC-VSAI
# Codesphered01010

import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.difficulty = "Easy"  

        self.header_label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        self.header_label.pack(pady=10)

        self.board_frame = tk.Frame(root, bg="#f0f0f0")
        self.board_frame.pack()
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.board_frame, text="", font=("Arial", 24), height=2, width=5, bg="#ffffff", fg="#333",
                               activebackground="#ddd", command=lambda idx=i: self.make_move(idx))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        self.reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), bg="#ff9999", fg="#fff",
                                       activebackground="#ff4d4d", command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.settings_frame = tk.Frame(root, bg="#f0f0f0")
        self.settings_frame.pack(pady=10)

        self.difficulty_label = tk.Label(self.settings_frame, text="Difficulty:", font=("Arial", 14), bg="#f0f0f0", fg="#333")
        self.difficulty_label.grid(row=0, column=0, padx=5)
        self.difficulty_var = tk.StringVar(value="Easy")
        self.difficulty_menu = tk.OptionMenu(self.settings_frame, self.difficulty_var, "Easy", "Medium", "Hard", command=self.update_difficulty)
        self.difficulty_menu.config(font=("Arial", 12), bg="#ffffff", fg="#333", activebackground="#ddd")
        self.difficulty_menu.grid(row=0, column=1, padx=5)

        self.score_frame = tk.Frame(root, bg="#f0f0f0")
        self.score_frame.pack(pady=10)

        self.x_score_label = tk.Label(self.score_frame, text="Player X: 0", font=("Arial", 14), bg="#f0f0f0", fg="#333")
        self.x_score_label.grid(row=0, column=0, padx=20)
        self.o_score_label = tk.Label(self.score_frame, text="Player O: 0", font=("Arial", 14), bg="#f0f0f0", fg="#333")
        self.o_score_label.grid(row=0, column=1, padx=20)

        self.x_score = 0
        self.o_score = 0

    def update_difficulty(self, level):
        self.difficulty = level
        messagebox.showinfo("Difficulty Selected", f"Difficulty level set to: {level}")

    def make_move(self, index):
        if self.board[index] == "" and self.current_player == "X":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg="#007bff" if self.current_player == "X" else "#ff3333")

            if self.check_winner():
                self.x_score += 1
                self.update_scoreboard()
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.disable_buttons()
                return

            if "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                return

            self.current_player = "O"
            self.computer_move()

    def computer_move(self):
        empty_indices = [i for i, value in enumerate(self.board) if value == ""]

        if self.difficulty == "Easy":
            move = random.choice(empty_indices) 
        elif self.difficulty == "Medium":
            move = self.medium_ai_move(empty_indices)
        else: 
            move = self.hard_ai_move()

        if empty_indices:
            self.board[move] = self.current_player
            self.buttons[move].config(text=self.current_player, fg="#007bff" if self.current_player == "X" else "#ff3333")

            if self.check_winner():
                self.o_score += 1
                self.update_scoreboard()
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.disable_buttons()
                return

            if "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                return

            self.current_player = "X"

    def medium_ai_move(self, empty_indices):
        for index in empty_indices:
            self.board[index] = "O"
            if self.check_winner():
                self.board[index] = ""
                return index
            self.board[index] = ""

        for index in empty_indices:
            self.board[index] = "X"
            if self.check_winner():
                self.board[index] = ""
                return index
            self.board[index] = ""

        return random.choice(empty_indices)

    def hard_ai_move(self):
        best_score = -float('inf')
        best_move = None

        for index in range(9):
            if self.board[index] == "":
                self.board[index] = "O"
                score = self.minimax(0, False)
                self.board[index] = ""
                if score > best_score:
                    best_score = score
                    best_move = index

        return best_move

    def minimax(self, depth, is_maximizing):
        if self.check_winner():
            return 1 if not is_maximizing else -1

        if "" not in self.board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "O"
                    score = self.minimax(depth + 1, False)
                    self.board[i] = ""
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "X"
                    score = self.minimax(depth + 1, True)
                    self.board[i] = ""
                    best_score = min(best_score, score)
            return best_score

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)              
        ]

        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                return True

        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def reset_game(self):
        self.board = ["" for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL, bg="#ffffff")

    def update_scoreboard(self):
        self.x_score_label.config(text=f"Player X: {self.x_score}")
        self.o_score_label.config(text=f"Player O: {self.o_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
