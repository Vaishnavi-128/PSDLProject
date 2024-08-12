import tkinter as tk
import subprocess

def submit_username():
    username = username_entry.get()
    if username:
        print("Username:", username)
        # Proceed to the next page or any other action
        subprocess.run(['python', 'projectUI2.py'])
    else:
        error_label.config(text="Username field should not be empty")

# Create the main window
root = tk.Tk()
root.title("Background Image Example")

# Load your background image (replace 'bg.png' with your image file)
background_image = tk.PhotoImage(file="bg.png")

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Cover the whole window

# Add a label to display the project title
project_title = tk.Label(root, text="CountToLift: Elevator Magic with Fingers", font=("Arial", 36), fg="white", bg="blue")
project_title.pack(fill=tk.X)

# Create a label for the username with a different font and color
username_label = tk.Label(root, text="Username", font=("Arial", 20), fg="Black", bg="white")
username_label.pack(pady=(30, 10))  # Add vertical spacing

# Create an entry for the username with a border
username_entry = tk.Entry(root, font=("Arial", 20), bd=2, relief=tk.SOLID)
username_entry.pack(pady=10)  # Add vertical spacing

# Create a button to submit the username with a border
submit_button = tk.Button(root, text="Submit", command=submit_username, font=("Arial", 20), bg="blue", fg="white", bd=2, relief=tk.SOLID)
submit_button.pack(pady=(10, 30))  # Add vertical spacing

# Create a label to display validation error
error_label = tk.Label(root, text="", font=("Arial", 16), fg="red", bg="white")
error_label.pack()

# Center the elements on top of the background
root.update_idletasks()  # Make sure the window size is updated
project_title.place(relx=0.5, rely=0, anchor='n')
username_label.place(relx=0.5, rely=0.4, anchor='center')
username_entry.place(relx=0.5, rely=0.5, anchor='center')
submit_button.place(relx=0.5, rely=0.6, anchor='center')

# Start the Tkinter main loop
root.mainloop()
