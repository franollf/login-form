import tkinter as tk
from tkinter import messagebox


# Dictionary to store user accounts
user_accounts = {}

# Function to load account data from the file
def load_accounts():
    try:
        with open("tkinter/accounts.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Username:") and ", Password:" in line:
                    parts = line.split(", Password: ")
                    username = parts[0].replace("Username: ", "")
                    password = parts[1].strip()
                    user_accounts[username] = password
    except FileNotFoundError:
        pass  # Handle the case where the file doesn't exist

# Function to switch back to login frame when then button is pressed
def switch_to_login_frame():
    create_account_frame.pack_forget()
    login_frame.pack()
    create_account_button.pack(side="top", pady=10)
    back_to_login_button.pack_forget()

# Function to switch to Create Account frame when then button is pressed
def switch_to_create_account_frame():
    login_frame.pack_forget()
    create_account_frame.pack()
    create_account_button.pack_forget()
    back_to_login_button.pack(side="top", pady=10)


def center_frame(frame):
    frame.pack(expand=True, fill="both")


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the provided username exists and the password is correct
    if username in user_accounts and user_accounts[username] == password:
        messagebox.showinfo(title="Login Success",
                            message="You Successfully Logged In.")
    else:
        messagebox.showerror(title="Error", message="Invalid Login")


def create_account():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    if not new_username or not new_password:
        messagebox.showerror(
            title="Error", message="Username and password are required.")

    elif new_username in user_accounts:
        messagebox.showerror(
            title="Error", message="Username is already taken.")
    else:
        try:
            with open("tkinter/accounts.txt", "a") as file:
                file.write(
                    f"Username: {new_username}, Password: {new_password}\n")
            messagebox.showinfo(title="Account Created",
                                message="Account Successfully Created.")
            switch_to_login_frame()
        except Exception as e:
            messagebox.showerror(
                title="Error", message=f"An error occurred: {str(e)}")


# Load user accounts from the file when the program starts
load_accounts()

root = tk.Tk()
root.title("Login Form")

# Making the frame accessible for login
login_frame = tk.Frame(root)
login_label = tk.Label(login_frame, text="Login", font=("Arial", 30))
username_label = tk.Label(login_frame, text="Username", font=("Arial", 16))
username_entry = tk.Entry(login_frame, font=("Arial", 16))
password_label = tk.Label(login_frame, text="Password", font=("Arial", 16))
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 16))
login_button = tk.Button(login_frame, text="Login",
                         font=("Arial", 16), command=login)
# Adding a Create Account Button to bring to another page
create_account_button = tk.Button(login_frame, text="Create Account", font=(
    "Arial", 16), command=switch_to_create_account_frame)

login_label.pack(side="top", pady=40)
username_label.pack()
username_entry.pack(pady=20)
password_label.pack()
password_entry.pack(pady=20)
login_button.pack(side="top", pady=30)
create_account_button.pack(side="top", pady=10)

# Making the Frame Accessible for Creating an Account
create_account_frame = tk.Frame(root)
create_account_label = tk.Label(
    create_account_frame, text="Create Account", font=("Arial", 30))
new_username_label = tk.Label(
    create_account_frame, text="New Username", font=("Arial", 16))
new_username_entry = tk.Entry(create_account_frame, font=("Arial", 16))
new_password_label = tk.Label(
    create_account_frame, text="New Password", font=("Arial", 16))
new_password_entry = tk.Entry(
    create_account_frame, show="*", font=("Arial", 16))
create_button = tk.Button(create_account_frame, text="Create", font=(
    "Arial", 16), command=create_account)
back_to_login_button = tk.Button(create_account_frame, text="Back to Login", font=(
    "Arial", 16), command=switch_to_login_frame)

create_account_label.pack(side="top", pady=40)
new_username_label.pack()
new_username_entry.pack(pady=20)
new_password_label.pack()
new_password_entry.pack(pady=20)
create_button.pack(side="top", pady=10)  # Add the "Create" button
back_to_login_button.pack(side="top", pady=10)

switch_to_login_frame()
root.geometry("340x440")
root.mainloop()
