# 🔐 Password Strength Analyzer

A professional cybersecurity-focused Password Strength Analyzer built using Python and Tkinter.

This application evaluates password security using modern password validation techniques, entropy calculation, pattern detection, and cryptographic hashing concepts.

---

# 📌 Features

## ✅ Password Security Analysis
The application checks:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Repeated patterns
- Predictable sequences
- Common/weak passwords

---

## ✅ Password Strength Classification

Passwords are classified as:

- VERY WEAK
- WEAK
- MEDIUM
- STRONG
- VERY STRONG

---

## ✅ Security Scoring System

The analyzer calculates:
- Security score (0–10)
- Password entropy
- Password complexity level

Includes:
- Visual strength meter
- Real-time analysis report

---

## ✅ Secure Password Generator

Generate strong random passwords using:
- Uppercase letters
- Lowercase letters
- Digits
- Symbols

Uses Python's secure:
- `secrets` module

---

## ✅ Password Reuse Prevention

The application:
- Stores password hashes only
- Uses SHA-256 hashing
- Detects password reuse
- Never stores plain-text passwords

---

## ✅ Modern GUI

Built using:
- Tkinter

Features:
- Dark mode UI
- Password visibility toggle
- Analyze button
- Generate password button
- Strength progress bar
- Security report display

---

# 🛠 Technologies Used

- Python 3
- Tkinter
- Regex (`re`)
- SQLite3
- hashlib
- math
- secrets

---

# 📁 Project Structure

```text
PasswordStrengthAnalyzer/
│
├── main.py
├── password_checker.py
├── password_generator.py
├── database.py
├── common_passwords.txt
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Guide

## Step 1 — Install Python

Download and install Python:

https://www.python.org/downloads/

✅ Recommended Version:
- Python 3.10 or higher

---

## Step 2 — Download/Create Project Folder

Create a folder named:

```text
PasswordStrengthAnalyzer
```

Place all project files inside it.

---

## Step 3 — Open Terminal

Open terminal or command prompt inside the project folder.

Example:

```bash
cd PasswordStrengthAnalyzer
```

---

# ▶️ How To Run The Project

Run the application using:

```bash
python main.py
```

If `python` does not work:

```bash
python3 main.py
```

---

# 🖥 Expected GUI

The GUI includes:

- Password input field
- Show/Hide password option
- Analyze Password button
- Generate Password button
- Password strength progress bar
- Security analysis report area

---

# 📊 Example Output

```text
========================================
PASSWORD ANALYSIS REPORT
========================================

Length Check: PASS
Uppercase Check: PASS
Lowercase Check: PASS
Number Check: PASS
Special Character Check: PASS
Common Password Check: SAFE

Entropy Score: 92.4 bits

Password Strength: VERY STRONG
Security Score: 10/10

Suggestions:
- Excellent password security.
========================================
```

---

# 🔒 Security Concepts Used

## SHA-256 Hashing

Passwords are hashed using:

```python
hashlib.sha256()
```

This ensures:
- Passwords are not stored in plain text
- Secure password handling
- Better security practices

---

## Entropy Calculation

Entropy measures password randomness and unpredictability.

Higher entropy means:
- Harder to crack passwords
- Better resistance against brute-force attacks

---

## Common Password Detection

The app checks passwords against a database of weak/common passwords such as:

- 123456
- password
- qwerty
- admin123

---

# 🚀 Future Improvements

Possible upgrades:

- Copy-to-clipboard button
- Real-time typing analysis
- Animated strength meter
- Flask web version
- PDF report export
- Password breach API integration
- Advanced entropy visualization
- Cyberpunk UI theme

---

# 🧠 Skills Demonstrated

This project demonstrates:

- Cybersecurity fundamentals
- Password auditing
- Cryptography basics
- Regex validation
- SHA-256 hashing
- GUI development
- SQLite database handling
- Secure coding practices
- Modular Python programming

---

# ⚠️ Disclaimer

This project is intended for:
- Educational purposes
- Cybersecurity learning
- Ethical security demonstrations

Do not use this software for malicious activities.

---

# PINNINTI DEEKSHITH REDDY

Password Strength Analyzer Project  
Built using Python & Cybersecurity Concepts
