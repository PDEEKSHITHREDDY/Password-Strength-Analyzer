import re
import math


class PasswordChecker:

    def __init__(self):
        self.common_passwords = self.load_common_passwords()

    def load_common_passwords(self):
        try:
            with open("common_passwords.txt", "r") as file:
                return set(line.strip() for line in file)
        except FileNotFoundError:
            return set()

    def calculate_entropy(self, password):
        charset = 0

        if re.search(r"[a-z]", password):
            charset += 26

        if re.search(r"[A-Z]", password):
            charset += 26

        if re.search(r"\d", password):
            charset += 10

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            charset += 32

        if charset == 0:
            return 0

        return round(len(password) * math.log2(charset), 2)

    def check_password(self, password):

        report = {}

        report["length"] = len(password) >= 8
        report["uppercase"] = bool(re.search(r"[A-Z]", password))
        report["lowercase"] = bool(re.search(r"[a-z]", password))
        report["numbers"] = bool(re.search(r"\d", password))
        report["special"] = bool(
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
        )

        report["common"] = password.lower() in self.common_passwords

        report["repeated"] = bool(
            re.search(r"(.)\1{2,}", password)
        )

        report["sequence"] = (
            "123" in password or
            "abc" in password.lower() or
            "qwerty" in password.lower()
        )

        report["entropy"] = self.calculate_entropy(password)

        score = 0

        if report["length"]:
            score += 2

        if report["uppercase"]:
            score += 1

        if report["lowercase"]:
            score += 1

        if report["numbers"]:
            score += 1

        if report["special"]:
            score += 2

        if not report["common"]:
            score += 1

        if not report["repeated"]:
            score += 1

        if not report["sequence"]:
            score += 1

        report["score"] = score

        if score <= 2:
            strength = "VERY WEAK"
        elif score <= 4:
            strength = "WEAK"
        elif score <= 6:
            strength = "MEDIUM"
        elif score <= 8:
            strength = "STRONG"
        else:
            strength = "VERY STRONG"

        report["strength"] = strength

        return report

    def get_suggestions(self, report):

        suggestions = []

        if not report["length"]:
            suggestions.append("Use at least 12 characters.")

        if not report["uppercase"]:
            suggestions.append("Add uppercase letters.")

        if not report["lowercase"]:
            suggestions.append("Add lowercase letters.")

        if not report["numbers"]:
            suggestions.append("Include numbers.")

        if not report["special"]:
            suggestions.append("Add special characters.")

        if report["common"]:
            suggestions.append("Avoid common passwords.")

        if report["repeated"]:
            suggestions.append("Avoid repeated characters.")

        if report["sequence"]:
            suggestions.append("Avoid predictable sequences.")

        return suggestions