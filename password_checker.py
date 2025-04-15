# Password Strength Checker
# Author: Saron Emanuel
# A simple tool to evaluate password strength based on industry best practices
# Migrating from my VT projects GH + adding improvements with support from GH Copilot

import re
import tkinter as tk
from tkinter import ttk
import hashlib
import requests

class PasswordStrengthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Set styles
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 11))
        self.style.configure("TButton", font=("Arial", 11))
        self.style.configure("Header.TLabel", font=("Arial", 14, "bold"))
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create header
        header = ttk.Label(self.main_frame, text="Password Strength Checker", style="Header.TLabel")
        header.pack(pady=(0, 20))
        
        # Create password input field
        password_frame = ttk.Frame(self.main_frame)
        password_frame.pack(fill=tk.X, pady=5)
        
        password_label = ttk.Label(password_frame, text="Enter Password:")
        password_label.pack(anchor=tk.W)
        
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(password_frame, textvariable=self.password_var, show="•", width=40)
        self.password_entry.pack(fill=tk.X, pady=5)
        self.password_entry.bind("<KeyRelease>", self.check_password)
        
        # Create strength meter
        meter_frame = ttk.Frame(self.main_frame)
        meter_frame.pack(fill=tk.X, pady=10)
        
        meter_label = ttk.Label(meter_frame, text="Password Strength:")
        meter_label.pack(anchor=tk.W)
        
        self.meter = ttk.Progressbar(meter_frame, orient="horizontal", length=400, mode="determinate")
        self.meter.pack(fill=tk.X, pady=5)
        
        self.strength_label = ttk.Label(meter_frame, text="")
        self.strength_label.pack(anchor=tk.W)
        
        # Create feedback area
        feedback_frame = ttk.Frame(self.main_frame)
        feedback_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        feedback_label = ttk.Label(feedback_frame, text="Feedback:")
        feedback_label.pack(anchor=tk.W)
        
        self.feedback_text = tk.Text(feedback_frame, height=8, width=50, wrap=tk.WORD, bg="#f9f9f9", relief=tk.FLAT)
        self.feedback_text.pack(fill=tk.BOTH, expand=True, pady=5)
        self.feedback_text.config(state=tk.DISABLED)
        
        # Create check button (for future extensions like haveibeenpwned check)
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(fill=tk.X, pady=10)
        
        check_button = ttk.Button(buttons_frame, text="Check Data Breach", command=self.check_data_breach)
        check_button.pack(side=tk.LEFT, padx=5)
        
        generate_button = ttk.Button(buttons_frame, text="Generate Strong Password", command=self.generate_password)
        generate_button.pack(side=tk.RIGHT, padx=5)
        
        # Set criteria
        self.length_criterion = 8
        self.min_score_for_strong = 80
        
        # Welcome message
        self.update_feedback("Enter a password to check its strength.\n\nA strong password should:\n- Be at least 8 characters long\n- Include uppercase and lowercase letters\n- Include numbers\n- Include special characters\n- Avoid common patterns")
    
    def check_password(self, event=None):
        """Check password strength and update the UI"""
        password = self.password_var.get()
        
        if not password:
            self.meter["value"] = 0
            self.strength_label.config(text="")
            self.update_feedback("Enter a password to check its strength.")
            return
        
        # Calculate score
        score = 0
        feedback = []
        
        # Check length
        if len(password) >= self.length_criterion:
            score += 20
        else:
            feedback.append(f"Password should be at least {self.length_criterion} characters long.")
        
        # Check for uppercase letters
        if re.search(r'[A-Z]', password):
            score += 15
        else:
            feedback.append("Add uppercase letters (A-Z).")
        
        # Check for lowercase letters
        if re.search(r'[a-z]', password):
            score += 15
        else:
            feedback.append("Add lowercase letters (a-z).")
        
        # Check for numbers
        if re.search(r'[0-9]', password):
            score += 15
        else:
            feedback.append("Add numbers (0-9).")
        
        # Check for special characters
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 15
        else:
            feedback.append("Add special characters (!@#$%^&*(),.?\":{}|<>).")
        
        # Check for repetitive patterns
        if re.search(r'(.)\1{2,}', password):  # Same character repeated 3+ times
            score -= 10
            feedback.append("Avoid repeated characters (e.g., 'aaa').")
        
        # Check for sequential patterns
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|012|123|234|345|456|567|678|789)', password.lower()):
            score -= 10
            feedback.append("Avoid sequential patterns (e.g., 'abc', '123').")
        
        # Check for common passwords (very basic check)
        common_passwords = ['password', '123456', 'qwerty', 'admin', 'welcome', 'letmein']
        if password.lower() in common_passwords:
            score = 0
            feedback = ["This is a commonly used password and extremely vulnerable to attacks."]
        
        # Ensure score is between 0 and 100
        score = max(0, min(100, score))
        
        # Update UI
        self.meter["value"] = score
        
        if score < 40:
            strength = "Weak"
            color = "#ff6666"  # Red
        elif score < 70:
            strength = "Moderate"
            color = "#ffcc66"  # Yellow
        elif score < self.min_score_for_strong:
            strength = "Good"
            color = "#99cc66"  # Light Green
        else:
            strength = "Strong"
            color = "#66cc66"  # Green
        
        self.strength_label.config(text=f"Strength: {strength} ({score}%)")
        
        # Update feedback
        if not feedback:
            feedback.append("Your password meets all basic security criteria.")
        
        self.update_feedback("\n".join(feedback))
        
        # Change meter color based on strength
        self.style.configure("TProgressbar", background=color)
    
    def check_data_breach(self):
        """Check if password has been exposed in data breaches using k-anonymity model"""
        password = self.password_var.get()
        
        if not password:
            self.update_feedback("Please enter a password first.")
            return
        
        # Calculate SHA-1 hash of the password
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        try:
            # Use haveibeenpwned API with k-anonymity model
            url = f"https://api.pwnedpasswords.com/range/{prefix}"
            response = requests.get(url)
            
            if response.status_code == 200:
                # Check if the suffix is in the response
                hashes = (line.split(':') for line in response.text.splitlines())
                for hash_suffix, count in hashes:
                    if hash_suffix == suffix:
                        count = int(count)
                        self.update_feedback(f"❌ This password has been found in {count:,} data breaches!\nIt is strongly recommended to choose a different password.")
                        return
                
                self.update_feedback("✓ Good news! This password hasn't been found in known data breaches.")
            else:
                self.update_feedback("Unable to check for data breaches. Service might be unavailable.")
        
        except Exception as e:
            self.update_feedback(f"Error checking for data breaches: {str(e)}")
    
    def generate_password(self):
        """Generate a strong random password"""
        import random
        import string
        
        # Define character sets
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        special = '!@#$%^&*()_-+=<>?'
        
        # Ensure at least one character from each set
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(special)
        ]
        
        # Add more random characters to reach desired length (16 chars)
        all_chars = uppercase + lowercase + digits + special
        password.extend(random.choice(all_chars) for _ in range(12))
        
        # Shuffle the password
        random.shuffle(password)
        password = ''.join(password)
        
        # Update UI
        self.password_var.set(password)
        self.check_password()
    
    def update_feedback(self, text):
        """Update the feedback text widget"""
        self.feedback_text.config(state=tk.NORMAL)
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_text.insert(tk.END, text)
        self.feedback_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
