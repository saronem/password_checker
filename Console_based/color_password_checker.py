# Password Strength Checker with Color
# Author: Saron Emanuel
# A simple tool to evaluate password strength with colorful terminal output

import re
import random
import string

# Import colorama for cross-platform colored terminal output
try:
    from colorama import init, Fore, Back, Style
    # Initialize colorama
    init(autoreset=True)
    has_color = True
except ImportError:
    # Create dummy color classes if colorama is not available
    class DummyFore:
        def __init__(self):
            self.RED = ''
            self.YELLOW = ''
            self.GREEN = ''
            self.BLUE = ''
            self.CYAN = ''
            self.WHITE = ''
            self.MAGENTA = ''
            self.RESET = ''
    
    class DummyBack:
        def __init__(self):
            self.RED = ''
            self.YELLOW = ''
            self.GREEN = ''
            self.BLUE = ''
            self.BLACK = ''
            self.RESET = ''
    
    class DummyStyle:
        def __init__(self):
            self.BRIGHT = ''
            self.DIM = ''
            self.NORMAL = ''
            self.RESET_ALL = ''
    
    Fore = DummyFore()
    Back = DummyBack()
    Style = DummyStyle()
    has_color = False
    print("Tip: Install colorama for colored output: pip install colorama")

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

def print_title():
    """Print a colorful title banner"""
    if has_color:
        print(Fore.CYAN + Style.BRIGHT + "=" * 60)
        print(Fore.CYAN + Style.BRIGHT + "          PASSWORD STRENGTH CHECKER")
        print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    else:
        print("=" * 60)
        print("          PASSWORD STRENGTH CHECKER")
        print("=" * 60)
    
    print("This tool evaluates password strength based on cybersecurity best practices.")
    print("Type 'exit' to quit or 'generate' for a strong password.")

def print_strength_bar(score):
    """Print a colorful strength bar based on the score"""
    filled = int(score / 5)  # 20 segments for 100%
    
    if has_color:
        # Choose color based on score
        if score < 40:
            bar_color = Fore.RED
        elif score < 70:
            bar_color = Fore.YELLOW
        elif score < 90:
            bar_color = Fore.BLUE
        else:
            bar_color = Fore.GREEN
        
        # Create the bar
        bar = "[" + bar_color + "#" * filled + Fore.WHITE + "-" * (20 - filled) + Fore.RESET + "]"
    else:
        bar = "[" + "#" * filled + "-" * (20 - filled) + "]"
    
    return bar

def print_strength_text(score):
    """Print the strength text with appropriate color"""
    if score < 40:
        strength = "WEAK"
        color = Fore.RED
    elif score < 70:
        strength = "MODERATE"
        color = Fore.YELLOW
    elif score < 90:
        strength = "GOOD"
        color = Fore.BLUE
    else:
        strength = "STRONG"
        color = Fore.GREEN
    
    if has_color:
        return f"{color}{Style.BRIGHT}{strength}{Style.RESET_ALL} ({score}/100)"
    else:
        return f"{strength} ({score}/100)"

def print_feedback(feedback):
    """Print the feedback with appropriate colors"""
    print("\nFeedback:")
    
    for i, item in enumerate(feedback):
        if i == 0:  # The first item is the summary
            if "Weak" in item:
                color = Fore.RED
            elif "Moderate" in item:
                color = Fore.YELLOW
            elif "Good" in item:
                color = Fore.BLUE
            else:
                color = Fore.GREEN
        else:
            color = Fore.WHITE
        
        if has_color:
            print(f"{Fore.CYAN}• {color}{item}{Style.RESET_ALL}")
        else:
            print(f"• {item}")

# Console-based password checker
def console_checker():
    print_title()
    
    while True:
        if has_color:
            print("\n" + Fore.WHITE + "-" * 60)
            password = input(Fore.CYAN + "Enter a password to check: " + Fore.WHITE)
        else:
            print("\n" + "-" * 60)
            password = input("Enter a password to check: ")
        
        if password.lower() == 'exit':
            if has_color:
                print(Fore.GREEN + "\nExiting program. Stay secure!" + Style.RESET_ALL)
            else:
                print("\nExiting program. Stay secure!")
            break
        
        if password.lower() == 'generate':
            strong_password = generate_strong_password()
            if has_color:
                print(f"\n{Fore.GREEN}Generated strong password: {Fore.CYAN}{Style.BRIGHT}{strong_password}{Style.RESET_ALL}")
            else:
                print(f"\nGenerated strong password: {strong_password}")
            continue
        
        score, feedback = check_password_strength(password)
        
        # Display strength
        print(f"\nPassword Strength: {print_strength_text(score)}")
        
        # Display score as a visual bar
        print(print_strength_bar(score))
        
        # Display feedback
        print_feedback(feedback)

if __name__ == "__main__":
    console_checker()
