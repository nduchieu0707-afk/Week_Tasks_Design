import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import hashlib
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title):
        self.__title = title
    
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
    
    @abstractmethod
    def get_details(self):
        pass

class PhysicalBook(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.__author = author
    
    def get_author(self):
        return self.__author
    
    def get_details(self):
        return f"{self.get_title()}"

def hash_pw(passwords):
    return hashlib.sha256(passwords.encode()).hexdigest()

class Login():
    def __init__(self):
        self.login = tk.Tk()
        self.login.title("TASKS Manager")
        self.login.geometry("500x550")
        self.login.configure(bg="#2c3e50")
        
        tk.Label(self.login, text="TASKS MANAGER", font=("Arial", 20, "bold"), 
                bg="#2c3e50", fg="white").pack(pady=40)
        
        frame = tk.Frame(self.login, bg="#2c3e50")
        frame.pack(pady=20)
        
        tk.Label(frame, text="Username", bg="#2c3e50", fg="white", font=("Arial", 12)).pack(pady=5)
        self.username_entry = tk.Entry(frame, width=30, font=("Arial", 11))
        self.username_entry.pack(pady=5)
        
        tk.Label(frame, text="Password", bg="#2c3e50", fg="white", font=("Arial", 12)).pack(pady=5)
        self.password_entry = tk.Entry(frame, show="*", width=30, font=("Arial", 11))
        self.password_entry.pack(pady=5)
        
        tk.Button(frame, text="Login", command=self.login_ready, bg="#3498db", fg="white", 
                 width=20, font=("Arial", 11, "bold")).pack(pady=10)
        tk.Button(frame, text="Register", command=self.register_ready, bg="#2ecc71", fg="white", 
                 width=20, font=("Arial", 11, "bold")).pack(pady=5)
        
        self.login.mainloop()

    def login_ready(self):
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        username = self.username_entry.get()
        password = hash_pw(self.password_entry.get())
        c.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        if user:
            self.show_profile(user)
        else:
            messagebox.showerror("Error", "Invalid")

    def show_profile(self, user):
        self.login.destroy()
        self.profile = tk.Tk()
        self.profile.title(f"Profile: {user[0]}")
        self.profile.geometry("800x600")
        self.profile.configure(bg="#ecf0f1")
        
        header = tk.Frame(self.profile, bg="#34495e", height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text=f"Welcome {user[2]}", font=("Arial", 16, "bold"), 
                bg="#34495e", fg="white").pack(pady=20)
        
        info = tk.Frame(self.profile, bg="#bdc3c7", height=40)
        info.pack(fill=tk.X)
        info.pack_propagate(False)
        
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM tasks WHERE username = ?", (user[0],))
        tasks = c.fetchone()[0]
        conn.close()
        
        self.tasks = tk.Label(info, text=f"TASKS: {tasks}", bg="#bdc3c7", font=("Arial", 11))
        self.tasks.pack(side=tk.LEFT, padx=20, pady=8)
        tk.Label(info, text=f"Email: {user[4]}", bg="#bdc3c7", font=("Arial", 11)).pack(side=tk.LEFT, padx=20)
        tk.Button(info, text="Logout", command=self.logout_ready, bg="#e74c3c", fg="white", 
                 font=("Arial", 10, "bold")).pack(side=tk.RIGHT, padx=20)

        self.task_manager = TaskManager(self.profile, user[0], self.tasks)
        self.profile.mainloop()

    def logout_ready(self):
        self.profile.destroy()
        Login()

    def register_ready(self):
        register = tk.Toplevel(self.login)
        register.title("Register")
        register.geometry("350x450")
        register.configure(bg="#2c3e50")
        
        tk.Label(register, text="REGISTER", font=("Arial", 16, "bold"), 
                bg="#2c3e50", fg="white").pack(pady=20)
        
        fields = [("Username", False), ("Password", True), ("Name", False), ("Email", False)]
        entries = {}
        
        for label, hide in fields:
            tk.Label(register, text=label, bg="#2c3e50", fg="white").pack(pady=5)
            entry = tk.Entry(register, show="*" if hide else "", width=30)
            entry.pack(pady=5)
            entries[label] = entry

        def submit():
            username = entries["Username"].get()
            password = entries["Password"].get()
            name = entries["Name"].get()
            email = entries["Email"].get()
        
            if not all([username, password, name, email]):
                messagebox.showerror("Error", "Invalid")
                return
            
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            try:
                c.execute("INSERT INTO user VALUES (?, ?, ?, 0, ?)", (username, hash_pw(password), name, email))
                conn.commit()
                messagebox.showinfo("Success", "Account created!")
                register.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username exists")
            conn.close()
            
        tk.Button(register, text="Register", command=submit, bg="#2ecc71", fg="white", 
                 font=("Arial", 11, "bold")).pack(pady=20)

class TaskManager():
    def __init__(self, parent, username, label_tasks):
        self.username = username
        self.label_tasks = label_tasks
        self.conn = sqlite3.connect('tasks.db')
        self.c = self.conn.cursor()
        
        main = tk.Frame(parent, bg="#ecf0f1")
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        left = tk.Frame(main, bg="white", relief=tk.RAISED, bd=1)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,10))
        
        tk.Label(left, text="ADD TASKS", font=("Arial", 14, "bold"), bg="white").pack(pady=15)
        self.entry = tk.Entry(left, width=35, font=("Arial", 11))
        self.entry.pack(pady=10, padx=20)
        
        tk.Button(left, text="Save", command=self.add, bg="#27ae60", fg="white", 
                 width=15, font=("Arial", 10, "bold")).pack(pady=5)
        tk.Button(left, text="Edit", command=self.edit, bg="#f39c12", fg="white", 
                 width=15, font=("Arial", 10, "bold")).pack(pady=5)
        tk.Button(left, text="Delete", command=self.delete, bg="#e74c3c", fg="white", 
                 width=15, font=("Arial", 10, "bold")).pack(pady=5)
        
        right = tk.Frame(main, bg="white", relief=tk.RAISED, bd=1)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10,0))
        
        tk.Label(right, text="MY TASKS", font=("Arial", 14, "bold"), bg="white").pack(pady=15)
        
        scrollbar = tk.Scrollbar(right)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(right, width=40, height=15, font=("Arial", 10),
                                  yscrollcommand=scrollbar.set)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.config(command=self.listbox.yview)
        
        self.book_objects = []
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        self.c.execute("SELECT * FROM tasks WHERE username = ?", (self.username,))
        tasks = self.c.fetchall()
        
        self.book_objects.clear()
        for task in tasks:
            book = PhysicalBook(task[1], self.username)
            self.book_objects.append(book)
            self.listbox.insert(tk.END, f"{book.get_details()}")
        
        self.label_tasks.config(text=f"TASKS: {len(tasks)}")
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("UPDATE user SET number_tasks = ? WHERE username = ?", (len(tasks), self.username))
        conn.commit()
        conn.close()

    def add(self):
        if self.entry.get():
            self.c.execute("INSERT INTO tasks (title, username) VALUES (?, ?)", (self.entry.get(), self.username))
            self.conn.commit()
            self.entry.delete(0, tk.END)
            self.refresh()
        else:
            messagebox.showerror("Error", "Enter book title")

    def delete(self):
        if self.listbox.curselection():
            selected = self.listbox.get(self.listbox.curselection())
            title = selected.split(" ")[1]
            self.c.execute("DELETE FROM tasks WHERE title = ? AND username = ?", (title, self.username))
            self.conn.commit()
            self.refresh()
        else:
            messagebox.showerror("Error", "Select a book")

    def edit(self):
        if self.listbox.curselection() and self.entry.get():
            selected = self.listbox.get(self.listbox.curselection())
            old_title = selected.split(" ")[1]
            new_title = self.entry.get()
            self.c.execute("UPDATE tasks SET title = ? WHERE title = ? AND username = ?", (new_title, old_title, self.username))
            self.conn.commit()
            self.entry.delete(0, tk.END)
            self.refresh()
        else:
            messagebox.showerror("Error", "Select a book and enter new title")

if __name__ == "__main__":
    Login()