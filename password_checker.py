# Simple Password Strength Checker
# Author: Saron Emanuel
# A lightweight tool to evaluate password strength based on cybersecurity best practices (original)

import re
import PySimpleGUI as sg

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
    
    # Add more random characters to reach desired length (12 chars)
    all_chars = uppercase + lowercase + digits + special
    password.extend(random.choice(all_chars) for _ in range(8))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

def main():
    """Main function to create the GUI and handle events"""
    # Set theme
    sg.theme('LightGrey1')
    
    # Define layout
    layout = [
        [sg.Text('Password Strength Checker', font=('Helvetica', 16), justification='center', expand_x=True)],
        [sg.Text('Enter Password:', font=('Helvetica', 10)), sg.Input(key='-PASSWORD-', password_char='•')],
        [sg.Text('Strength:', font=('Helvetica', 10)), sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-')],
        [sg.Text('', key='-STRENGTH-')],
        [sg.Text('Feedback:', font=('Helvetica', 10))],
        [sg.Multiline(size=(50, 5), key='-FEEDBACK-', disabled=True)],
        [sg.Button('Generate Strong Password'), sg.Button('Exit')]
    ]
    
    # Create window
    window = sg.Window('Password Strength Checker', layout, size=(500, 300))
    
    # Event loop
    while True:
        event, values = window.read(timeout=200)  # Poll every 200ms
        
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        
        # Check password strength when input changes
        password = values['-PASSWORD-']
        score, feedback = check_password_strength(password)
        
        # Update UI
        window['-PROGRESS-'].update(score)
        
        # Set strength text with appropriate color
        if score < 40:
            strength = "Weak"
            color = 'red'
        elif score < 70:
            strength = "Moderate"
            color = 'orange'
        elif score < 90:
            strength = "Good"
            color = 'blue'
        else:
            strength = "Strong"
            color = 'green'
        
        window['-STRENGTH-'].update(f"Strength: {strength} ({score}%)")
        window['-STRENGTH-'].update(text_color=color)
        
        # Update feedback
        window['-FEEDBACK-'].update('\n'.join(feedback))
        
        # Generate strong password
        if event == 'Generate Strong Password':
            strong_password = generate_strong_password()
            window['-PASSWORD-'].update(strong_password)
    
    window.close()

if __name__ == '__main__':
    main()
