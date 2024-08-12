import tkinter as tk
import subprocess


def skip_button():
    subprocess.run(['python', 'project.py'])
# Create the main window
root = tk.Tk()
root.title("Background Image Example")

# Load your background image (replace 'bg2.png' with your image file)
background_image = tk.PhotoImage(file="bg2.png")

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the whole window

# Add a label to display the project title
project_title = tk.Label(root, text="Undertake an exploratory trials", font=("Arial", 36), fg="white", bg="blue")
project_title.pack(fill=tk.X)

# Create a button to submit the username with a border
submit_button = tk.Button(root, text="Skip for now",command=skip_button, font=("Arial", 20), bg="blue", fg="white", bd=2, relief=tk.SOLID)
submit_button.pack(pady=(10,30))  # Add vertical spacing

# Center the elements on top of the background
root.update_idletasks()  # Make sure the window size is updated
project_title.place(relx=0.5, rely=0, anchor='n')
submit_button.place(relx=0.5, rely=0.9, anchor='center')

# Start the Tkinter main loop
root.mainloop()