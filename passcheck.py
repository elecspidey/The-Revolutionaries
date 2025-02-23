from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard
import string
import random

class PasswordStrengthApp(App):
    def build(self):
        self.title = "AI Password Strength Evaluator"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.lbl_title = Label(text="AI Password Strength Checker", font_size=24, size_hint=(1, 0.2))
        layout.add_widget(self.lbl_title)
        
        self.entry_password = TextInput(password=True, multiline=False, font_size=18, size_hint=(1, 0.2))
        self.entry_password.bind(text=self.check_strength)
        layout.add_widget(self.entry_password)
        
        self.generate_button = Button(text="Generate Strong Password", on_press=self.generate_password, size_hint=(1, 0.2))
        layout.add_widget(self.generate_button)
        
        self.copy_button = Button(text="Copy to Clipboard", on_press=self.copy_to_clipboard, size_hint=(1, 0.2))
        layout.add_widget(self.copy_button)
        
        self.lbl_strength = Label(text="Strength: ", font_size=18, size_hint=(1, 0.2))
        layout.add_widget(self.lbl_strength)
        
        self.progress_bar = ProgressBar(max=100, size_hint=(1, 0.2))
        layout.add_widget(self.progress_bar)
        
        self.lbl_brute_force = Label(text="Brute Force Time: ", font_size=18, size_hint=(1, 0.2))
        layout.add_widget(self.lbl_brute_force)
        
        self.lbl_adaptive_security = Label(text="Adaptive Security: ", font_size=18, size_hint=(1, 0.2))
        layout.add_widget(self.lbl_adaptive_security)
        
        self.lbl_phishing_resistance = Label(text="Phishing Resistance: ", font_size=18, size_hint=(1, 0.2))
        layout.add_widget(self.lbl_phishing_resistance)
        
        self.lbl_tips = Label(text="Tips: Use a mix of letters, numbers, and symbols.", font_size=14, size_hint=(1, 0.2))
        layout.add_widget(self.lbl_tips)
        
        return layout

    def check_strength(self, instance=None, value=None):
        password = self.entry_password.text
        strength = "Weak"
        brute_force_time = "Instantly Cracked"
        adaptive_security = "Low"
        phishing_resistance = "Low"
        color = (1, 0, 0, 1)  # Red
        score = 20

        # Check password complexity
        if len(password) > 8 and any(char.isupper() for char in password) and \
           any(char.isdigit() for char in password) and any(char in string.punctuation for char in password):
            strength = "Strong"
            brute_force_time = "Several Years"
            adaptive_security = "High"
            phishing_resistance = "High"
            color = (0, 1, 0, 1)  # Green
            score = 90
        elif len(password) >= 6:
            strength = "Medium"
            brute_force_time = "Few Hours"
            adaptive_security = "Moderate"
            phishing_resistance = "Moderate"
            color = (1, 1, 0, 1)  # Yellow
            score = 50

        # Update UI
        self.lbl_strength.text = f"Strength: {strength}"
        self.lbl_strength.color = color
        self.progress_bar.value = score
        self.lbl_brute_force.text = f"Brute Force Time: {brute_force_time}"
        self.lbl_adaptive_security.text = f"Adaptive Security: {adaptive_security}"
        self.lbl_phishing_resistance.text = f"Phishing Resistance: {phishing_resistance}"

    def generate_password(self, instance):
        length = 12  # Fixed length for generated password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.entry_password.text = password
        self.show_popup("Generated Password", password)

    def copy_to_clipboard(self, instance):
        Clipboard.copy(self.entry_password.text)
        self.show_popup("Copied to Clipboard", "Password copied to clipboard!")

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_label = Label(text=message, font_size=18)
        popup_button = Button(text="Close", size_hint=(1, 0.2))
        popup_layout.add_widget(popup_label)  
        popup_layout.add_widget(popup_button)
        
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    PasswordStrengthApp().run()