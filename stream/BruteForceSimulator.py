
import tkinter as tk
import itertools
import time

class BruteForceSimulatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Brute Force Attack Simulator')
        self.geometry('400x300')

        # Variable to store the user's password
        self.password = tk.StringVar()

        # Create the GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Instruction label
        self.instruction_label = tk.Label(self, text="Enter a password to simulate a brute force attack:")
        self.instruction_label.pack(pady=10)

        # Password entry
        self.password_entry = tk.Entry(self, textvariable=self.password, show="*")
        self.password_entry.pack()

        # Brute force button
        self.brute_force_button = tk.Button(self, text="Start Brute Force Attack", command=self.brute_force_attack)
        self.brute_force_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(self, text="", fg="red")
        self.result_label.pack(pady=10)

    def brute_force_attack(self):
        # Get the password from the entry widget
        password_to_crack = self.password.get()

        # Define character set and initialize attempts
        charset = 'abcdefghijklmnopqrstuvwxyz'
        attempts = 0
        start_time = time.time()

        # Brute force attack
        for length in range(1, len(password_to_crack) + 1):
            for attempt in itertools.product(charset, repeat=length):
                attempts += 1
                attempt_password = ''.join(attempt)
                if attempt_password == password_to_crack:
                    time_taken = time.time() - start_time
                    self.result_label.config(text=f"Password cracked in {attempts} attempts and {time_taken:.2f} seconds.")
                    return
        
        # If password is not cracked
        self.result_label.config(text="Failed to crack the password within the character limit.")

# The main application
if __name__ == "__main__":
    app = BruteForceSimulatorApp()
    app.mainloop()
