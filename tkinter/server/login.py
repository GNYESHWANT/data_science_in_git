import tkinter as tk
from tkinter import messagebox
from  subprocess import call

# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()
    server=server_entry.get()


    # You can add your own validation logic here
    if userid == "admin" and password == "password":
       if server=="Server":
         call(["python","server_creater.py"])
       elif server=="client":
         call(["python","client.py"])
       else:
          messagebox.showerror("wrong type ","please enter a valid sever")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Create and place the username label and entry
username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

server_name=tk.Label(parent,text="servername")
server_name.pack()
server_entry=tk.Entry(parent)
server_entry.pack()
# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
parent.mainloop()