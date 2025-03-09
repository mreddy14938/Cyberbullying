
import tkinter as tk
from tkinter import messagebox

def detect_phishing_email(email_content):
    phishing_indicators = ["urgent", "verify your account", "update your password", "click the link below"]
    for indicator in phishing_indicators:
        if indicator in email_content.lower():
            return True
    return False

class PhishingDetectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Phishing Email Detection Simulator')
        self.geometry('400x300')
        
        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self, text="Enter the email content to check for phishing:")
        self.instruction_label.pack(pady=10)

        self.email_text = tk.Text(self, height=10)
        self.email_text.pack()

        self.check_button = tk.Button(self, text="Check for Phishing", command=self.check_email)
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", fg="red")
        self.result_label.pack(pady=10)

    def check_email(self):
        email_content = self.email_text.get("1.0", "end-1c")
        if detect_phishing_email(email_content):
            self.result_label.config(text="Warning: This email may be a phishing attempt.")
        else:
            self.result_label.config(text="This email appears to be safe.")

if __name__ == "__main__":
    app = PhishingDetectionApp()
    app.mainloop()
