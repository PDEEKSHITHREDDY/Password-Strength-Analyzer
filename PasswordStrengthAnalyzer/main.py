import tkinter as tk
from tkinter import ttk, messagebox

from password_checker import PasswordChecker
from password_generator import PasswordGenerator
from database import PasswordDatabase


checker = PasswordChecker()
db = PasswordDatabase()


class PasswordStrengthApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Professional Password Strength Analyzer")
        self.root.geometry("850x700")
        self.root.configure(bg="#0f172a")

        self.create_ui()

    def create_ui(self):

        title = tk.Label(
            self.root,
            text="PASSWORD STRENGTH ANALYZER",
            font=("Arial", 24, "bold"),
            fg="#38bdf8",
            bg="#0f172a"
        )

        title.pack(pady=20)

        # Password Entry
        self.password_var = tk.StringVar()

        password_frame = tk.Frame(self.root, bg="#0f172a")
        password_frame.pack(pady=10)

        password_label = tk.Label(
            password_frame,
            text="Enter Password:",
            font=("Arial", 14),
            fg="white",
            bg="#0f172a"
        )

        password_label.grid(row=0, column=0, padx=10)

        self.password_entry = tk.Entry(
            password_frame,
            textvariable=self.password_var,
            width=35,
            font=("Arial", 14),
            show="*",
            bg="#1e293b",
            fg="white",
            insertbackground="white"
        )

        self.password_entry.grid(row=0, column=1)

        # Show Password
        self.show_var = tk.BooleanVar()

        show_check = tk.Checkbutton(
            self.root,
            text="Show Password",
            variable=self.show_var,
            command=self.toggle_password,
            bg="#0f172a",
            fg="white",
            selectcolor="#0f172a",
            activebackground="#0f172a"
        )

        show_check.pack()

        # Buttons
        button_frame = tk.Frame(self.root, bg="#0f172a")
        button_frame.pack(pady=20)

        analyze_btn = tk.Button(
            button_frame,
            text="Analyze Password",
            command=self.analyze_password,
            bg="#2563eb",
            fg="white",
            font=("Arial", 12, "bold"),
            width=18
        )

        analyze_btn.grid(row=0, column=0, padx=10)

        generate_btn = tk.Button(
            button_frame,
            text="Generate Password",
            command=self.generate_password,
            bg="#16a34a",
            fg="white",
            font=("Arial", 12, "bold"),
            width=18
        )

        generate_btn.grid(row=0, column=1, padx=10)

        # Progress Bar
        self.progress = ttk.Progressbar(
            self.root,
            length=400,
            mode='determinate'
        )

        self.progress.pack(pady=20)

        # Result Box
        self.result_box = tk.Text(
            self.root,
            width=90,
            height=22,
            font=("Consolas", 11),
            bg="#1e293b",
            fg="#f8fafc"
        )

        self.result_box.pack(pady=10)

    def toggle_password(self):

        if self.show_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def analyze_password(self):

        password = self.password_var.get()

        if not password.strip():
            messagebox.showerror(
                "Error",
                "Password field cannot be empty."
            )
            return

        report = checker.check_password(password)

        suggestions = checker.get_suggestions(report)

        self.progress["value"] = report["score"] * 10

        self.result_box.delete(1.0, tk.END)

        output = ""

        output += "=" * 45 + "\n"
        output += "PASSWORD ANALYSIS REPORT\n"
        output += "=" * 45 + "\n\n"

        output += f"Length Check: {'PASS' if report['length'] else 'FAIL'}\n"
        output += f"Uppercase Check: {'PASS' if report['uppercase'] else 'FAIL'}\n"
        output += f"Lowercase Check: {'PASS' if report['lowercase'] else 'FAIL'}\n"
        output += f"Number Check: {'PASS' if report['numbers'] else 'FAIL'}\n"
        output += f"Special Character Check: {'PASS' if report['special'] else 'FAIL'}\n"

        output += (
            f"Common Password Check: "
            f"{'UNSAFE' if report['common'] else 'SAFE'}\n"
        )

        output += (
            f"Repeated Pattern Check: "
            f"{'DETECTED' if report['repeated'] else 'SAFE'}\n"
        )

        output += (
            f"Sequence Pattern Check: "
            f"{'DETECTED' if report['sequence'] else 'SAFE'}\n"
        )

        output += f"\nEntropy Score: {report['entropy']} bits\n"

        output += f"\nPassword Strength: {report['strength']}\n"
        output += f"Security Score: {report['score']}/10\n\n"

        output += "Suggestions:\n"

        if suggestions:
            for suggestion in suggestions:
                output += f"- {suggestion}\n"
        else:
            output += "- Excellent password security.\n"

        # Reuse Detection
        if db.password_exists(password):
            output += "\nWARNING: Password reuse detected!\n"
        else:
            db.save_password(password)

        self.result_box.insert(tk.END, output)

    def generate_password(self):

        generated = PasswordGenerator.generate_password()

        self.password_var.set(generated)

        messagebox.showinfo(
            "Generated Password",
            "Secure password generated successfully."
        )


root = tk.Tk()
app = PasswordStrengthApp(root)
root.mainloop()