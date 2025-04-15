# Password Strength Checker

A Python application that evaluates password strength based on industry best practices and checks for potential data breaches.

![Password Strength Checker Screenshot](https://github.com/sarone/password-strength-checker/raw/main/screenshot.png)

## Overview

This tool helps users create and evaluate secure passwords by:
- Analyzing password complexity and strength
- Providing specific feedback for improvement
- Checking if passwords have appeared in known data breaches
- Generating strong random passwords

## Features

### 1. Password Strength Analysis
- Visual meter showing password strength from 0-100%
- Color-coded indicators (red, yellow, light green, green)
- Calculates score based on industry-standard criteria

### 2. Comprehensive Feedback
- Provides specific suggestions for improving password security
- Identifies common password vulnerabilities:
  - Insufficient length
  - Missing character types (uppercase, lowercase, numbers, symbols)
  - Sequential patterns (abc, 123)
  - Repetitive characters (aaa, 111)
  - Common dictionary words

### 3. Data Breach Verification
- Checks if a password has appeared in known data breaches
- Uses the "Have I Been Pwned" API with k-anonymity model for secure checking
- Only the first 5 characters of the password hash are sent over the network

### 4. Strong Password Generator
- Creates cryptographically strong random passwords
- Ensures all character types are included
- Default length of 16 characters for optimal security

## Technical Implementation

- Built with Python 3.x
- Uses Tkinter for the graphical user interface
- Implements industry-standard password security checks
- Integrates with the "Have I Been Pwned" API for breach checking
- Uses secure hashing (SHA-1) with k-anonymity for privacy protection

## Installation

### Prerequisites
- Python 3.7 or higher
- Internet connection (for data breach checking)

### Required Packages
```
requests
```

### Setup
1. Clone this repository:
   ```
   git clone https://github.com/saronem/password-strength-checker.git
   cd password-strength-checker
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
   
   Or install individually:
   ```
   pip install requests
   ```

## Usage

1. Run the application:
   ```
   python password_checker.py
   ```

2. Enter a password in the text field
   - The strength meter updates in real-time as you type
   - Feedback appears in the text area below

3. Click "Check Data Breach" to verify if your password has been exposed in known data breaches

4. Click "Generate Strong Password" to create a new secure password

## Security Considerations

- No passwords are stored or transmitted in plain text
- Data breach checking uses a k-anonymity model
- Only the first 5 characters of the SHA-1 hash are sent over the network
- The application does not store any passwords or history

## Educational Value

This project demonstrates several important cybersecurity concepts:
- Password complexity requirements
- Common password vulnerabilities
- Secure API integration
- K-anonymity model for privacy protection
- Hash functions for secure data handling

## Future Enhancements

Potential improvements for future versions:
- Password manager integration
- Custom complexity policy settings
- Password expiration tracking
- Multi-language support
- Dark mode theme

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Saron Emanuel

## Notes

API connectivity and Tkinter config (prettification) was adding in support with Copilot! Still learning how to expand security tooling with AI!

## Acknowledgments

- [Have I Been Pwned](https://haveibeenpwned.com/) for the password breach API
- [NIST Special Publication 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) for password security guidelines
