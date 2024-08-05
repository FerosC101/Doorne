import tkinter as tk
from tkinter import messagebox
import json
import time
import os

class MainMenu:
    def __init__(self, root, user_manager):
        self.root = root
        self.user_manager = user_manager
        self.current_user = None
        self.initialize_frame()
        self.create_widgets()

    def initialize_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

    def create_widgets(self):
        self.clear_frame()  # Ensure the frame is cleared
        self.root.title("MyDormie")

        self.label = tk.Label(self.frame, text="Welcome to MyDormie", font=("Arial", 16))
        self.label.pack(pady=10)

        self.register_button = tk.Button(self.frame, text="Register", command=self.register)
        self.register_button.pack(fill='x')

        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.pack(fill='x')

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(fill='x')

    def register(self):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="Register", font=("Arial", 16))
        self.label.pack(pady=10)

        tk.Label(self.frame, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.frame, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.frame, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(self.frame, text="Register", command=self.perform_registration).pack(pady=5)
        tk.Button(self.frame, text="Back", command=self.create_widgets).pack(pady=5)

    def perform_registration(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_manager.acc_register(username, password):
            messagebox.showinfo("Success", "Registration Successful!")
            self.create_widgets()
        else:
            messagebox.showerror("Error", "Username already exists.")

    def login(self):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="Login", font=("Arial", 16))
        self.label.pack(pady=10)

        tk.Label(self.frame, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.frame, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.frame, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(self.frame, text="Login", command=self.perform_login).pack(pady=5)
        tk.Button(self.frame, text="Back", command=self.create_widgets).pack(pady=5)

    def perform_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_manager.acc_login(username, password):
            messagebox.showinfo("Success", "Login Successful!")
            self.current_user = username
            self.user_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def user_menu(self):
        self.clear_frame()
        self.label = tk.Label(self.frame, text=f"Welcome {self.current_user}", font=("Arial", 16))
        self.label.pack(pady=10)

        tk.Button(self.frame, text="Show Available Dorms", command=self.show_dorms).pack(fill='x')
        tk.Button(self.frame, text="Show Map of GCH", command=self.show_map).pack(fill='x')
        tk.Button(self.frame, text="Dorm Information", command=self.dorm_info).pack(fill='x')
        tk.Button(self.frame, text="Logout", command=self.create_widgets).pack(fill='x')

    def show_dorms(self):
        messagebox.showinfo("Info", "Showing available dorms...")

    def show_map(self):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="Map of GCH", font=("Arial", 16))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(self.frame, width=400, height=300, bg="white")
        self.canvas.pack()

        self.canvas.create_rectangle(50, 100, 100, 100, outline="black")
        self.canvas.create_rectangle(110, 50, 160, 100, outline="black")
        self.canvas.create_rectangle(170, 50, 220, 100, outline="black")
        self.canvas.create_rectangle(50, 110, 100, 160, outline="black")
        self.canvas.create_rectangle(110, 110, 160, 160, outline="black")
        self.canvas.create_rectangle(170, 110, 220, 160, outline="black")
        self.canvas.create_rectangle(50, 170, 100, 220, outline="black")
        self.canvas.create_rectangle(110, 170, 160, 220, outline="black")
        self.canvas.create_rectangle(170, 170, 220, 220, outline="black")
        self.canvas.create_rectangle(50, 230, 100, 280, outline="black")
        self.canvas.create_rectangle(110, 230, 160, 280, outline="black")
        self.canvas.create_rectangle(170, 230, 220, 280, outline="black")

        tk.Button(self.frame, text="Back", command=self.user_menu).pack(pady=10)

    def dorm_info(self):
        messagebox.showinfo("Info", "Showing dorm information...")

    def clear_frame(self):
        if hasattr(self, 'frame'):
            for widget in self.frame.winfo_children():
                widget.destroy()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_database(self):
        return {
            'username': self.username,
            'password': self.password
        }

class UserManager:
    def __init__(self, user_file='users.json'):
        self.user_file = user_file
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.user_file):
            with open(self.user_file, 'r') as file:
                return json.load(file)
        return {}

    def save_users(self):
        with open(self.user_file, 'w') as file:
            json.dump(self.users, file)

    def acc_register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password).to_database()
        self.save_users()
        return True

    def acc_login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return True
        return False

class DormSystem:
    def __init__(self):
        pass

def text_appear_time(message, delay):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)

if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(400, 300)
    root.maxsize(400, 300) 
    user_manager = UserManager()
    main_menu = MainMenu(root, user_manager)
    root.mainloop()
