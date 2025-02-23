AI Password Strength Evaluator
A simple, interactive desktop application built with Kivy to evaluate the strength of passwords, generate secure passwords, and provide feedback on security metrics like brute-force resistance, adaptive security, and phishing resistance.

Features
Password Strength Checker: Analyzes your password based on length, uppercase letters, digits, and special characters.
Strength Metrics: Displays password strength, estimated brute-force time, adaptive security level, and phishing resistance.
Password Generator: Creates a random, strong 12-character password with a mix of letters, numbers, and symbols.
Clipboard Support: Copy your password to the clipboard with one click.
Visual Feedback: Includes a progress bar and color-coded strength indicators (red, yellow, green).
User-Friendly Interface: Built with Kivy for a clean, cross-platform experience.
Prerequisites
To run this application, you'll need:

Python 3.x (tested with Python 3.8+)
Kivy: A Python library for building cross-platform GUI applications.


Usage
Launch the App: Run the script as shown above, and a window titled "AI Password Strength Evaluator" will appear.
Check a Password:
Type a password into the text input field.
The app will automatically evaluate it and update the strength metrics and progress bar.
Generate a Password:
Click "Generate Strong Password" to create a random 12-character password.
A popup will display the generated password.
Copy to Clipboard:
Click "Copy to Clipboard" to copy the current password for use elsewhere.
A confirmation popup will appear.

How It Works
Strength Evaluation: The app checks for:
Length (>8 for "Strong", ≥6 for "Medium")
Presence of uppercase letters, digits, and punctuation.
Assigns a score (20 = Weak, 50 = Medium, 90 = Strong).
Metrics:
Brute Force Time: Estimated time to crack the password.
Adaptive Security: Resistance to adaptive hacking techniques.
Phishing Resistance: Likelihood of surviving phishing attempts.
Password Generation: Uses Python's random.choice with a mix of ASCII letters, digits, and punctuation.
Limitations
The strength evaluation is basic and heuristic-based, not a cryptographic analysis.
The app does not store or transmit passwords; all processing is local.
Requires Kivy, which may have compatibility issues on some systems.
Contributing
Feel free to fork this repository, submit issues, or create pull requests! Suggestions for improving the evaluation algorithm, adding new features, or enhancing the UI are welcome.

Acknowledgments
Built with Kivy, an open-source Python framework.
Inspired by the need for simple, user-friendly password tools.
