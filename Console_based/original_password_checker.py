# Basic Password Strength Checker
# Author: Saron Emanuel
# A simple tool to evaluate password strength based on cybersecurity best practices

import re
import random
import string

def check_password_strength(password):
    """
    Evaluate password strength based on security criteria
    Returns a score (0-100) and feedback
    """
    score = 0
    feedback = []
    
    # Check if password is empty
    if not password:
        return 0, ["Please enter a password."]
    
    # Check length (minimum 8 characters recommended)
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        feedback.append("Consider using a longer password (12+ characters).")
    else:
        feedback.append("Password is too short. Use at least 8 characters.")
    
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
        feedback.append("Avoid repeated characters (e.g., 'aaa', '111').")
    
    # Check for sequential patterns
    if re.search(r'(abc|bcd|cde|def|efg|123|234|345|456|567|678|789)', password.lower()):
        score -= 10
        feedback.append("Avoid sequential patterns (e.g., 'abc', '123').")
    
    # Check for common passwords (very basic check)
    common_passwords = ['password', '123456', 'qwerty', 'admin', 'welcome', 'letmein']
    if password.lower() in common_passwords:
        score = 0
        feedback = ["This is a commonly used password and extremely vulnerable to attacks."]
    
    # Ensure score is between 0 and 100
    score = max(0, min(100, score))
    
    # Add summary feedback
    if score < 40:
        feedback.insert(0, "Weak password. Please improve by following recommendations.")
    elif score < 70:
        feedback.insert(0, "Moderate password. Consider the suggestions for improvement.")
    elif score < 90:
        feedback.insert(0, "Good password, but could be stronger.")
    else:
        feedback.insert(0, "Strong password!")
    
    return score, feedback

def generate_strong_password():
    """Generate a strong random password"""
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
    
    # Add more random characters to reach desired length (12 chars)
    all_chars = uppercase + lowercase + digits + special
    password.extend(random.choice(all_chars) for _ in range(8))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

# Simple console-based version
def console_checker():
    print("=" * 50)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    print("This tool evaluates password strength based on cybersecurity best practices.")
    print("Type 'exit' to quit or 'generate' for a strong password.")
    
    while True:
        print("\n" + "-" * 50)
        password = input("Enter a password to check: ")
        
        if password.lower() == 'exit':
            print("Exiting program. Stay secure!")
            break
        
        if password.lower() == 'generate':
            strong_password = generate_strong_password()
            print(f"\nGenerated strong password: {strong_password}")
            continue
        
        score, feedback = check_password_strength(password)
        
        # Display strength
        if score < 40:
            strength = "WEAK"
        elif score < 70:
            strength = "MODERATE"
        elif score < 90:
            strength = "GOOD"
        else:
            strength = "STRONG"
        
        print(f"\nPassword Strength: {strength} ({score}/100)")
        
        # Display score as a simple visual bar
        filled = int(score / 5)
        bar = "[" + "#" * filled + "-" * (20 - filled) + "]"
        print(bar)
        
        # Display feedback
        print("\nFeedback:")
        for item in feedback:
            print(f"• {item}")

if __name__ == "__main__":
    console_checker()
