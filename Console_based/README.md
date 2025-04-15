# Password Strength Checker

A simple Python console application that evaluates password strength based on cybersecurity best practices.

Adapted from my Field Study in Cybersecurity course at VT!

## Overview

This lightweight tool helps users create and evaluate secure passwords by:
- Analyzing password complexity and strength
- Providing specific feedback for improvement
- Strong Password Generator: Creates cryptographically secure random passwords
- Displaying results with color-coded visual elements (optional)

## Features

### Core Functionality

- **Password Strength Evaluation**: Analyzes passwords against cybersecurity best practices
- **Detailed Feedback**: Provides specific improvement recommendations
- **Visual Strength Meter**: Shows password strength with a text-based progress bar

### Security Checks

The tool evaluates passwords based on several criteria:

- **Length**: Minimum recommended length of 8 characters, with 12+ being ideal
- **Character Types**: Presence of uppercase letters, lowercase letters, numbers, and special characters
- **Pattern Detection**: Identifies sequential (e.g., "abc", "123") and repetitive (e.g., "aaa") patterns
- **Common Password Detection**: Flags frequently used passwords that are vulnerable to attacks

### Color Display (Optional)

When run with the colorama library installed, the application provides:

- **Color-Coded Feedback**: 
  - Red for weak passwords (0-39%)
  - Yellow for moderate passwords (40-69%)
  - Blue for good passwords (70-89%)
  - Green for strong passwords (90-100%)
- **Colorful Interface Elements**: Enhances readability with colored headings, progress bars, and feedback points

## Installation

### Prerequisites
- Python 3.6 or higher

### Optional Dependencies
- colorama: For colored terminal output

### Setup
1. Clone this repository:
   ```
   git clone https://github.com/saronem/Console_based/password_checker.git
   cd password_checker
   ```

2. Install colorama (optional but recommended):
   ```
   python3 -m pip install colorama
   ```
   
   Or install from requirements.txt:
   ```
   python3 -m pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python3 Console_based/password_checker.py
   ```

2. Enter a password to check its strength.

3. Special commands:
   - Type `generate` to create a strong random password
   - Type `exit` to quit the program

### Example Output

With colorama installed, you'll see color-coded output:

```
============================================================
          PASSWORD STRENGTH CHECKER
============================================================
This tool evaluates password strength based on cybersecurity best practices.
Type 'exit' to quit or 'generate' for a strong password.

------------------------------------------------------------
Enter a password to check: mypassword123

Password Strength: MODERATE (60/100)
[############--------]

Feedback:
• Moderate password. Consider the suggestions for improvement.
• Add special characters (!@#$%^&*(),.?":{}|<>).
```

Without colorama, the application still functions perfectly with plain text output.

## How It Works

The password checker uses a scoring system based on security best practices:

1. **Base Score Calculation**:
   - Length (8+ chars: +15 points, 12+ chars: +25 points)
   - Uppercase letters (+15 points)
   - Lowercase letters (+15 points)
   - Numbers (+15 points)
   - Special characters (+15 points)

2. **Penalty Deductions**:
   - Repetitive patterns (-10 points)
   - Sequential patterns (-10 points)
   - Common passwords (score reduced to 0)

3. **Final Score Categorization**:
   - 0-39: Weak
   - 40-69: Moderate
   - 70-89: Good
   - 90-100: Strong

## Educational Value

This project demonstrates several important cybersecurity concepts:
- Password complexity requirements
- Common password vulnerabilities
- Basic pattern recognition
- Secure random password generation

It's an excellent practical introduction to password security principles for both developers and users.

## Future Enhancements

Potential improvements for future versions:
- Zxcvbn integration for more advanced password entropy calculation
- Password breach checking
- Password history tracking
- Configuration options for custom security policies
- More extensive password dictionaries

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Saron Emanuel

## Acknowledgments

- [NIST Special Publication 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) for password security guidelines
- [colorama](https://pypi.org/project/colorama/) for cross-platform colored terminal text
- Copilot for helping write this ReadMe and support the development of the password generation & color creation features!
