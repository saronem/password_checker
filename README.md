# Simple Password Strength Checker

A lightweight Python application that evaluates password strength based on cybersecurity best practices.
Based on VT Project for Cybersecurity Field Study

![Password Strength Checker Screenshot](https://github.com/sarone/password-strength-checker/raw/main/screenshot.png)

## Overview

This tool helps users create and evaluate secure passwords by:
- Analyzing password complexity and strength
- Providing specific feedback for improvement
- Generating strong random passwords

## Features

### 1. Password Strength Analysis
- Visual meter showing password strength from 0-100%
- Color-coded indicators (red, orange, blue, green)
- Calculates score based on cybersecurity best practices

### 2. Comprehensive Feedback
- Provides specific suggestions for improving password security
- Identifies common password vulnerabilities:
  - Insufficient length
  - Missing character types (uppercase, lowercase, numbers, symbols)
  - Sequential patterns (abc, 123)
  - Repetitive characters (aaa, 111)
  - Common dictionary words

### 3. Strong Password Generator
- Creates cryptographically strong random passwords
- Ensures all character types are included
- Default length of 12 characters for good security

## Technical Implementation

- Built with Python 3.x
- Uses PySimpleGUI for a simple, clean graphical user interface
- Implements industry-standard password security checks
- No external API dependencies - works completely offline
- Lightweight and easy to understand for beginner developers

## Installation

### Prerequisites
- Python 3.7 or higher

### Required Packages
```
PySimpleGUI
```

### Setup
1. Clone this repository:
   ```
   git clone https://github.com/saronem/password_checker.git
   cd password_checker
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
   
   Or install individually:
   ```
   pip install PySimpleGUI
   ```

## Usage

1. Run the application:
   ```
   python password_checker.py
   ```

2. Enter a password in the text field
   - The strength meter updates in real-time as you type
   - Feedback appears in the text area below

3. Click "Generate Strong Password" to create a new secure password

## Security Considerations

- No passwords are stored or transmitted
- The application works completely offline
- No internet connection required
- The application does not store any passwords or history

## Educational Value

This project demonstrates several important cybersecurity concepts:
- Password complexity requirements
- Common password vulnerabilities
- Password entropy and strength calculation
- Secure random password generation
- Defense against common password attacks

## Future Enhancements

Potential improvements for future versions:
- Data breach checking (optional API integration)
- Custom complexity policy settings
- Password history tracking
- Multi-language support
- Dark mode theme
- Password strength visualization with charts

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Saron Emanuel

## Acknowledgments

- [Have I Been Pwned](https://haveibeenpwned.com/) for the password breach API
- [NIST Special Publication 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) for password security guidelines
